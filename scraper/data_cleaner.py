import pandas as pd
from pandas import DataFrame

class DataCleaner:
    def clean_followers_data(self):
        self.clean_data('data/followers_list.csv')
        
    def clean_followings_data(self):
        self.clean_data('data/followings_list.csv')
        
    def clean_data(self, file_path: str):
        try:
            df = pd.read_csv(f'{file_path}')
            df = df.drop_duplicates()
            df['username'] = df['username'].replace('', pd.NA)
            df['username'] = df['username'].fillna(df['user_id'])
            
            try: df.to_csv(f'{file_path}', index=False, encoding='utf-8')
            except Exception as e: return
            
        except Exception as e: return
        
    def find_relationships(self) -> tuple[DataFrame, DataFrame, DataFrame]:
        try:
            followers_df = pd.read_csv('data/followers_list.csv')
            followings_df = pd.read_csv('data/followings_list.csv')
            only_following = followings_df[~followings_df['username'].isin(followers_df['username'])]
            only_followed = followers_df[~followers_df['username'].isin(followings_df['username'])]
            both = followers_df[followers_df['username'].isin(followings_df['username'])]
            return only_following, only_followed, both
        
        except Exception as e:
            print(f"Error occurred: {e}")
            return None, None, None