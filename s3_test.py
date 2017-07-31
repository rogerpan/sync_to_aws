import boto3

s3_client = boto3.client('s3')

bucket = 'datg-databases-backup'
prefix = 'mssql/AM-NCKM-DSVM001/Program Files/Microsoft SQL Server/MSSQL10_50.MSSQLSERVER/MSSQL/Backup/master'

# List all objects within a S3 bucket path
response = s3_client.list_objects(
    Bucket = bucket,
    Prefix = prefix
)

# Loop through each file
for file in response['Contents']:

    # Get the file name
    name = file['Key'].rsplit('/', 1)
    print (name)
    # Download each file to local disk
    #s3_client.download_file(bucket, file['Key'], prefix + '/' + name[1])