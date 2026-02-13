import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def expand_to_pan_islamic_market():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 프로젝트 ID: [Global] 부산 여행 (773c4421...)
    notebook_id = "773c4421-0deb-40fe-8b3d-4e4277e7b69a"
    title = "[Pan-Islamic] 부산 무슬림 투어 (파키스탄/인도/중동)"

    print(f"🚀 '{title}' 시장 확장 전략 수립! (ID: {notebook_id})\n")

    # 3. NotebookLM에게 질문: 무슬림 전체 시장 공략
    # 핵심은 '국가별 미묘한 차이(파키스탄 vs 인도 무슬림 vs 중동 아랍)와 공통점(할랄, 기도)'을 어떻게 아우를 것인가?
    query = (
        "우리는 '인도네시아/대만'에서 더 나아가 **'파키스탄, 인도(무슬림), 중동(아랍)'**까지 타겟을 대폭 확장한다. "
        "이 거대한 '범(Pan) 무슬림 시장'을 안방처럼 드나들기 위한 3가지 초격차 전략을 달라:\n\n"
        "1. [통합 킬러 콘텐츠] 파키스탄, 인도, 아랍 관광객 모두가 공통적으로 엄지 척(👍) 할 수밖에 없는 '부산 필수 코스'는? (예: 바다 + 할랄 + 쇼핑)\n"
        "2. [국가별 디테일] 파키스탄/인도 관광객(가성비, 가족 중심?)과 중동 오일머니 관광객(럭셔리, 의료 관광?)의 니즈 차이를 어떻게 한 큐에 해결하나?\n"
        "3. [마케팅/커뮤니티] 이들이 모여 있는 온라인 집결지(Facebook 그룹, WhatsApp 단톡방 등)를 어떻게 뚫고 들어가서 바이럴을 일으킬 것인가?"
    )
    
    print(f"💡 질문 전송: \"야! 파키스탄, 인도, 중동 다 내놔!\"")
    print("⏳ NotebookLM이 코란과 론리플래닛을 동시에 정독 중입니다... Use your imagination! 🕌")

    try:
        # 쿼리 실행
        result = client.query(notebook_id, query)
        answer = result["answer"]
        
        print("\n" + "="*40)
        print(f"📢 [NotebookLM의 범(Pan) 무슬림 정복 전략]")
        print("="*40 + "\n")
        print(answer)
        
        # 파일 저장
        filename = "busan_pan_islamic_strategy.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 🕌 부산 여행 - 파키스탄/인도/중동 타겟 확장 전략\n\n{answer}")
        print(f"\n✅ 전략 보고서가 '{filename}' 파일로 저장되었습니다.")
        
        # 노트북 소스 추가
        client.add_text_source(notebook_id, answer, "🕌 범 무슬림 시장 확장 전략")
        print("✅ 노트북 소스에도 추가 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    expand_to_pan_islamic_market()
