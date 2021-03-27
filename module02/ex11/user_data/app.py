#!/usr/bin/env python3

# ============================================================================#
# =============================== LIBRARIES ==================================#
# ============================================================================#

from flask import Flask, request, send_file
from s3_funcs import list_files, delete_file, upload_file, download_file

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
        'message': "Successfully listed files on s3 bucket '{}'".format(BUCKET),
        'content': list_files(BUCKET)
    }
    return response

@app.route('/delete/<filename>', methods= ['GET', 'POST'])
def delete(filename):
    if request.method == 'GET':
        response = {
            'status': 200,
            'message': "Successfully deleted file '{}' on s3 bucket '{}'".format(filename, BUCKET),
            'content': delete_file(filename, BUCKET)
        }
        return (response)

@app.route('/upload/<filename>', methods= ['GET', 'POST'])
def upload(filename):
    if request.method == 'GET':
        response = {
            'status': 200,
            'message': "Successfully uploaded file '{}' on s3 bucket '{}'".format(filename, BUCKET),
            'content': upload_file(filename, BUCKET)
        }
        return (response)

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        presigned_url = download_file(filename, BUCKET)
        response = {
            'status': 200,
            'message': "Successfully downloaded file '{}' on s3 bucket '{}'".format(filename, BUCKET),
            'content': presigned_url
        }
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)