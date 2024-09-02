class UserCredentials:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def __repr__(self):
        return f"UserCredentials(username={self._username}, password={self._password})"

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password