'''
Putting all useful links here:
https://stackoverflow.com/questions/62799852/read-pdf-object-from-s3
https://stackoverflow.com/questions/56716852/what-is-a-cost-effective-solution-to-store-pdf-files-on-cloud-when-i-am-using-aw
https://flask-s3.readthedocs.io/en/latest/
'''


import json
import os
import boto3


def download_json_files(bucket: str, prefix: str, local_dir: str) -> None:
    bucket = boto3.resource("s3").Bucket(bucket)
    objects = bucket.objects.filter(Prefix=prefix)
    keys = [obj.key for obj in objects if obj.key.endswith(".json")]

    local_paths = [os.path.join(local_dir, key) for key in keys]

    for key, local_path in zip(keys, local_paths):
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        bucket.download_file(key, local_path)


'''def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output


def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)

    return contents'''
