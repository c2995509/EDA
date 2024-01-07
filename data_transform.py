import pandas as pd
from sqlalchemy import create_engine
class DataTransform:
    @staticmethod
    #date object to datetime
    def convert_date_to_datetime(df, date_column):
        df[date_column] = df[date_column].apply(lambda x: pd.to_datetime(x, errors='coerce', format='%b-%Y'))
        return df
    @staticmethod
    #to integer
    def convert_to_integer(df, column_name):
        if column_name in ['employment_length', 'term']:
            # Extract numeric part from 'X years' format
            df[column_name] = df[column_name].str.extract('(\d+)').astype('Int64')
        else:
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce').astype('Int64')
        return df

    @staticmethod
    #to categorical
    def convert_to_categorical(df, column_name):
        df[column_name] = df[column_name].astype('category')
        return df