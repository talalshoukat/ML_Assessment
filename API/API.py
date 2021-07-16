# Uncomment below line to install dependencies if not already installed
# !pip install  flask 
# !pip install  flask_jsonpify


# Importing Libraries
from flask import Flask,request
from flask_jsonpify import jsonpify
import helping_method 

app = Flask(__name__)
 
# Flask API to mapping csv files  
@app.route("/", methods=['GET'])
def home():
    try:
        # Unpacking input arguments  
        args = request.args
        notes_path = args['notes_path']
        patient_path = args['patient_path']
        admission_path = args['admission_path']
        processed_path = args['processed_path']

        # Null check to see if any argument is null  
        if all(v is not None for v in [notes_path, patient_path,admission_path, processed_path]):
            result =helping_method.mapping(notes_path, patient_path, admission_path, processed_path)
            result_list = result.values.tolist()
            JSONP_data = jsonpify(result_list)
            return JSONP_data   
        else:
            return f"<h1>Please provide all file paths.</h1>"
    except:
        return "<h1>An Error Occured During Processing. Please provide correct Input file paths.</h1>"
    
app.run(host='0.0.0.0', port=5000)