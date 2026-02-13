import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def kickstart_busan_project():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 프로젝트 ID 찾기 (부산 여행)
    # Json 파일이 깨져보이거나 인코딩 문제가 있을 수 있으므로 ID를 직접 지정하거나 검색
    # 앞선 출력에서 확인된 부산 여행 프로젝트 ID: 773c4421-0deb-40fe-8b3d-4e4277e7b69a
    notebook_id = "773c4421-0deb-40fe-8b3d-4e4277e7b69a"
    title = "[New Project 1] 부산 여행 가이드 및 코스 추천"
    
    print(f"🚀 '{title}' 사업화 시작합니다! (ID: {notebook_id})\n")

    # 3. NotebookLM에게 실전 과제 부여
    query = (
        "우리는 지금 당장 이 부산 여행 가이드 사업을 시작한다. "
        "기존에 작성된 '실행 계획서'를 바탕으로, 다음 3가지 핵심 자료를 구체적으로 작성해줘:\n\n"
        "1. [킬러 테마 3선] 2030 MZ세대(커플/혼행족)가 5,900원을 내고서라도 사고 싶은 '초개인화 여행 테마' 3가지.\n"
        "   (예: 'MBTI I형을 위한 노포 혼밥 코스', '인스타 인생샷 보장 오션뷰 카페 투어' 등)\n"
        "2. [랜딩 페이지 카피] 고객의 지갑을 열게 할 강렬한 헤드라인(Headline)과 서브 카피.\n"
        "3. [CEO 일주일 미션] 대표님이 당장 내일부터 일주일간 실행해야 할 구체적인 행동 리스트 (D-1 ~ D-7)."
    )
    
    print(f"💡 질문 전송: \"{query}\"")
    print("⏳ NotebookLM이 부산 핫플을 스캔 중입니다... 잠시만요!")

    try:
        # 쿼리 실행
        result = client.query(notebook_id, query)
        answer = result["answer"]
        
        print("\n" + "="*40)
        print(f"📢 [NotebookLM의 사업화 전략 보고]")
        print("="*40 + "\n")
        print(answer)
        
        # 결과를 파일로 저장 (대표님이 나중에 보기 편하게)
        filename = "busan_travel_kickoff.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 🌊 부산 여행 프로젝트 사업화 전략\n\n{answer}")
        print(f"\n✅ 전략 보고서가 '{filename}' 파일로 저장되었습니다.")
        
        # (선택) 결과를 노트북 소스로도 추가
        client.add_text_source(notebook_id, answer, "🚀 사업화 킥오프 전략")
        print("✅ 노트북 소스에도 추가 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    kickstart_busan_project()
