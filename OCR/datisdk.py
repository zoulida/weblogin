#coding=utf-8
from urllib3 import encode_multipart_formdata
import requests
import json
import base64

apiurl="https://api.laladama.com"

#以表单形式上传验证图片 
def uploadFile(filename,authcode, typeno, author, remark):
    """
        用法：uploadFile("D:\\88.jpg", "nEPGcKsXXgdx8qM9", "200103", "test", "")

        filename:图片文件绝对物理路径
        authcode:授权码
        typeno:题型
        author:开发者帐号
        remark:图片备注
        返回dict对象,判断['status']==0,则['msg']就是题号，否则是具体的错误信息
    """
    header={}
    data={"authcode":authcode,"typeno":typeno,"author":author,"remark":remark}
    try:
        data['imagefile']= (filename,open(filename,'rb').read())
    except:
        return {"status":-1,"msg":"打开图片出错"}
    else:
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        header['Content-Type'] = encode_data[1]
        try:
            r = requests.post(apiurl+"/member/uploadform", headers=header, data=data)
        except:
            return {"status":-1,"msg":"访问接口出错"}
        else:
            if r.status_code==200:
                return json.loads(r.content)
            else:
                return {"status":-1,"msg":"访问接口出错"}

#以表单形式上传验证码图片，图片经base64编码
def uploadBase64String(base64string, authcode, typeno, author, remark):
    """
        用法：uploadBase64String("data:image/jpeg;base64,............", "nEPGcKsXXgdx8qM9", "200103", "test", "")

        base64string:图片经过base64编码的字符串

            可参考以下方法转成base64编码，传给接口时必须加上前缀data:image/jpeg;base64,或data.image/gif;base64,或data.image/png;base64,
            jpg格式=>data:image/jpeg;base64,
            png格式=>data:image/png;base64,
            gif格式=>data:image/gif;base64,

            import base64
            with open("D:\\ww\\1.jpg", 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()

            print('data:image/jpeg;base64,%s'%s)

        authcode:授权码
        typeno:题型
        author:开发者帐号
        remark:图片备注
        返回dict对象,判断['status']==0,则['msg']就是题号，否则是具体的错误信息      
    """
    data={"base64string":base64string,"authcode":authcode,"typeno":typeno,"author":author,"remark":remark}
    try:
        r = requests.post(apiurl+"/member/uploadformbase64",data=data)
    except:
        return {"status":-1,"msg":"访问接口出错"}
    else:
        if r.status_code==200:
            return json.loads(r.content)
        else:
            return {"status":-1,"msg":"访问接口出错"}

#以application/json形式上传验证码图片，图片经base64编码
def uploadJson(base64string, authcode, typeno, author, remark):
    """
        用法：uploadJson("data:image/jpeg;base64,............", "nEPGcKsXXgdx8qM9", "200103", "test", "")

        base64string:图片经过base64编码的字符串

            可参考以下方法转成base64编码，传给接口时必须加上前缀data:image/jpeg;base64,或data.image/gif;base64,或data.image/png;base64,
            jpg格式=>data:image/jpeg;base64,
            png格式=>data:image/png;base64,
            gif格式=>data:image/gif;base64,
            
            import base64
            with open("D:\\ww\\1.jpg", 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()

            print('data:image/jpeg;base64,%s'%s)

        authcode:授权码
        typeno:题型
        author:开发者帐号
        remark:图片备注
        返回dict对象,判断['status']==0,则['msg']就是题号，否则是具体的错误信息      
    """
    data=json.dumps({"base64string":base64string,"authcode":authcode,"typeno":typeno,"author":author,"remark":remark})
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(apiurl+"/member/uploadjson",data=data,headers=headers)
    except:
        return {"status":-1,"msg":"访问接口出错"}
    else:
        if r.status_code==200:
            return json.loads(r.content)
        else:
            return {"status":-1,"msg":"访问接口出错"}

#以表单形式通过题号及授权码查询答案
def queryForm(authcode,subjectno):
    """
        用法：queryForm("nEPGcKsXXgdx8qM9", "2003")

        authcode:授权码
        subjectno:题号
        返回dict对象,判断['status']==0,则['msg']就是答案，否则就是错误或提示信息      
    """
    data={"authcode":authcode,"subjectno":subjectno}
    try:
        r = requests.post(apiurl+"/member/queryform",data=data)
    except:
        return {"status":-1,"msg":"访问接口出错"}
    else:
        if r.status_code==200:
            return json.loads(r.content)
        else:
            return {"status":-1,"msg":"访问接口出错"}

#以application/json形式通过题号及授权码查询答案
def queryJson(authcode,subjectno):
    """
        用法：queryJson("nEPGcKsXXgdx8qM9", "2003")

        authcode:授权码
        subjectno:题号
        返回dict对象,判断['status']==0,则['msg']就是答案，否则就是错误或提示信息      
    """
    data=json.dumps({"authcode":authcode,"subjectno":subjectno})
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(apiurl+"/member/queryjson",data=data,headers=headers)
    except:
        return {"status":-1,"msg":"访问接口出错"}
    else:
        if r.status_code==200:
            return json.loads(r.content)
        else:
            return {"status":-1,"msg":"访问接口出错"}

#提交答案错误反馈
def submitError(authcode,subjectno):
    """
        用法：submitError("nEPGcKsXXgdx8qM9", "2003")

        authcode:授权码
        subjectno:题号
        返回dict对象,判断['status']==0,则反馈成功，否则['msg']是错误或提示信息      
    """
    data={"authcode":authcode,"subjectno":subjectno}

    try:
        r = requests.post(apiurl+"/member/resultform",data=data)
    except:
        return {"status":-1,"msg":"访问接口出错"}
    else:
        if r.status_code==200:
            return json.loads(r.content)
        else:
            return {"status":-1,"msg":"访问接口出错"}

#以下为测试代码

#上传验证码图片
with open("D:\\88.png", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()

result=uploadJson('data:image/jpeg;base64,'+str(s), "vGpAl7zman8POWJc", "200103", "test", "请输入四个数字")
#result=uploadBase64String('data:image/jpeg;base64,'+str(s), "nEPGcKsXXgdx8qM9", "200103", "test", "")
print("status:"+str(result['status'])+",msg:"+result['msg'])
subjectno=""

#查询答案
if result['status']==0:
    #正式业务场景请隔一段时间再查询，查询时可以按具体情况以一定的频率查询答案
    subjectno=result['msg']
    result=queryJson("vGpAl7zman8POWJc",result['msg'])
    print("status:"+str(result['status'])+",msg:"+result['msg'])
#提交错误反馈
if result['status']==100:
    result=submitError("vGpAl7zman8POWJc",subjectno)
    print("status:"+str(result['status'])+",msg:"+result['msg'])

