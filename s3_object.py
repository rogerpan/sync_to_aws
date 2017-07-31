import boto3
import botocore

s3_client = boto3.client('s3')

bucket = 'datg-databases-backup'
filename = 'decom_databases_backups/klcaptureserver.bak'


"""
Check if s3 object exists on S3 bucket.
return:
     True     objet exists
     False    object not exists
     Exception  communication error
"""
exists = False
try:
    s3 = boto3.resource('s3')
    s3.Object(bucket, filename).load()
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        exists = False
    else:
        raise
else:
    exists = True
print(exists)
