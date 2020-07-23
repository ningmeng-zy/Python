
# from selenium import webdriver
# #引入keys包
# from selenium.webdriver.common.keys import Keys
# import os,time
# driver = webdriver.Chrome()
# driver.get("http://demo.zentao.net/user-login-LW==.html")
# time.sleep(3)
# driver.maximize_window()
# driver.find_element_by_id("account").clear()
# time.sleep(3)
# driver.find_element_by_id("account").send_keys("demo")
# time.sleep(3)
# #tab的定位相当于清除了密码框的默认提示信息，等同上面的clear()
# driver.find_element_by_id("account").send_keys(Keys.TAB)
# time.sleep(3)
# #通过定位密码框，enter(回车)来代替登陆按钮
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
# time.sleep(3)
# driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
drive = webdriver.Chrome()
drive.get("https://www.baidu.com/")
drive.find_element_by_id("kw").send_keys("任嘉伦")
su1 = drive.find_element_by_id("su")
time.sleep(3)
#右击
ActionChains(drive).context_click(su1).perform()
time.sleep(3)
#双击
ActionChains(drive).double_click(su1).perform()
time.sleep(3)
title = drive.find_element_by_id("su")
target = drive.find_element_by_link_text("任嘉伦_百度百科")
#拖动
ActionChains(drive).drag_and_drop(title,target).perform()
#移动
ActionChains(drive).move_to_element(target).perform()
time.sleep(6)
# #ctrl+a全选输入框的内容
# drive.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# time.sleep(3)
# #ctrl+x剪切输入框的内容
# drive.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# time.sleep(3)
drive.quit()
# #将页面滚动条拖住底部
# js = "var q=document.documentElement.scrollTop=100000"
# drive.execute_script(js)
# time.sleep(3)
# #将页面滚动条拖住顶部
# js = "var q=document.documentElement.scrollTop=0"
# drive.execute_script(js)
# time.sleep(3)
# #同时控制浏览器的左右，上下
# js = "window.scrollTo(200,200)"
# drive.execute_script(js)
# time.sleep(3)
# drive.quit()
# driver = webdriver.Chrome()
# #访问百度页面
# driver.get("https://www.baidu.com/")
# time.sleep(6)
# #访问地图页面
# driver.get("https://map.baidu.com/")
# time.sleep(6)
# #后退到百度页面
# driver.back()
# time.sleep(6)
# #前进到地图页面
# driver.forward()
# time.sleep(6)
# driver.quit()




# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.set_window_size(400,800)
#driver.maximize_window()
# print(driver.title) #把页面的title打印出来
# print(driver.current_url)  #把页面的URL打印出来
#智能等待20秒
#driver.implicitly_wait(20)
# driver.maximize_window()
# time.sleep(2)
# data = driver.find_element_by_link_text("新闻").text
# print(data)
# time.sleep(6)
#通过id定义到百度输入框，并搜索任嘉伦
# driver.find_element_by_id("kw").send_keys("任嘉伦")
# driver.find_element_by_id("su").submit()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
#通过name定义到百度输入框，并搜索肖战
# driver.find_element_by_name("wd").send_keys("肖战")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# 通过tag_name定义到百度输入框，并搜索王一博，但是不能成功定义到百度搜索框
# driver.find_element_by_tag_name("input").send_keys("王一博")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# 通过class_name定义到百度输入框，并搜索王一博
# driver.find_element_by_class_name("s_ipt").send_keys("王一博")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# 通过css定义到百度输入框，并搜索万茜
# driver.find_element_by_css_selector("#kw").send_keys("万茜")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# 通过xpath定义到百度输入框，并搜索宋亚轩
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("宋亚轩")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# 通过link_text定义到hao123网站
# driver.find_element_by_link_text("hao123").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# 通过partial_link_text定义到hao123网站
# driver.find_element_by_partial_link_text("hao").click()
# time.sleep(6)
# driver.find_element_by_id("kw").clear()

#driver.quit()
# driver.find_element_by_id("kw").clear()
# time.sleep(3)
# driver.find_element_by_id("kw").send_keys("肖战")
# driver.find_element_by_id("su").submit()
# time.sleep(8)
