# ML Assessment


## Data Analysis

In the data analysis assessment patient record was mapped using Citizen number and Patient number. Left join was used to join table and it was identified after joining that few record **(89 out of 1000)** were not mapped with admission table. Those records were then mapped based on Admission date and time column which was already present processed data table. After that only **4 records** were not mapped which were discarded from the overall data set. 

Data Analysis folder contains :
1- One notebook file with all cleaning and mapping code along.
2- Data Folder with input files are copied in this folder
3- Reports Folder: Profiling report generated during EDA are stored in this folder.




## API

API folder consist of two python script files. One with the flask API code and other with the helping method. You can run this script by using following command but before that make sure you have flask and flask_jsonpify installed: 

```
python API.py
```

Flask API will by deployed at **port number 5000**. You can use postman for GET request. It expect 4 arguments (notes_path, patient_path, admission_path and processd_path). Sample url is given as follow:

http://localhost:5000/?notes_path=notes.csv&patient_path=patient_mapping.csv&admission_path=admission.csv&processed_path=processed_data.csv


