import http.server
import socketserver
import json
from urllib.parse import parse_qs
from datetime import datetime

PORT = 58541
DATA_FILE = 'chat_data.json'

class ChatHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit-form':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            chat_data = parse_qs(post_data)['chat'][0]

            # Get the IP address
            ip_address = self.client_address[0]
            # Get the current time
            timestamp = datetime.now().isoformat()

            try:
                with open(DATA_FILE, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            # Append new chat message with IP and timestamp
            data.append({
                'chat': chat_data,
                'ip': ip_address,
                'time': timestamp
            })
            
            with open(DATA_FILE, 'w') as file:
                json.dump(data, file)

            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            super().do_POST()

# Initialize and start the server
httpd = socketserver.TCPServer(("", PORT), ChatHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
