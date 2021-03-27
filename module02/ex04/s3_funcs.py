import boto3

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3_client = boto3.client('s3')
    contents = []
    for item in s3_client.list_objects(Bucket=bucket)['Contents']:
        contents.append(item['Key'])
    return contents

def delete_file(file_name, bucket):
    """
    Function to delete a file to an S3 bucket
    """
    s3_client = boto3.client('s3')
    return s3_client.delete_object(Bucket=bucket, Key=file_name)

def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    s3_client = boto3.client('s3')
    return s3_client.generate_presigned_post(bucket, file_name)

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3_client = boto3.client('s3')
    return s3_client.generate_presigned_url('get_object',
                                     Params={'Bucket': bucket, 'Key': file_name},
                                     ExpiresIn=60)