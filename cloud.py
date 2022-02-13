'''

'''
# 
import os
from google.cloud import storage


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/pi/ServiceKey.json'

storage_client = storage.Client()

"""
Create a New Bucket
"""
# bucket_name = 'food-inventory'
# bucket = storage_client.bucket(bucket_name)
# bucket.location = 'US'
# bucket = storage_client.create_bucket(bucket)

# my_bucket = storage_client.get_bucket('food-inventory')

# Upload file

def upload_to_bucket(blob_name, file_path, bucket_name): 
    try: 
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e: 
        print(e)
        return False

file_path = '/home/pi/' 
upload_to_bucket('Image 1', os.path.join(file_path, '2021-11-29-105425_1920x1080_scrot.png') ,'food-inventory')
upload_to_bucket('blob/Image 2', os.path.join(file_path, '2021-11-29-105425_1920x1080_scrot.png') ,'food-inventory')