import os

def create_file_if_not_exists(file_name: str):
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(file_name):
        with open(file_name, "w") as jsonfile: pass

create_file_if_not_exists("./auth/cookies.json")
create_file_if_not_exists("./auth/user_credentials.json")
create_file_if_not_exists("./data/friends_count.json")