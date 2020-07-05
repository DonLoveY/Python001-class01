from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()  # 呼起Chrome浏览器
browser.implicitly_wait(3)
browser.maximize_window()
browser.get('https://shimo.im')
# # 一行代码完成
# WebDriverWait(browser,10).until(lambda browser:browser.find_element_by_id("kw")).send_keys("pytest")
# # 定义方法完成
# def kw(driver,times,func):
# 	return WebDriverWait(driver,times).until(func)
#
# kw(browser,10,lambda x:x.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')).send_keys("selenium")

class tc():
    # def __init__(self):
    #     pass

    def test(self):
        try:

            # 需要安装chrome driver, 和浏览器版本保持一致
            # http://chromedriver.storage.googleapis.com/index.html


            time.sleep(1)

            #browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])  # 切换到“密码登录”frame
            btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')  # 定位到“登录”按钮
            btm1.click()

            #time.sleep(2)
            username = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('15055495@qq.com')
            #time.sleep(2)
            #newusern = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('1111111111111111')
            #time.sleep(2)
            browser.execute_script("alert('输入框标红了!')")
            browser.switch_to.alert.accept()

            #username1=self.wait.until(EC.presence_of_element_located((By.NAME,'mobileOrEmail')))

            print(browser.current_url)
            #self.ttt(browser.current_url)
            #WebElement ele = browser.findElement(By.xpath("element_xpath"))
            #email = self.wait.until(EC.persence_of_element_located((By.XPATH.ID, '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')))
            #time.sleep(2)
            print('54username',username)
            # while not username:
            #     username = browser.find_element_by_xpath(
            #         '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(
            #         '1111111111111111')
            #     time.sleep(5)
            #print(newusern)
            print(username)
            #print(email)
            #time.sleep(2000)
            if(username != None):
                print("----------------------------")

            #browser.find_element_by_id('password').send_keys('test123test456')
            password = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]').send_keys("testtesttest")
            print('password===',password)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
            time.sleep(5)
            cookies = browser.get_cookies()  # 获取cookies
            print(cookies)
            time.sleep(3)

        except Exception as e:
            print(e)
        finally:
            browser.close()

    # 鼠标悬停
    def hover(self,by,value):
          element = self.findElement(by,value)
          #ActionChains(self.driver).move_to_element(element).perform()

    # 通过不同的方式查找界面元素
    def findElement(self,by,value):
          if(by == "id"):
                element = self.driver.find_element_by_id(value)
                return element
          elif(by == "name"):
                 element = self.driver.find_element_by_name(value)
                 return element
          elif(by == "xpath"):
                 element = self.driver.find_element_by_xpath(value)
                 return element
          elif(by == "classname"):
                 element = self.driver.find_element_by_class_name(value)
                 return element
          elif(by == "css"):
                 element = self.driver.find_element_by_css_selector(value)
                 return element
          elif(by == "link_text"):
                 element = self.driver.find_element_by_link_text(value)
                 return element
          else:
                 print("无对应方法，请检查")
                 return None


    def ttt(self,url):
        browser = webdriver.Chrome()
        response = browser.get(url)
        login_button_xpath = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input'
        print(login_button_xpath)
        print(time.time())
        # 每1秒扫描一次，直到60秒超时后，停止
        a = WebDriverWait(browser, 60, 1).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))
        print(a)
        login_button = browser.find_element_by_xpath(login_button_xpath)
        print("-----------------------")
        login_button.send_keys("1112121212")
        print(login_button)
        print(time.time())
        login_button.click()


if __name__ == "__main__":
    t = tc()
    t.test()