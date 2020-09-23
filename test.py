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

def operationGetPicture(driver):
    url = "http://bcfl.sdufe.edu.cn/index/login.html"
    driver.get(url)
    time.sleep(3)

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

def saveVcode():#zuofei
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


# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    #operationAuth(driver)
    operationGetPicture(driver)
