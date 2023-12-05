import yaml
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

#credentials_details()
class RDSDatabaseConnector:
    def __init__(self):
        pass
         
    def credentials_details(self):
        with open ('c:/Users/alanw/AI_CORE_FOLDER/Finance_project/credentials.yaml','r') as credentials:
            connenction_details= yaml.safe_load(credentials)
            #print(connenction_details)
            #print(type(connenction_details))
        return connenction_details

    def create_connection(self,connection_details):
        #set variables from connection details previous function
        database=connection_details['RDS_DATABASE']
        user=connection_details['RDS_USER']
        password=connection_details['RDS_PASSWORD']
        host=connection_details['RDS_HOST']
        port=connection_details['RDS_PORT']
        intro='postgresql+psycopg2://'
        engine = create_engine(f'{intro}{user}:{password}@{host}:{port}/postgres')
       # cursor=engine.connect()
       # select_query="Select * From loan_payments"
       # extract_data=cursor.execute(select_query)
        return engine
        df=pd.DataFrame(extract_data)
        print('connection successful')
        engine.close()
        cursor.close()

        return df
      

    def save_csv(self,create_connection):
        df.to_csv('C:/Users/alanw/AI_CORE_FOLDER/Finance_project.loan_payments.csv', index=False)



        

aws_data=RDSDatabaseConnector()

conn=aws_data.credentials_details() 
aws_data.create_connection(conn)

aws_data=pd.DataFrame()
csv_df=save_csv()           


        