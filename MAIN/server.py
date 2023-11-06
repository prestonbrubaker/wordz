import http.server
import socketserver

PORT = 58541
Handler = http.server.SimpleHTTPRequestHandler

# The Handler will automatically serve files from the current directory.
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
