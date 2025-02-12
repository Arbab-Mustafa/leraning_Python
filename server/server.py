import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # ✅ Allows React to fetch
            self.end_headers()
            response = {"message": "Hello from Python backend!"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        pass
    def do_PUT(self):
        pass
       

    def do_OPTIONS(self):  # ✅ Handle CORS preflight
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()



          






if __name__ == "__main__":
    server_address = ("", 5000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Python Server running on port 5000...")
    httpd.serve_forever()
