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
    time.sleep(5)

    # 找到输入框并输入查询内容
    elem = driver.find_element_by_id("number")
    elem.send_keys("20170279")

    elem = driver.find_element_by_id("card")
    elem.send_keys("113717")

    elem = driver.find_element_by_id("verify") #login_type
    elem.send_keys("dddd")


    # 提交表单
    driver.find_element_by_xpath("//*[@id='sub_btn']").click()


def debugChrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.find_element_by_id('kw').send_keys('哈哈哈哈')
    driver.find_element_by_xpath("//*[@id='su']").click()

def screenAllshot():
    from time import sleep
    from PIL import Image
    import numpy as np
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.fullscreen_window()  # 全屏窗口
    driver.get('https://www.qq.com/')
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
        Image.fromarray(base_mat).save('hao123.png')

    driver.quit()

def test2():
    from selenium import webdriver

    br = webdriver.PhantomJS()
    br.maximize_window()
    br.get("https://www.cnblogs.com/Jack-cx/p/9383990.html")

    br.save_screenshot("app1.png")

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    #driver = openChrome()
    #debugChrome()
    #operationAuth(driver)
    #operationGetPicture(driver)
    #login(driver)
    #screenAllshot()
    test2()
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\chrome_temp"