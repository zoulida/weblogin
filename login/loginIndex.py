__author__ = 'zoulida'
# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# debug模式，不是从新开新的的chrome
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\chrome_temp"  这是cmd命令，提前手动打开
def debugChrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver

# 授权操作
def operationAuth(driver):
    url = "http://www.baidu.com"
    driver.get(url)
    # 找到输入框并输入查询内容
    elem = driver.find_element_by_id("kw")
    elem.send_keys("邹立达")
    # 提交表单
    driver.find_element_by_xpath("//*[@id='su']").click()

    print('查询操作完毕！')

def operationGetPictureStone(driver):
    url = "http://bcfl.sdufe.edu.cn/index/login.html"
    driver.get(url)
    time.sleep(5)

    # 截取验证码图片
    from PIL import Image
    driver.save_screenshot('bdbutton.png')

    element = driver.find_element_by_id("auth_code_img")
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    im = Image.open('bdbutton.png')
    im = im.crop((left, top, right, bottom))
    im.save('bdbutton.png')

    print('查询操作完毕！')

def operationGetPicture(driver):


    # 截取验证码图片
    from PIL import Image
    picturename = 'hao123.png'
    driver.save_screenshot(picturename)

    # 长截图没有成功，只能下划1200像素，然后再定位下移1200，1200只能是多次调试试的。
    down = 1200
    #scriptString = 'window.scrollTo(0,%s);' %down
    #print(scriptString)
    driver.execute_script('window.scrollTo(0,%s);' %down)
    #screenshotAll(driver, picturename)

    element = driver.find_element_by_id("auth_code_img")
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y'] - down
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height'] - down

    im = Image.open(picturename)
    im = im.crop((left, top, right, bottom))
    im.save('888.png')

def saveVcode(driver):#zuofei
    # 截取验证码图片
    from PIL import Image
    driver.save_screenshot('bdbutton.png')
    element = driver.find_element_by_xpath('//*[@id="nc_1_clickCaptcha"]/div[2]/img')  # 找到验证码图片
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    im = Image.open('bdbutton.png')
    im = im.crop((left, top, right, bottom))
    im.save('bdbutton.png')

def login(driver):
    url = "http://bcfl.sdufe.edu.cn/index/login.html"
    driver.get(url)
    time.sleep(3)

    # 找到输入框并输入查询内容
    elem = driver.find_element_by_id("number")
    elem.send_keys("20170279")

    elem = driver.find_element_by_id("card")
    elem.send_keys("113717")

    #elem = driver.find_element_by_id("verify") #login_type
    #elem.send_keys("dddd")

    # 查找所有name属性值为“fruit”的单选框元素对象，并存放在radioList列表中
    radioList = driver.find_elements_by_xpath("//input[@name='login_type']")
    '''
    循环遍历radioList中的每个单选按钮，查找value属性值为“orange”的单选框，
    如果找到此单选框以后，发现未处于选中状态，则调用click方法选中该选项。
    '''
    for radio in radioList:
        if radio.get_attribute("value") == "1":
            if not radio.is_selected():
                radio.click()
                #assertEqual(radio.get_attribute("value"), "1")

    #填写验证码
    result = vcode(driver)
    elem = driver.find_element_by_id("verify")
    elem.send_keys(result)


    # 提交表单
    driver.find_element_by_xpath("//*[@id='sub_btn']").click()

def screenshotAll(driver, picturename = 'hao123.png'):#作废
    from time import sleep
    from PIL import Image
    import numpy as np
    from selenium import webdriver

    #driver = webdriver.Chrome()
    driver.fullscreen_window()  # 全屏窗口
    #driver.get(url)#driver.get('https://www.qq.com/')
    window_height = driver.get_window_size()['height']  # 窗口高度

    page_height = driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度
    driver.save_screenshot('qq.png')

    if page_height > window_height:
        n = page_height // window_height  # 需要滚动的次数
        base_mat = np.atleast_2d(Image.open('qq.png'))  # 打开截图并转为二维矩阵

        for i in range(n):
            driver.execute_script(f'document.documentElement.scrollTop={window_height * (i + 1)};')
            sleep(.5)
            driver.save_screenshot(f'qq_{i}.png')  # 保存截图
            mat = np.atleast_2d(Image.open(f'qq_{i}.png'))  # 打开截图并转为二维矩阵
            base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
        Image.fromarray(base_mat).save(picturename)

    #driver.quit()

def vcode(driver):
    operationGetPicture(driver)

    #调用图鉴
    from PIL import Image
    import OCR.tujian as tujian
    img_path = "./888.png"
    img = Image.open(img_path)
    #result = tujian.base64_api(uname='zoulida0000', pwd='zoulida', img=img)
    result = '不发送到服务器'
    print(result)
    return result

def submit(driver):
    result = vcode(driver)
    print(result)


    pass

def total(driver):
    login(driver)
    time.sleep(3)

    #driver.find_element_by_link_text("每日打卡").click()
    driver.find_element_by_partial_link_text("每日打卡").click()
    #driver.get("http://bcfl.sdufe.edu.cn/teacher/handle_ext.html")
    submit(driver)

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    #driver = openChrome()
    driver = debugChrome()#这个是调试浏览器
    #operationAuth(driver)
    #operationGetPicture(driver)
    #login(driver)
    #total(driver)
    #driver.execute_script('window.scrollTo(0,1200);')
    #driver.execute_script('window.scrrollBy(0,400);')
    submit(driver)
    #screenshotAll()
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\chrome_temp"