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
bucket_name = 'food-inventory'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)

my_bucket = storage_client.get_bucket('food-inventory')

# # Upload file

# def upload_to_bucket(blob_name, file_path, bucket_name): 
#     try: 
#         bucket = storage_client.get_bucket(bucket_name)
#         blob = bucket.blob(blob_name)
#         blob.upload_from_filename(file_path)
#         return True
#     except Exception as e: 
#         print(e)
#         return False

# file_path = '/home/pi/2021-11-29-105425_1920x1080_scrot.png' 
# upload_to_bucket('Image 1', os.path.join(file_path, '2021-11-29-105425_1920x1080_scrot.png') ,'food_inventory')
# upload_to_bucket('blob/Image 2', os.path.join(file_path, '2021-11-29-105425_1920x1080_scrot.png') ,'food_inventory')



# def upload_blob(bucket_name, source_file_name, destination_blob_name):
#     """Uploads a file to the bucket."""
#     bucket_name = "food-inventory"
#     source_file_name = "/home/pi/2021-11-29-105425_1920x1080_scrot.png"
#     destination_blob_name = ""

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)