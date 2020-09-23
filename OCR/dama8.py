__author__ = 'zoulida'

import requests

url = "http://dama.a4a.cn/api/upload"
data = {
        "username":"zoulida",
        "password":"zoulida"
}
files = {"file":("bdbutton.png",open("./bdbutton.png","rb"),"image/gif")}
r = requests.post(url,files=files,data=data)
print (r.text)