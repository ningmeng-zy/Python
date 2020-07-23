from selenium import webdriver
import time
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('/002/0001/checkbox.html')
dr.get(file_path)# 选择页面上所有的input，然后从中过滤出所有的checkbox 并勾选之
dr.maximize_window()
#定位一组元素
inputs = dr.find_elements_by_tag_name('input')
time.sleep(3)
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
        time.sleep(2)
time.sleep(6)
dr.quit()