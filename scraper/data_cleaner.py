import pandas as pd

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
            
            try: df.to_csv('data/followers_list.csv', index=False, encoding='utf-8')
            except Exception as e: return
            
        except Exception as e: return