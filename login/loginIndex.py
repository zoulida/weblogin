__author__ = 'zoulida'
# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class alert_is_present(object):
    """ Expect an alert to be present."""

    """判断当前页面的alert弹窗"""
    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except :
            return False

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
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
    driver.maximize_window()
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

def getPicture(driver, down = 0):
    print('down = ', down)
    # 截取验证码图片
    from PIL import Image
    picturename = 'hao123.png'
    #driver.save_screenshot(picturename)

    # 长截图没有成功，只能下划1200像素，然后再定位下移1200，1200只能是多次调试试的。
    #down = 1200
    # scriptString = 'window.scrollTo(0,%s);' %down
    # print(scriptString)
    driver.execute_script('window.scrollTo(0,%s);' % down)
    time.sleep(0.2)
    driver.save_screenshot(picturename)
    time.sleep(0.1)
    # screenshotAll(driver, picturename)

    element = driver.find_element_by_id("auth_code_img")
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y'] - down
    print('top: ', top)
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height'] - down
    print('bottom: ', bottom)

    im = Image.open(picturename)
    im = im.crop((left, top, right, bottom))
    im.save('888.png')
    #time.sleep(3)

def operationGetPicture(driver):
    sizeDict = driver.get_window_size()
    print(sizeDict)
    print('当前浏览器窗口的宽:', sizeDict['width'])
    print('当前浏览器窗口的高:', sizeDict['height'])

    element = driver.find_element_by_id("auth_code_img")
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    bottom = element.location['y'] + element.size['height']

    if bottom > sizeDict['height']:
        getPicture(driver, down=  sizeDict['height'])#bottom - sizeDict['height']
        #down 是多少可以根据，要下划几个屏幕决定。如果多就用取整再乘以屏幕的高度。
    else:
        getPicture(driver, down=0)



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
    #print(driver.current_url)
    time.sleep(1)

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
    elem.clear()
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
    result = '不发送到服务器'
    result = tujian.base64_api(uname='zoulida', pwd='zoulida', img=img)

    print(result)
    return result

def selectorOp(driver):
    # driver.find_element_by_xpath('//div[text()="省份"]').click()province_id
    #driver.find_element_by_id("province_id").click()
    # tags = driver.find_elements_by_xpath('//ul[@class="selector-box"]/li')
    # elem = driver.find_element_by_id("province_id")

    from selenium.webdriver.support.select import Select
    # 实例化一个Select类的对象
    selector = Select(driver.find_element_by_id("province_id"))

    # 下面三种方法用于选择"篮球运动员"
    # selector.select_by_index("2")  # 通过index进行选择,index从0开始
    selector.select_by_value("16")  # 通过value属性值进行选择
    # selector.select_by_visible_text("篮球运动员")  # 通过标签显示的text进行选择

    time.sleep(1)
    selector2 = Select(driver.find_element_by_id("city_id"))
    selector2.select_by_visible_text("济南市")

def submit(driver):

    #print(result)
    #time.sleep(3)
    selectorOp(driver)
    time.sleep(2)
    result = vcode(driver)

    elem = driver.find_element_by_id("verify")
    elem.clear()#这个会滚动屏幕
    elem.send_keys(result)
    # 提交表单
    driver.find_element_by_xpath("//*[@id='teacher_btn']").click()
    pass

def total(driver):

    flag = "还没开始登录呢"
    k = 10
    while(flag is not False and k > 0):
        login(driver)
        time.sleep(1)

        # 判断弹窗结果 交流QQ群: 232607095
        result = alert_is_present()(driver)
        if result:
            print('登录出错:', result.text)
            result.accept()
        else:
            print("login.html登录成功，alert 未弹出！")
        k = k - 1
        flag = result


    #url = 'http://bcfl.sdufe.edu.cn/Teacher/handle_person'
    #print(driver.current_url)
    #if (driver.getCurrentUrl().equals(url)):
    #    print('OKKKKK')

    #driver.find_element_by_link_text("每日打卡").click()
    driver.find_element_by_partial_link_text("每日打卡").click()
    #driver.get("http://bcfl.sdufe.edu.cn/teacher/handle_ext.html")
    time.sleep(1)

    flag = "还未提交"
    k = 10
    while (flag is not False and k > 0):
        submit(driver)
        time.sleep(1)
        # 判断弹窗结果 交流QQ群: 232607095
        result = alert_is_present()(driver)
        if result:
            print('登录出错:', result.text)
            result.accept()
        else:
            print("提交成功，alert 未弹出！")
        k = k - 1
        flag = result

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    #driver = openChrome()
    driver = debugChrome()#这个是调试浏览器
    #operationAuth(driver)
    #operationGetPicture(driver)
    #login(driver)
    total(driver)
    #driver.execute_script('window.scrollTo(0,1200);')
    #driver.execute_script('window.scrrollBy(0,400);')
    #submit(driver)
    #screenshotAll()
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\chrome_temp"