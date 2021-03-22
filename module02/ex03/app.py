#!/usr/bin/env python3

# ============================================================================#
# =============================== LIBRARIES ==================================#
# ============================================================================#

from flask import Flask, request, send_file
from s3_funcs import list_files

# ============================================================================#
# ================================ FUNCTIONS =================================#
# ============================================================================#

app = Flask(__name__)
BUCKET = "module02-12345"

@app.route('/')
def home():
    response = {
        'status': 200,
        'message': 'Successfully connected to module02 cloud storage API'
    }
    return response

@app.route("/list_files")
def list_bucket():
    response = {
        'status': 200,
        'message': "Successfully listed files on s3 bucket '{}'.".format(BUCKET),
        'content': list_files(BUCKET)        
    }
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)