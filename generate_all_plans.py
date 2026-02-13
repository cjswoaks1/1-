import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def generate_plans_for_all_projects():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 업데이트된 프로젝트 목록 로드
    try:
        with open("updated_projects_final.json", "r", encoding="utf-8") as f:
            projects = json.load(f)
    except FileNotFoundError:
        try:
             # 파일명이 다를 수 있으니 이전에 생성한 파일도 체크
            with open("created_projects_final.json", "r", encoding="utf-8") as f:
                projects = json.load(f)
        except:
             print("❌ 프로젝트 목록 파일을 찾을 수 없습니다.")
             return

    print(f"총 {len(projects)}개의 프로젝트에 대해 '상세 실행 계획'을 생성합니다...\n")

    report_results = []
    
    # 3. 각 프로젝트별로 질문 던져서 계획 생성
    # 공통 질문 템플릿 (수정 가능)
    query_template = (
        "이 프로젝트를 성공시키기 위한 '초구체적 실행 계획'을 짜줘. "
        "다음 3가지 항목을 필수 포함해서 작성해:\n"
        "1. [수익 모델] 구체적으로 누구에게 얼마를 받고 팔 것인가? (Pricing 전략)\n"
        "2. [마케팅/영업] 초기 고객 10명을 어떻게 모을 것인가? (Cold Email, SNS 등)\n"
        "3. [자동화] 1인 기업으로서 운영 리소스를 최소화할 자동화 툴과 워크플로우는?"
    )

    for i, proj in enumerate(projects, 1):
        notebook_id = proj['id']
        title = proj['title']
        
        print(f"[{i}/{len(projects)}] '{title}' 계획 수립 중...", end=" ")
        
        try:
            # 쿼리 실행
            result = client.query(notebook_id, query_template)
            answer = result["answer"]
            
            # 답변을 해당 노트북에 '소스'로 저장 (중요! 대표님이 검사할 때 볼 수 있게)
            # 답변 내용을 텍스트 파일 소스로 추가
            source_title = f"🚀 {title} - 실행 계획서"
            client.add_text_source(notebook_id, answer, source_title)
            
            print("[완료] 소스 추가됨 📄")
            
            report_results.append({
                "project": title,
                "plan": answer
            })
            
            # API 과부하 방지용 짧은 대기
            time.sleep(2)
            
        except Exception as e:
            print(f"[실패: {e}]")

    # (선택) 전체 결과를 하나의 리포트 파일로도 저장 (백업용)
    with open("all_projects_execution_plan.md", "w", encoding="utf-8") as f:
        f.write("# 💼 1인 기업 10대 프로젝트 실행 계획 통합본\n\n")
        for item in report_results:
            f.write(f"## {item['project']}\n\n")
            f.write(f"{item['plan']}\n\n")
            f.write(f"---\n\n")
            
    print("\n✅ 모든 프로젝트 계획 수립 및 노트북 저장 완료! (all_projects_execution_plan.md 생성됨)")

if __name__ == "__main__":
    generate_plans_for_all_projects()
