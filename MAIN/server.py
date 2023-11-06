import http.server
import socketserver
import json
from urllib.parse import parse_qs

PORT = 58541
DATA_FILE = 'chat_data.json'

class ChatHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Check if the path is correct
        if self.path == '/submit-form':
            # Get the length of the data and read it
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            chat_data = parse_qs(post_data)['chat'][0]

            # Load existing chat data
            try:
                with open(DATA_FILE, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            # Append new chat message
            data.append({'chat': chat_data})
            
            # Save back to the file
            with open(DATA_FILE, 'w') as file:
                json.dump(data, file)

            # Redirect back to the main page
            self.send_response(303)  # Redirect with See Other response
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # Default to the superclass method if the path is not the one we handle
            super().do_POST()

# Initialize and start the server
httpd = socketserver.TCPServer(("", PORT), ChatHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
