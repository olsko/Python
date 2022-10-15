from time import sleep
from selenium import webdriver
from selenium_utilities import getChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Timewall_bot():
    def __init__(self, email, password):
        #Credentials
        self.email = email
        self.password = password
        #Settings
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        #Recaptcha solver
        options.add_argument('--lang=en-US') #need for recaptcha be in english
        options.add_extension(r"Noptcha--ReCAPTCHA---hCAPTCHA-Solver.crx")
        #Disables popups
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        self.bot = webdriver.Chrome(executable_path=getChromeDriver(), options=options)

    def login(self):
        bot = self.bot
        #open the website
        bot.get("https://timewall.io/users/login?oid=&uid=")
        sleep(2)
        bot.refresh()
        #Finding input boxes and pasting the credentials
        email_box = bot.find_element(By.NAME, "email")
        password_box = bot.find_element(By.NAME, "password")
        email_box.send_keys(self.email)
        password_box.send_keys(self.password)
        #Captcha
        sleep(30)
        password_box.send_keys(Keys.RETURN)
        bot.get("https://timewall.io/clicks")
        sleep(2)
    def clicks(self):
        bot = self.bot
        timewall = bot.current_window_handle
        sleep(15)
        while True:
            bot.switch_to.window(timewall)
            sleep(3)
            #Store how much to wait
            clickTimer = bot.find_elements(By.CLASS_NAME, "clickTimer")
            wait_time = clickTimer[0]
            wait_time = wait_time.text
            #Button to view the website
            bot.find_element(By.CSS_SELECTOR, "a.clickBtn").click()
            sleep(1)
            sleep(int(wait_time))
            #Close all tabs except timewall
            for window_handle in bot.window_handles:
                if window_handle != timewall:
                    bot.switch_to.window(window_handle)
                    bot.close()


if __name__ == "__main__":
    bot = Timewall_bot("username", "password")
    bot.login()
    bot.clicks()