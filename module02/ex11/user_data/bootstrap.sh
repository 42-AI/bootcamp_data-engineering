#! /bin/bash
aws s3 cp s3://module02-12345/app.py /home/ec2-user/app.py
aws s3 cp s3://module02-12345/s3_funcs.py /home/ec2-user/s3_funcs.py
amazon-linux-extras install python3
pip3 install flask
pip3 install boto3
nohup python3 /home/ec2-user/app.py