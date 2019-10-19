import boto
from boto.s3.transfer import TransferConfig

# Set the desired multipart threshold value (5GB)
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)

# Perform the transfer
s3 = boto3.client('s3')
s3.upload_file('test.txt', 'testbucketjanne', 'upload_file', Config=config)
