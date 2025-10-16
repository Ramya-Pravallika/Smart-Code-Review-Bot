from github.pr_fetcher import fetch_pr_code
from analyzers.python_analyzer import analyze_python_code
from ai.openai_review import get_ai_feedback
from github.commenter import post_comment

def handle_github_event(event, payload):
    if event == "pull_request" and payload['action'] in ["opened", "synchronize"]:
        pr_url = payload['pull_request']['url']
        code_files = fetch_pr_code(pr_url)
        static_results = []
        ai_results = []
        for file in code_files:
            if file.endswith('.py'):
                static_results += analyze_python_code(file)
            # Add more language checks here
            ai_results += get_ai_feedback(file)
        # Compose comment
        comment_body = f"Static Analysis:\n{static_results}\nAI Review:\n{ai_results}"
        post_comment(pr_url, comment_body)
        return {"status": "review posted"}
    return {"status": "ignored"}