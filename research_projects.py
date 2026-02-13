from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient
import sys

def research_ideas():
    tokens = load_cached_tokens()
    if not tokens:
        print("Auth failed")
        return

    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)
    
    # Target Notebook: Mastering Solopreneurship...
    # ID from previous list: 9c435a6e-ad6d-45da-8f01-bd36c271a7b5
    notebook_id = "9c435a6e-ad6d-45da-8f01-bd36c271a7b5"
    
    query = (
        "Based on the strategies in this notebook, list 10 specific, high-revenue project ideas "
        "for a one-person business (Solopreneur). Focus on leveraging AI, automation, and "
        "strategic tax planning to maximize profit. For each idea, briefly explain the revenue model."
    )
    
    print(f"Querying Notebook ID: {notebook_id}...")
    try:
        result = client.query(notebook_id, query)
        print("\n--- NotebookLM Answer ---")
        print(result["answer"])
        print("-------------------------")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    research_ideas()
