#发送模块
import requests
import sys
ip="http://"+sys.argv[1]
if sys.argv[2]=="-m":
    message=sys.argv[3]
elif sys.argv[2]=="-f":
    message=open(sys.argv[3]).read()
else:
    print("!!!指令错误!!!")
    sys.exit()

#发送post请求
ret=requests.post(ip,data=message)
print("http状态码："+str(ret)+"\n发送完成")