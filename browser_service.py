from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import List, Dict, Any
from user_credentials import UserCredentials
from friends_count import FriendsCount

class BrowserService():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service('/opt/homebrew/bin/chromedriver'))
        
    def load_login_page(self):
        self.driver.get("https://www.instagram.com/")
        
    def get_cookies(self) -> List[Dict[str, Any]]:
        return self.driver.get_cookies()
    
    def refresh_cookies(self, cookies: List[Dict[str, Any]]):
        self.driver.delete_all_cookies()
        for c in cookies: self.driver.add_cookie(c)
        self.driver.refresh()
        
    def load_user_profile_page(self, username: str):
        self.driver.get((f"https://www.instagram.com/{username}"))
    
    def fill_in_user_credentials(self, user_credentials: UserCredentials):
        username = WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username.clear()
        username.send_keys(user_credentials.username)
        password = WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password.clear()
        password.send_keys(user_credentials.password)
        
    def press_login(self):
        WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))\
            .click()
            
    def fetch_friends_count(self) -> FriendsCount:
        followers_count = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]/span"))).text
        followings_count = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/following')]/span"))).text
        return FriendsCount(followers_count=int(followers_count), followings_count=int(followings_count))
    
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