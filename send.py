#发送模块
import requests
import sys
ip="http://"+sys.argv[1]
if sys.argv[2]=="-m": #发送消息
    message=sys.argv[3]
elif sys.argv[2]=="-f": #发送文件
    message=message=str(open(sys.argv[3],mode="rb").read()) #二进制读文件
    #获取文件名
    file_name=sys.argv[3].split("/")
    file_name=file_name[::-1]
    file_name=file_name[0]
    message="file!"+file_name+"!"+str(message) #声明消息类型
else:
    print("!!!指令错误!!!")
    sys.exit()

#发送post请求
ret=requests.post(ip,data=message).close()
print("http状态码:"+str(ret)+"\n发送完成")