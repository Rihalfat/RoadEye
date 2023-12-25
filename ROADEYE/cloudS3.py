import boto3

AWS_ACCESS_KEY = "AKIAYXTIXN4H5LMEC5YA"
AWS_SECRET_KEY = "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"

BUCKET_NAME = 'seniorwatertub'


local_file_path = '1.avi'
s3_key = 'new_1.avi'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY)

# Upload the file with public-read ACL
with open(local_file_path, 'rb') as f:
    s3.upload_fileobj(f, BUCKET_NAME, s3_key, ExtraArgs={"ACL": "public-read"})

s3.put_object_acl(Bucket=BUCKET_NAME, Key=s3_key, ACL='public-read')