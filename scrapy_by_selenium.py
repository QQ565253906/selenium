from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from datetime import datetime
import pdb

options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_arguhoment('--disable-dev-shm-usage')
prefs = {'profile.default_content_settings.popups': 1, 'download.default_directory': 'E:\\Django\\website\\selenium'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="E:\Django\website\selenium\chromedriver.exe",options=options)
# driver.get('http://localhost:8000/student/dl')
driver.get('http://localhost:8000/student/login')
username = driver.find_element_by_id("id_username")
username.send_keys('mtk40721')
password = driver.find_element_by_id("id_password")
password.send_keys('123')
submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.click()
# pdb.set_trace()

#in dl page->download won't effect
dl=driver.find_element_by_link_text("download")
dl.click()

#in csv page->download will effect
dl=driver.find_element_by_link_text("download")
dl.click()
print(datetime.now())
time.sleep(1    )
print(datetime.now())
# driver.quit()

# from selenium import webdriver # 从selenium导入webdriver
# options = webdriver.ChromeOptions()
# options.binary_location = r"E:\Django\website\selenium\chromedriver.exe"
# #prefs = {'profile.default_content_settings.popups': 1, 'download.default_directory': 'd:\\'}
# #options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options=options)
# #driver = webdriver.Chrome(r"chromedriver.exe")  # Optional argument, if not specified will search path.
# #driver.get('https://www.baidu.com') # 获取百度页面
# driver.get('http://localhost:8000/student/dl')
# driver.find_element_by_link_text("download").click()