# **EDA Project**
Objective
The Objective of this project is as follows
1. Create a YAML file
2. Use YAML file contents to extract a file from AWS RDS database
3. Note: Keeping the YAML details secure
4. Use SQL function with python in the process
5. Review that data quality of the data table extracted
6. Review the distribution of the data and if necessary modify accordingly
7. (If Applicanble) If the data is skewed, correct the skewed accotrdingly
8. Analysis the data, find ouEDA project upto Git Hub andt if there is a risk, and any collating data
9. Report process via a READ ME file
10. Upload all files create upto GIT Hub, excluding YAML file, and Ignore file
Note: Environment Python 3.18, Pandas
## Create YAML File
The first step was to find about a YAML file. "Yet another markup language"
Open VSC and select create new file. Type in "EDA.yaml" (yaml is the file extension)
 - RDS_HOST: ********************
 - RDS_PASSWORD: ******
 - RDS_USER: *******
 - RDS_DATABASE: *************
 - RDS_PORT: ***********
## Extract Data using YAML
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
