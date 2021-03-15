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