import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def generate_gumroad_sales_copy():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 프로젝트 ID: [Global] 부산 여행 (773c4421...)
    notebook_id = "773c4421-0deb-40fe-8b3d-4e4277e7b69a"
    title = "[Sales Page] Gumroad 판매 카피라이팅"

    print(f"🚀 '{title}' 생성 시작! (ID: {notebook_id})\n")

    # 3. NotebookLM에게 질문: 팔리는 상세페이지(Sales Copy) 작성
    query = (
        "우리는 이제 '부산 1박 2일 커플 가이드북(PDF)'을 Gumroad에서 판매한다. "
        "고객(외국인 커플)이 페이지를 보자마자 '어머, 이건 사야 해!' 하고 결제 버튼을 누르게 만들 **'세일즈 카피(Sales Copy)'**를 작성해줘.\n\n"
        "--- [필수 포함 항목] ---\n"
        "1. **[Headline]** 3초 만에 시선을 사로잡는 강력한 제목 (영어)\n"
        "2. **[Pain Point]** '블로그 검색하느라 시간 낭비하지 마세요' 같은 그들의 고충 건드리기\n"
        "3. **[Solution]** 우리 가이드북이 주는 혜택 (현지인 꿀팁, 인생샷 보장, 시간 절약)\n"
        "4. **[Bonus]** '지금 사면 구글맵 리스트 무료 증정' 강조\n"
        "5. **[Price Anchor]** '커피 한 잔 값($5)으로 완벽한 여행을 선물하세요' (가치 제안)\n"
        "-----------------------\n"
        "**[형식]** 바로 복사해서 Gumroad 상품 설명란에 붙여넣을 수 있게 영어로 작성해줘."
    )
    
    print(f"💡 질문 전송: \"야! 잘 팔리는 판매글 써와!\"")
    print("⏳ NotebookLM이 '100% 완판' 마케터로 빙의 중입니다... 💰")

    try:
        # 쿼리 실행
        result = client.query(notebook_id, query)
        answer = result["answer"]
        
        print("\n" + "="*40)
        print(f"📢 [NotebookLM의 판매 카피라이팅]")
        print("="*40 + "\n")
        print(answer)
        
        # 파일 저장
        filename = "gumroad_sales_copy.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(answer)
        print(f"\n✅ 판매 카피가 '{filename}' 파일로 저장되었습니다.")
        
        # 노트북 소스 추가
        client.add_text_source(notebook_id, answer, "Marketing Copy for Gumroad")
        print("✅ 노트북 소스에도 추가 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    generate_gumroad_sales_copy()
