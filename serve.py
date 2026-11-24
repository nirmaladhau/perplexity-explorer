#!/usr/bin/env python3
import http.server
import socketserver
import pathlib

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # allow CORS for local testing of model CDN fetches
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Change working directory to the folder containing this script (project root)
project_root = pathlib.Path(__file__).parent
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
print(f"Serving at http://localhost:{PORT}/")
httpd.serve_forever()
