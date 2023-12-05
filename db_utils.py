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
        return connenction_details

    def create_connection(self,connection_details):
        #set variables from connection details previous function
        database=connection_details['RDS_DATABASE']
        user=connection_details['RDS_USER']
        password=connection_details['RDS_PASSWORD']
        host=connection_details['RDS_HOST']
        port=connection_details['RDS_PORT']
        intro='postgresql+psycopg2://'
        #Create connection to AWS RDS server
        engine = create_engine(f'{intro}{user}:{password}@{host}:{port}/{database}')
        #Extract SQL table called 'loan_project' from database
        df=pd.read_sql_table("loan_payments",engine)
        print('connection successful')
        #Return SQL table into a data frame
        return df
        #engine.close()
        #cursor.close()

   
#Calling Class
aws_data=RDSDatabaseConnector()
conn=aws_data.credentials_details() 
#Defining df with function variable
df=aws_data.create_connection(conn)
#publish dataframe into a CSV file         
df.to_csv('C:/Users/alanw/AI_CORE_FOLDER/Finance_project/loan_payments.csv',index = False)

        