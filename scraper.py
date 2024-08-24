from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from local_accessor import LocalAccessor

class Scraper():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('/opt/homebrew/bin/chromedriver'))
        self.main_user = ""
        self.followers_count = 0
        self.followings_count = 0

    def load_page(self):
        self.driver.get("https://www.instagram.com/")

    def login(self):
        if LocalAccessor.are_cookies_empty:
            user_credentials = LocalAccessor.read_user_credentials()
            username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            username.clear()
            username.send_keys(user_credentials.username)
            password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
            password.clear()
            password.send_keys(user_credentials.password)
            WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))\
                .click()
            time.sleep(7)
            cookies = self.driver.get_cookies()
            LocalAccessor.save_cookies(cookies=cookies)
            self.main_user = LocalAccessor.read_user_credentials().username
            
        else:
            self.driver.delete_all_cookies()
            cookies = LocalAccessor.read_cookies()
            for c in cookies:
                self.driver.add_cookie(c)
            self.driver.refresh()
            time.sleep(7)
            self.main_user = LocalAccessor.read_user_credentials().username

    def main_user_profile(self):
        self.driver.get((f"https://www.instagram.com/{self.main_user}"))
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))
            )
            self.followers_count = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]/span").text
            self.followings_count = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followings')]/span").text
            print(self.followers_count, self.followings_count)
        except Exception as e:
            print(e)

    def tab_action(self, times):
        for i in range(times):
            ActionChains(self.driver)\
                .key_down(Keys.TAB)\
                .perform()
    
    def enter_action(self):
        ActionChains(self.driver)\
            .key_down(Keys.ENTER)\
            .perform()
        
    def tabShift_action(self, times):
        for i in range(times):
            ActionChains(self.driver)\
                .key_down(Keys.SHIFT)\
                .key_down(Keys.TAB)\
                .perform()
            ActionChains(self.driver)\
                .key_up(Keys.SHIFT)\
                .perform()