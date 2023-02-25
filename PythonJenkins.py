import time

from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service

s=Service("C:\Browserdrivers\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(6)
PageTitle=driver.title
print("The title is",PageTitle)
driver.close()