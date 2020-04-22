from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os;

os.environ["PATH"] += os.pathsep + r'C:\Users\fourth-home\Downloads\chromedriver_win32\chromedriver.exe';

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://remeeting.com/quiz/')

sleep(2)



