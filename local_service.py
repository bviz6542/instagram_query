import os
import json
from typing import List, Dict, Any, Optional
from user_credentials import UserCredentials
from friends_count import FriendsCount

class LocalService():
    def read_cookies(self) -> Optional[List[Dict[str, Any]]]:
        try:
            with open("./auth/cookies.json", "r") as jsonfile:
                cookies = json.load(jsonfile)
                return cookies
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def are_cookies_empty(self) -> bool:
        try:
            return os.path.getsize("./auth/cookies.json") == 0
        except FileNotFoundError:
            return True
        
    def save_cookies(self, cookies: List[Dict[str, Any]]) -> None:
        with open("./auth/cookies.json", "w") as jsonfile:
            json.dump(cookies, jsonfile)

    def read_user_credentials(self) -> Optional[UserCredentials]:
        try:
            with open("./auth/user_credentials.json", "r") as jsonfile:
                json_dict = json.load(jsonfile)
                return UserCredentials(username=json_dict["username"], password=json_dict["password"])
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        
    def read_friends_count(self) -> Optional[FriendsCount]:
        try:
            with open("./data/friends_count.json", "r") as jsonfile:
                json_dict = json.load(jsonfile)
                return FriendsCount(followers_count=json_dict["followers_count"], followings_count=json_dict["followings_count"])
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def save_friends_count(self, friends_count: FriendsCount) -> None:
        with open("./data/friends_count.json", "w") as jsonfile:
            json.dump(friends_count.to_dict(), jsonfile)