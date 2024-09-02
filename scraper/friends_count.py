from typing import Dict

class FriendsCount:
    def __init__(self, followers_count: int, followings_count: int) -> None:
        self._followers_count = followers_count
        self._followings_count = followings_count
    
    @property
    def followers_count(self) -> int:
        return self._followers_count
    
    @property
    def followings_count(self) -> int:
        return self._followings_count
    
    def to_dict(self) -> Dict[str, int]:
        return {
            "followers_count": self._followers_count,
            "followings_count": self._followings_count
        }