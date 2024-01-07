import pandas as pd
df = pd.read_csv('C:/Users/alanw/AI_CORE_FOLDER/Finance_project/loan_payments.csv')
class DataTransform:
    def __init__(self):
        self.df=df
        pass

    @staticmethod
    def modeval(df,column):
        for column in df:
            df['int_rate'] = df['int_rate'].fillna(df['int_rate'].median())
            return(df)
    @staticmethod
    def conv_to_integer(df,column):
        column=df['funded_amount']
        for column in df:
            #df['funded_amount']=df['funded_amount'].fillna('loan_amount')
            df['funded_amount']=pd.to_numeric(df['funded_amount'],errors='coerce')
            return df
    @staticmethod
    def convert_to_integer(df,column):
        column=df['term']
        for column in df:
            df['term']=df['term'].fillna('36 months')
            df['term']=df['term'].str.extract('(\d+)')
            df['term']=pd.to_numeric(df['term'],errors='coerce')
            return df

    
DataTransform=DataTransform()
Transform=DataTransform.conv_to_integer(df,'funded_amount')
Transform=DataTransform.convert_to_integer(df,'term')
Transform=DataTransform.modeval(df,'int_rate')

        
