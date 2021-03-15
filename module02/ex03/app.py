from flask import Flask, request, send_file
from s3_funcs import list_files

app = Flask(__name__)
BUCKET = "module02-12345"

@app.route('/')
def home():
    response = {}
    response['status'] = "200"
    response['message'] = "Successfully connected to module03 cloud storage API"
    return response


@app.route("/list_files")
def list_bucket():
    response = {}
    response['status'] = "200"
    response['message'] = "Successfully listed files on s3 bucket '{}'.".format(BUCKET)
    response['content'] = list_files(BUCKET)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
