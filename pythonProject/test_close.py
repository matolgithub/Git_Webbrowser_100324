import webbrowser
import time
from selenium import webdriver

# webbrowser.open_new_tab("https://kvartiravkaluge.ru/")

driver = webdriver.Chrome()
driver.get("https://kvartiravkaluge.ru/")
time.sleep(5)

driver.execute_script("window.close();")
