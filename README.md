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
The next process of the code is to extract the data from the rDS database. In this case was a table.
The table is then converted into a csv type file and a copy is made on the local drive

## Data Quality Review
The data review was mainly been done in notebook. The reason for using notebook instead of a python file.
Is simply easier to review all graphical illustration compared to using the terminal. The only elements where python file was used
to open up the csv file, convert relevant elements and change data types within the data Table
