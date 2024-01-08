from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello, world!</h1>")


def run_server():
    host = '127.0.0.1'
    port = 8000
    server_address = (host, port)

    httpd = TCPServer(server_address, MyHandler)

    print(f"Server listening on http://{host}:{port}...")
    httpd.serve_forever()

