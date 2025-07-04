import json
import requests
from http.server import BaseHTTPRequestHandler

TOKEN = "8089258024:AAFx2ieX_ii_TrI60wNRRY7VaLHEdD3-BP0"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        chat_id = data["message"]["chat"]["id"]
        text = "سلام بر تو محسن‌جان! 🤖"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        requests.post(url, json=payload)

        self.send_response(200)
        self.end_headers()
