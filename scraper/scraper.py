import time
from browser_service import BrowserService
from local_service import LocalService
from data_handler import DataHandler

class Scraper():
    def __init__(self):
        self.browser_service = BrowserService()
        self.local_service = LocalService()
        self.data_cleaner = DataHandler()
        self.username = ""

    def login(self):       
        self.browser_service.load_login_page()
        if self.local_service.are_cookies_empty:
            user_credentials = self.local_service.read_user_credentials()
            self.browser_service.fill_in_user_credentials(user_credentials=user_credentials)
            self.browser_service.press_login()
            time.sleep(7)
            cookies = self.browser_service.get_cookies()
            self.local_service.save_cookies(cookies=cookies)
            self.username = self.local_service.read_user_credentials().username
            
        else:
            cookies = self.local_service.read_cookies()
            self.browser_service.refresh_cookies(cookies=cookies)
            time.sleep(7)
            self.username = self.local_service.read_user_credentials().username

    def go_to_user_profile(self):
        self.browser_service.load_user_profile_page(username=self.username)
        try:
            friends_count = self.browser_service.fetch_friends_count()
            self.local_service.save_friends_count(friends_count=friends_count)
            time.sleep(5)
        except Exception as e:
            return
    
    def go_to_followers(self):
        self.browser_service.press_followers()
        time.sleep(3)
        self.browser_service.scroll_followers_list(callback=self.local_service.write_followers_to_csv)
        self.data_cleaner.clean_followers_data()
        
    def get_back_to_user_profile(self):
        self.browser_service.load_user_profile_page(username=self.username)
        time.sleep(2)
        
    def go_to_followings(self):
        self.browser_service.press_followings()
        time.sleep(3)
        self.browser_service.scroll_followings_list(callback=self.local_service.write_followings_to_csv)
        self.data_cleaner.clean_followings_data()

        