import http.server
import socketserver

PORT = 8000  # 服务器监听的端口号
DIRECTORY = './savesave'  # 文件保存的目录

class FileUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)  # 读取POST请求中的数据
        if self.path == '/upload':  # 如果请求的路径为/upload
            file_len = int(self.headers['Content-Length'])  # 获取上传文件的大小
            file_data = self.rfile.read(file_len)  # 读取上传文件的内容
            with open(DIRECTORY + '/uploaded_file', 'wb') as f:
                f.write(file_data)  # 将上传文件保存到本地
            self.send_response(200)  # 返回200表示上传成功
            self.end_headers()
        elif self.path == '/message':  # 如果请求的路径为/message
            message = post_data.decode('utf-8')  # 将POST请求中的数据解码为字符串
            print('Received message:', message)  # 输出接收到的消息
            self.send_response(200)  # 返回200表示接收成功
            self.end_headers()
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.TCPServer(("", PORT), FileUploadHandler)  # 创建服务器
print("Server running on port", PORT)
httpd.serve_forever()  # 启动服务器