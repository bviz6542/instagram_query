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

import time
import csv

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
    
    def press_followers(self):
        WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers')]")))\
            .click()

    def press_followings(self):
        WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/following')]")))\
            .click()

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

    def scroll_followers_list(self):
        try:
            # Find the scrollable container using the provided XPath
            scrollable_container = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]")
            print("Scrollable container found.")
        except:
            print("Error: Scrollable container not found with the provided XPath.")
            return

        prev_height = 0
        scroll_attempts = 0
        max_scroll_attempts = 5

        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_container)
            time.sleep(2)

            curr_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable_container)
            print(f"Scrolled to height: {curr_height}")

            if curr_height == prev_height:
                scroll_attempts += 1
                if scroll_attempts >= max_scroll_attempts:
                    print("No new followers loaded after several attempts. Ending scroll.")
                    break
            else:
                scroll_attempts = 0

            prev_height = curr_height

        # Wait briefly to ensure all elements are loaded
        time.sleep(2)

        # Attempt to extract follower elements
        try:
            followers_info = []

            # Adjust the XPath based on observed HTML structure
            follower_divs = scrollable_container.find_elements(By.XPATH, ".//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w')]")
            
            if not follower_divs:
                print("No follower elements found within the scrollable container.")
                return

            for follower_div in follower_divs:
                try:
                    user_id_elem = follower_div.find_element(By.XPATH, ".//a/div/div/span")
                    username_elem = follower_div.find_element(By.XPATH, ".//span/span")

                    user_id = user_id_elem.text if user_id_elem else "No User ID"
                    username = username_elem.text if username_elem else "No Username"

                    followers_info.append({"user_id": user_id, "username": username})
                except Exception as e:
                    print(f"Error extracting user info: {str(e)}")
                    continue

            print(f"Total Followers Found: {len(followers_info)}")
            for follower in followers_info:
                print(f"User ID: {follower['user_id']}, Username: {follower['username']}")

        except Exception as e:
            print(f"Error: Unable to extract follower information. {str(e)}")
