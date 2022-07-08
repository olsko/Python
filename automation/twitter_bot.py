from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Twitter_Bot():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.bot = webdriver.Chrome(service=service)
    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        email = bot.find_element(By.NAME, "text")
        bot.implicitly_wait(10)
        email.clear
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        password = bot.find_element(By.NAME, "password")
        password.clear
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10000)
ed = Twitter_Bot("email","pass")
ed.login()