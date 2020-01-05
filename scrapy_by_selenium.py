from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
prefs = {'profile.default_content_settings.popups': 1, 'download.default_directory': 'E:\\Django\\website\\selenium'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="E:\Django\website\selenium\chromedriver.exe",chrome_options=options)
driver.get('http://localhost:8000/student/dl')
driver.find_element_by_link_text("download").click()

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