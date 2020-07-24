from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("E:/Pythoncode/002/0006/alert.html")
driver.get(file_path)
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id("tooltip").click()
time.sleep(6)
# 得到操作弹出框的句柄
alert = driver.switch_to.alert
print("text: "+alert.text)
alert.accept()
time.sleep(6)