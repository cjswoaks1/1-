import sys
import io
import json

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def create_projects():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. NotebookLM이 추천한 10가지 프로젝트 아이디어
    project_ideas = [
        "블루칼라 타겟 '부재중 전화' 방어 에이전시",
        "기업 내부용 '보안 특화' 지식 검색 봇 (B2B)",
        "부동산 '스피드 리드' 대응 시스템",
        "법률 및 의료 분야 '문서 초안 작성' 에이전트",
        "'바이브 코딩' 기반 마이크로 SaaS 개발",
        "콘텐츠 리퍼포징(Repurposing) 자동화 대행",
        "개인 브랜드 기반 AI 교육 및 커뮤니티",
        "이커머스 '장바구니 이탈 방지' CS 자동화",
        "1인 기업 맞춤형 세무/재무 대시보드 구축",
        "콜드 아웃리치(Cold Outreach) 자동화 시스템"
    ]
    
    print(f"총 {len(project_ideas)}개의 1인 기업 프로젝트용 노트북을 생성합니다...")
    
    created_notebooks = []
    for i, title in enumerate(project_ideas, 1):
        full_title = f"[Project {i}] {title} (1인기업)"
        print(f">> 생성 중: '{full_title}'...", end=" ") # 이모지 제거 및 줄바꿈 방지
        try:
            notebook = client.create_notebook(title=full_title)
            
            if notebook:
                print(f"[성공] ID: {notebook.id}")
                created_notebooks.append({"title": full_title, "id": notebook.id})
                
                # 각 노트북에 초기 가이드라인 소스 추가
                guideline = f"""
# {full_title} 초기 가이드라인
- **목표:** 월 $10,000 (약 1,300만원) 자동 수익 달성
- **핵심 전략:** AI 에이전트 자동화 + 니치(Niche) 시장 공략
- **초기 할 일:** 
    1. 타겟 고객(페르소나) 정의
    2. MVP(최소 기능 제품) 기획
    3. 세일즈 퍼널(Sales Funnel) 설계
                """
                client.add_text_source(notebook.id, guideline, "초기 가이드라인")
            else:
                print(f"[실패]")
        except Exception as e:
            print(f"[오류: {e}]")

    # 결과 저장
    with open("created_projects_final.json", "w", encoding="utf-8") as f:
        json.dump(created_notebooks, f, ensure_ascii=False, indent=2)
    print("\n🎉 모든 프로젝트 노트북 생성 완료! created_projects_final.json 파일을 확인하세요.")

if __name__ == "__main__":
    create_projects()
