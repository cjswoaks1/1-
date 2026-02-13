import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def generate_pdf_sample_content():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 프로젝트 ID: [Global] 부산 여행 (773c4421...)
    notebook_id = "773c4421-0deb-40fe-8b3d-4e4277e7b69a"
    title = "[Sample PDF] 부산 1박2일 커플 코스"

    print(f"🚀 '{title}' PDF 콘텐츠 초안 생성 시작! (ID: {notebook_id})\n")

    # 3. NotebookLM에게 질문: 팔릴 만한 PDF 가이드북 내용 생성
    query = (
        "우리는 이제 앱이 아닌 **'PDF 가이드북'**을 만들어서 판매하려고 한다. "
        "당장 인쇄하거나 PDF로 저장해서 팔 수 있도록, 다음 내용을 포함한 **'부산 1박 2일 커플 인생샷 코스'** 가이드북 초안을 작성해줘:\n\n"
        "--- [가이드북 구성] ---\n"
        "1. **[표지]** 매력적인 제목과 부제 (예: 'The Only Guide You Need for Busan')\n"
        "   - 타겟: 인스타그램을 좋아하는 2030 글로벌 커플 (영어/한국어 병기 형태)\n"
        "2. **[Day 1: 바다와 노을]**\n"
        "   - 오전: 해운대 캡슐열차 (예약 꿀팁 포함)\n"
        "   - 점심: 현지인만 아는 오션뷰 돼지국밥집 (가상의 상호명 사용)\n"
        "   - 오후: 기장 힙플레이스 카페 (인생샷 포인트 설명)\n"
        "3. **[Day 2: 감성과 쇼핑]**\n"
        "   - 오전: 영도 흰여울문화마을 (포토스팟 3곳)\n"
        "   - 점심: 남포동 길거리 음식 투어 (필수 메뉴 3가지)\n"
        "   - 쇼핑: 국제시장 빈티지 & 기념품 샵\n"
        "4. **[Bonus]** 이 가이드북 구매자만을 위한 시크릿 혜택 (예: '우리가 만든 구글맵 리스트 링크 제공')\n"
        "-----------------------\n"
        "**[출력 형식]** 마크다운(Markdown)으로 작성해서, 내가 바로 PDF 변환기에 넣을 수 있게 해줘."
    )
    
    print(f"💡 질문 전송: \"야! 돈 받고 팔 수 있는 PDF 내용 짜와!\"")
    print("⏳ NotebookLM이 '베스트셀러 여행 작가' 모드로 빙의 중입니다... ✍️")

    try:
        # 쿼리 실행
        result = client.query(notebook_id, query)
        answer = result["answer"]
        
        print("\n" + "="*40)
        print(f"📢 [NotebookLM의 PDF 가이드북 초안]")
        print("="*40 + "\n")
        print(answer)
        
        # 파일 저장 (이게 바로 PDF 원고입니다)
        filename = "busan_couple_guide_draft.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(answer)
        print(f"\n✅ 가이드북 초안이 '{filename}' 파일로 저장되었습니다.")
        
        # 노트북 소스 추가
        client.add_text_source(notebook_id, answer, "📖 [판매용] 부산 커플 가이드북 초안")
        print("✅ 노트북 소스에도 추가 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    generate_pdf_sample_content()
