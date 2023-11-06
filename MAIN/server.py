import http.server
import socketserver
import os

PORT = 58541

# Define the directory where your HTML file and assets are located.
web_dir = os.path.join(os.path.dirname(__file__), 'main.html')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
