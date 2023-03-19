#接收模块
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
 
 
class Resquest(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())
 
    def do_GET(self):
        print(self.requestline)
        if self.path != '/hello':
            self.send_error(404, "Page not Found!")
            return
 
        data = {
            'result_code': '1',
            'result_desc': 'Success',
            'timestamp': '',
            'data': {'message_id': '25d55ad283aa400af464c76d713c07ad'}
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
 
 
    def do_POST(self):
        print(self.headers)
        print(self.command)
        req_datas = self.rfile.read(int(self.headers['content-length'])) #重点在此步!
        print(req_datas.decode())
        data = {
            'result_code': '2',
            'result_desc': 'Success',
            'timestamp': '',
            'data': {'message_id': '25d55ad283aa400af464c76d713c07ad'}
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
 
 
if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, Resquest)
    print("监听%s端口" % host[1])
    server.serve_forever()