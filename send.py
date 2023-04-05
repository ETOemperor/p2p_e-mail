#发送模块
import requests
import sys
ip="http://"+sys.argv[1]
if sys.argv[2]=="-m": #发送消息
    message=sys.argv[3]
    #发送post请求
    ret=requests.post(ip,data=message)
elif sys.argv[2]=="-f": #发送文件
    with open(sys.argv[3], 'rb') as f:
        sfile = {'file': (sys.argv[3], f)}  # 构建文件数据
        ret = requests.post(ip, files=sfile)  # 发送POST请求
else:
    print("!!!指令错误!!!")
    sys.exit()
print("http状态码:"+str(ret)+"\n发送完成")