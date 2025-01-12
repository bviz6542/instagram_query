from scraper import Scraper

scraper = Scraper()
scraper.login()
scraper.go_to_user_profile()
scraper.go_to_followers()
scraper.get_back_to_user_profile()
scraper.go_to_followings()

