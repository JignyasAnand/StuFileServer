import logging
import boto3
from botocore.exceptions import ClientError
import os

try:
    from .secret import ACCESS_KEY, SEC_ACCESS_KEY, BUCKET
except:
    from secret import ACCESS_KEY, SEC_ACCESS_KEY
s3_client = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SEC_ACCESS_KEY
                      )

BUCKET=BUCKET

def upload_file(file_name, bucket, object_name=None):
    global s3_client
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def genurl(name):
    temp=s3_client.generate_presigned_url("get_object",Params = {'Bucket': BUCKET, 'Key': name}, ExpiresIn=500)
    return temp

def getconts():
    arr=[]
    objects = s3_client.list_objects_v2(Bucket=BUCKET)
    for obj in objects['Contents']:
        arr.append(obj['Key'])
    return arr


# upload_file("secret.py", BUCKET)
# s3_client.download_file(BUCKET, 'img1.jpg', "newf.jpg")


if __name__ == '__main__':
    x=getconts()
    print("x0|0x".join(x))
    # print(genurl("secret.py"))