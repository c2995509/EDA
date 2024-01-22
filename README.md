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
Open and run the python file db_utilis.py file and run it. MAking sure the environemntal settings are correct.
The code will first open th yaml file and using a for loop extract each elements and population a dictionary list, that contains the relevant information
AWS requires. 
```
https://github.com/c2995509/EDA/db_utils.py
```
To run the code you will first need to change destination of the CSV file, to the location of your choosing, the current location will not work on other machines
The next process of the code is to extract the data from the rDS database. In this case was a table.
The table is then converted into a csv type file and a copy is made on the local drive

## Data Quality Review
The data review was mainly been done in notebook. The reason for using notebook instead of a python file.
Is simply easier to review all graphical illustration compared to using the terminal. The only elements where python file was used
to open up the csv file, convert relevant elements and change data types within the data Table
To set notebook up the following programs reqired importing:
### Software Requirement
- import pandas as pd
- import numpy as np 
- import matplotlib.pyplot as plt 
- from data_review import DataTransform as dt
- import seaborn as sns
- from statsmodels.graphics.gofplots import qqplot
- from scipy import stats
  
When reviewing the data quality of the data frame, as review found certain columns had over 20% null values, Each of these columns where
reviewed for the remining content and found the information was not necessary. Therefore those columns where deleted
The action where recorded in the file data analyse ipynb.
Also with the aid of graphical illustration to find out if the data had any skewed data, and where apprioprate redistrute the data, 
so  more balance information data set is made.
- df.shape
- data_info=df.info()
- print(data_info)
- data_stats=df.describe()
- print(data_stats)
## Problems discovered
As I am new to pyhton some of the training material supplied was extreemely long, and never went into the coding details, and how to create
visual element, which is very frustrating, it's like training someone to build a house and showing what the elements are but not explaining how they go together.
Unfortunately the fault is still there with the training manual

## *Loan Payment Review*
The data set was new to me and industry terminology was used, so understanding what the loan data represented took a bit of time.
A python file was create and the following code was used and called in relevant sections of the notebook, to transfer the data, etc so the data frame could be analysed
### Software Requirements
Import the following software
 - pandas
 - numpy
 - matplotlib.pyplot
 - seaborn
 - scipy

Also it is adviseble to include pd.set_option('display.max_columns', None), as part of the set up.
As previously using the original data table extracted from AWS RDS, a data quality check is required especially covering null values.
Once a list of Null values table is produced, the next step is to find any patterns between other columns and populate the null values with actual.
After the null values issue has been addressed the next stage is to convert the term column to a numerical data type by removing the text "months" for the column text values. This has been doen by calling a function previously programmed into a python file.

Once the data quality and data types have been corrected. The next stage is to start to analysis the loan data.
 - What type of loans being reported. In this case the loan data referes to front loaded loans, for customers who mainly consolidate existing debts 
 - Outstanding balance of all existing loans (ignore fully paid loans
 - What is the remaining percentage is the balance
 - How much of the loans will be paid off after another 6 months
 - Outstanding balance & percentage after 6 months
 - Which group are likely to default
 From what the data shows the group that have a graade 'C' seeme to be more likely to default in repaying the loan back, and having the laon disharged. Also Grae C category are generally in rented accommodation.

 - 
