#! /bin/bash
amazon-linux-extras install python3
pip3 install flask
pip3 install boto3
nohup python3 /home/ec2-user/app.py