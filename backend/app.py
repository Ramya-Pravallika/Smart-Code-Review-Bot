from flask import Flask, request, jsonify
from github.webhook_listener import handle_github_event

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def github_webhook():
    event = request.headers.get('X-GitHub-Event')
    payload = request.json
    result = handle_github_event(event, payload)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)