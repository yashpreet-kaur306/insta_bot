from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_I_FOLLOW = "bts.bighitofficial"
USERNAME = "overtookbybts"
PASSWORD = "236#test"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys(USERNAME, Keys.DOWN)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(PASSWORD)
        time.sleep(2.1)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT_I_FOLLOW}/followers")

        time.sleep(8.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_everyone = self.driver.find_elements( By.CSS_SELECTOR, value='._aano button')
        for button in follow_everyone:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
            button.click()
            time.sleep(1)

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
