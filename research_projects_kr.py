from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient
import sys

def research_ideas():
    print("[1] 인증 정보(쿠키) 로드 중...")
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패! 먼저 로그인을 해주세요.")
        return

    print("[2] NotebookLM 클라이언트 연결 중...")
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)
    
    # Target Notebook ID: Mastering Solopreneurship...
    notebook_id = "9c435a6e-ad6d-45da-8f01-bd36c271a7b5"
    
    # 쿼리 작성 (한국어로 요청)
    query = (
        "이 노트북에 담긴 전략(AI 자동화, 절세 등)을 바탕으로, "
        "1인 기업(솔로프리너)으로서 '수익을 극대화'할 수 있는 구체적인 프로젝트 아이디어 10가지를 제안해줘. "
        "각 아이디어마다 수익 모델(어떻게 돈을 버는지)과 핵심 전략(어떻게 자동화하는지)을 간단히 설명해줘."
    )
    
    print(f"[3] NotebookLM에 다음 질문을 전송합니다:\n    ➡️ \"{query}\"")
    print("\n[4] 잠시만 기다려주세요... (NotebookLM이 생각 중입니다 🧠)")
    
    try:
        result = client.query(notebook_id, query)
        print("\n=== [NotebookLM의 답변] ===")
        print(result["answer"])
        print("===========================")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    research_ideas()
