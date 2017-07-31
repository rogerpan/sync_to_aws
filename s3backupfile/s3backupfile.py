import boto3
import botocore
import pathlib


class S3Backupfile:

    def __init__(self, bucket_name, file_name, backup_base_dir):
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.backup_base_dir = backup_base_dir
        self.key_name = self.get_key_name()

    def get_key_name(self):
        a = self.file_name.split('/')
        b = self.backup_base_dir.split('/')
        c = []
        for i in range(len(a)):
            if i <= len(b)-1:
                if a[i] != b[i]:
                    if b[i] == '':
                        c.append(a[i])
                    else:
                        raise ValueError("backup file is not in the backup",
                                         " base folder.")
            else:
                c.append(a[i])
        return '/'.join(c)

    def check_file_exist(self):
        ffile = pathlib.Path(self.file_name)
        if ffile.is_file():
            return True
        else:
            return False

    def list_all_s3_objects(self):
        filelist = []
        conn = boto3.client('s3')
        for key in conn.list_objects(Bucket=self.bucket_name,Prefix=self.backup_base_dir )['Contents']:
            filelist.append(key['Key'])
        return filelist

    def list_s3_objects(self):
        filelist = []

        s3_client = boto3.client('s3')
        response = s3_client.list_objects(
            Bucket=self.bucket_name,
#            Prefix=self.backup_base_dir
        )

        # Loop through each file
        for file in response['Contents']:
            # Get the file name
            name = file['Key'].rsplit('/', 1)
            print(name)

    def check_s3_object_exist(self):
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
            s3.Object(self.bucket_name, self.key_name).load()
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                exists = False
            else:
                raise
        else:
            exists = True
        return exists
        