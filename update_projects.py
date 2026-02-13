import sys
import io
import json

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def modify_projects():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 이전에 생성된 프로젝트 ID 파일 로드
    try:
        with open("created_projects_final.json", "r", encoding="utf-8") as f:
            existing_projects = json.load(f)
    except FileNotFoundError:
        print("❌ 이전 프로젝트 목록 파일을 찾을 수 없습니다.")
        return

    # [1] 유지할 프로젝트 (번호 기준: 1, 3, 5, 6, 8, 9, 10)
    # 인덱스는 0부터 시작하므로 -1 해줌
    keep_indices = [0, 2, 4, 5, 7, 8, 9] 
    
    # 삭제할 프로젝트 ID 수집
    to_delete = []
    kept_projects = []
    
    for i, project in enumerate(existing_projects):
        if i in keep_indices:
            kept_projects.append(project)
        else:
            to_delete.append(project)

    # [2] 삭제 실행 (비동기라 생각하고 요청만 보냄)
    print(f"🗑️ 삭제 대상: {len(to_delete)}개 프로젝트")
    for proj in to_delete:
        print(f"   - 삭제 중: {proj['title']}...", end=" ")
        try:
            client.delete_notebook(proj['id'])
            print("[완료]")
        except Exception as e:
            print(f"[오류: {e}]")

    # [3] 추가할 신규 프로젝트 3개
    new_projects_info = [
        "부산 여행 가이드 및 코스 추천",
        "단체 소개팅 매칭 앱 (직장인/취미 기반)",
        "출퇴근 직장인을 위한 뉴스 정보 요약 앱"
    ]
    
    # 마지막 번호 확인 (Project 10까지 썼으므로 11부터 시작하면 좋겠지만, 
    # 그냥 깔끔하게 'New Project' 접두사를 쓰거나 번호를 이어감)
    
    print(f"\n✨ 신규 프로젝트 {len(new_projects_info)}개 생성 중...")
    
    new_created = []
    for i, title in enumerate(new_projects_info, 1):
        full_title = f"[New Project {i}] {title} (1인기업)"
        print(f">> 생성 중: '{full_title}'...", end=" ")
        try:
            notebook = client.create_notebook(title=full_title)
            
            if notebook:
                print(f"[성공] ID: {notebook.id}")
                new_created.append({"title": full_title, "id": notebook.id})
                
                # 가이드라인 추가
                guideline = f"""
# {full_title} 초기 가이드라인
- **목표:** 사용자 확보 및 수익화 모델 구축
- **핵심 전략:** 지역 특화/타겟 특화 + AI 추천 알고리즘
- **초기 할 일:** 콘텐츠 수집 및 MVP 앱 기획
                """
                client.add_text_source(notebook.id, guideline, "초기 가이드라인")
            else:
                print(f"[실패]")
        except Exception as e:
            print(f"[오류: {e}]")
            
    # 최종 리스트 저장 (유지된 것 + 새로 만든 것)
    final_list = kept_projects + new_created
    with open("updated_projects_final.json", "w", encoding="utf-8") as f:
        json.dump(final_list, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ 최종 업데이트 완료! 총 {len(final_list)}개 프로젝트가 유지/생성되었습니다.")

if __name__ == "__main__":
    modify_projects()
