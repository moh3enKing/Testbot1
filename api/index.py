from http.server import BaseHTTPRequestHandler
import sys

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print("📥 پیام دریافتی از تلگرام:", body.decode('utf-8'), file=sys.stderr)

        self.send_response(200)
        self.end_headers()
        self.wfile.write("✅ پیام دریافت شد".encode())
