from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("E:/Pythoncode/002/0007/send.html")
driver.get(file_path)
driver.maximize_window()
# 定位点击按钮
driver.find_element_by_tag_name("input").click()
time.sleep(6)
# 得到操作alert的句柄
alert = driver.switch_to.alert
# 给弹出框输入的内容
alert.send_keys("hello,lemon")
time.sleep(6)
# 关闭弹框
alert.accept()
time.sleep(6)
driver.quit()
