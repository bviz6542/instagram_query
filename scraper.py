import time
from browser_service import BrowserService
from local_service import LocalService

class Scraper():
    def __init__(self):
        self.browser_service = BrowserService()
        self.local_service = LocalService()
        self.main_user = ""

    def login(self):       
        self.browser_service.load_login_page()
        if self.local_service.are_cookies_empty:
            user_credentials = self.local_service.read_user_credentials()
            self.browser_service.fill_in_user_credentials(user_credentials=user_credentials)
            self.browser_service.press_login()
            time.sleep(7)
            cookies = self.browser_service.get_cookies()
            self.local_service.save_cookies(cookies=cookies)
            self.main_user = self.local_service.read_user_credentials().username
            
        else:
            cookies = self.local_service.read_cookies()
            self.browser_service.refresh_cookies(cookies=cookies)
            time.sleep(7)
            self.main_user = self.local_service.read_user_credentials().username

    def user_profile(self):
        self.browser_service.load_user_profile_page(username=self.main_user)
        try:
            friends_count = self.browser_service.fetch_friends_count()
            self.local_service.save_friends_count(friends_count=friends_count)
            time.sleep(5)
        except Exception as e:
            return