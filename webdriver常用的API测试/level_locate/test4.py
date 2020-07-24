from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("E:/Pythoncode/002/0004/level_locate.html")
driver.get(file_path)
#点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text("Link1").click()
#将鼠标移动到Actionn元素的位置
action = driver.find_element_by_link_text("Action")
ActionChains(driver).move_to_element(action).perform()
time.sleep(10)