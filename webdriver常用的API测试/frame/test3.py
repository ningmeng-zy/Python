from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('E:/Pythoncode/002/0003/frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
#从默认页面调到frame1，不能没有这一步直接跳到frame2
driver.switch_to.frame("f1")
#从frame1里找frame2
#因为frame2包含在frame1页面
#从默认页面调到frame2
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("任嘉伦")
driver.find_element_by_id("su").click()
time.sleep(3)

#点击click
#1.从现在的frame2界面跳转会默认页面
#2.在从默认页面跳转到frame1页面
#因为frame1页面包含在默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(6)
driver.quit()