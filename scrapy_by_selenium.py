from selenium import webdriver # 从selenium导入webdriver

driver = webdriver.Chrome(r"chromedriver.exe")  # Optional argument, if not specified will search path.
#driver.get('https://www.baidu.com') # 获取百度页面
driver.get('http://localhost:8000/student/dl')
driver.find_element_by_link_text("download").click()