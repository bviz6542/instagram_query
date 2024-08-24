import os
import json
from typing import List, Dict, Any, Optional
from user_credentials import UserCredentials

class LocalAccessor():
    @staticmethod
    def read_cookies() -> Optional[List[Dict[str, Any]]]:
        try:
            with open("./auth/cookies.json", "r") as jsonfile:
                cookies = json.load(jsonfile)
                return cookies
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    @staticmethod
    def are_cookies_empty() -> bool:
        try:
            return os.path.getsize("./auth/cookies.json") == 0
        except FileNotFoundError:
            return True
        
    @staticmethod
    def save_cookies(cookies: List[Dict[str, Any]]) -> None:
        with open("./auth/cookies.json", "w") as jsonfile:
            json.dump(cookies, jsonfile)

    @staticmethod
    def read_user_credentials() -> Optional[UserCredentials]:
        try:
            with open("./auth/user_credentials.json", "r") as jsonfile:
                json_dict = json.load(jsonfile)
                return UserCredentials(username=json_dict["username"], password=json_dict["password"])
        except (FileNotFoundError, json.JSONDecodeError):
            return None