'''

'''
# 
import os
from google.cloud import storage
import glob



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

"""
Upload a file
"""

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


for filename in glob.glob(os.path.join(file_path, '/images/*.jpg')): 
    upload_to_bucket('Image 3_{}'.format(filename), os.path.join(file_path, filename) ,'food-inventory')