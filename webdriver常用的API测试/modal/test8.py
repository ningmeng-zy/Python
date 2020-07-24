from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("E:/Pythoncode/002/0008/modal.html")
driver.get(file_path)
driver.maximize_window()
#点击click
driver.find_element_by_id("show_modal").click()
time.sleep(5)
#点击click me
ddiv = driver.find_element_by_class_name("modal-body")
ddiv.find_element_by_id("click").click()
time.sleep(5)
#关闭alert
# div2 = driver.find_element_by_class_name("modal-footer")
# buttons = div2.find_element_by_tag_name("button")
# buttons[0].click()
div2 = driver.find_element_by_class_name("modal-foooter")
div2.find_element_by_class_name("btn").click()
time.sleep(5)

time.sleep(5)
driver.quit()