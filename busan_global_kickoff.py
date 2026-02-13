import sys
import io
import json
import time

# 터미널 출력 인코딩 강제 설정 (UTF-8)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def kickstart_busan_global_project():
    # 1. 인증
    tokens = load_cached_tokens()
    if not tokens:
        print("❌ 인증 실패!")
        return
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)

    # 2. 프로젝트 ID: [New Project 1] 부산 여행 가이드 (773c4421...)
    notebook_id = "773c4421-0deb-40fe-8b3d-4e4277e7b69a"
    title = "[Global] 부산 여행 가이드 (Target: 인도네시아/대만)"

    print(f"🚀 '{title}' 글로벌 사업화 전략 수립! (ID: {notebook_id})\n")

    # 3. NotebookLM에게 글로벌 타겟팅 질문 + 핵심 전략 요구
    query = (
        "우리는 타겟을 '한국인'에서 **'인도네시아(무슬림 친화) 및 대만(미식/감성)' 관광객**으로 변경한다. "
        "다음 3가지 글로벌 핵심 전략을 구체적으로 제안해줘:\n\n"
        "1. [킬러 테마] 인도네시아(할랄, 기도실 등)와 대만(힙한 카페, 인생샷) 관광객이 각각 10달러($10)를 내고 살 만한 '맞춤형 테마 코스' 기획.\n"
        "2. [마케팅/채널] 이들에게 우리 가이드북(PDF/App)을 팔기 위해 어디에 홍보해야 하나? (예: 현지 커뮤니티, 여행사 제휴 등)\n"
        "3. [결제/언어] 1인 기업으로서 언어 장벽과 해외 결제(PayPal 등) 문제를 해결할 가장 쉬운 방법은?"
    )
    
    print(f"💡 질문 전송: \"인도네시아/대만 타겟 전략 내놔!\"")
    print("⏳ NotebookLM이 글로벌 트렌드를 분석 중입니다... (Global mode 🌏)")

    try:
        # 쿼리 실행
        result = client.query(notebook_id, query)
        answer = result["answer"]
        
        print("\n" + "="*40)
        print(f"📢 [NotebookLM의 글로벌 전략 보고]")
        print("="*40 + "\n")
        print(answer)
        
        # 파일 저장
        filename = "busan_global_strategy.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 🌏 [Global] 부산 여행 가이드 - 인도네시아 & 대만 타겟 전략\n\n{answer}")
        print(f"\n✅ 전략 보고서가 '{filename}' 파일로 저장되었습니다.")
        
        # 노트북 소스 추가
        client.add_text_source(notebook_id, answer, "🌏 글로벌 타겟 전략 (ID/TW)")
        print("✅ 노트북 소스에도 추가 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    kickstart_busan_global_project()
