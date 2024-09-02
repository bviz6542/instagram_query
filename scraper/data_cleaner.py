import pandas as pd

class DataCleaner:
    def clean_data(self):
        try:
            df = pd.read_csv('data/followers_list.csv')
            df = df.drop_duplicates()
            df['username'] = df['username'].replace('', pd.NA)
            df['username'] = df['username'].fillna(df['user_id'])
            
            try: df.to_csv('data/followers_list.csv', index=False, encoding='utf-8')
            except Exception as e: return
            
        except Exception as e: return