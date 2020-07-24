from selenium import webdriver
import os,time
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("E:/Pythoncode/002/0005/drop_down.html")
driver.get(file_path)
#1.xpath定位
driver.find_element_by_xpath("//option[@value='12.51']").click()
time.sleep(6)
#通过定位一组元素
# lists = driver.find_elements_by_tag_name("option")
#2.通过循环
# for list in lists:
#     if list.get_attribute('value') == "10.69":
#         list.click()
#3.通过下标
#list[2].click()
time.sleep(6)
driver.quit()