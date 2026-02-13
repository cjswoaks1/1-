from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient
import json

def create_projects():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 아이디어 생성 (Mock: 실제로는 research_projects_kr의 결과를 사용)
    # 일단은 앞서 나온 10가지 아이디어를 기반으로 10개의 '노트북'을 만든다고 가정
    project_ideas = [
        "AI 자동화 뉴스레터",
        "유튜브 쇼츠 자동화 채널",
        "노코드 앱 개발 서비스",
        "소셜 미디어 콘텐츠 대행",
        "온라인 강의 자동 판매",
        "AI 챗봇 개발 대행",
        "맞춤형 프롬프트 마켓플레이스",
        "자동화된 주식/코인 트레이딩 봇",
        "POD (Print on Demand) 스토어",
        "디지털 템플릿/전자책 판매"
    ]
    
    print(f"총 {len(project_ideas)}개의 1인 기업 프로젝트용 노트북을 생성합니다...")
    
    created_notebooks = []
    for i, title in enumerate(project_ideas, 1):
        full_title = f"[Project {i}] {title} (1인기업)"
        print(f"➡️ 생성 중: '{full_title}'...")
        notebook = client.create_notebook(title=full_title)
        
        if notebook:
            print(f"✅ 생성 완료! ID: {notebook.id}")
            created_notebooks.append({"title": full_title, "id": notebook.id})
            
            # (옵션) 각 노트북에 초기 가이드라인 소스 추가 (텍스트 소스)
            guideline = f"""
# {full_title} 가이드라인
- **목표:** 월 1,000만원 자동 수익
- **핵심 전략:** AI를 활용한 생산성 극대화 + 절세 전략
- **초기 할 일:** 시장 조사, MVP(최소 기능 제품) 제작
            """
            client.add_text_source(notebook.id, guideline, "초기 가이드라인")
            print("   └─ 가이드라인 소스 추가 완료")
        else:
            print(f"❌ 생성 실패: {full_title}")

    # 결과 저장
    with open("created_projects.json", "w", encoding="utf-8") as f:
        json.dump(created_notebooks, f, ensure_ascii=False, indent=2)
    print("\n🎉 모든 프로젝트 노트북 생성 완료!")

if __name__ == "__main__":
    create_projects()
