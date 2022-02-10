'''

'''
# 
from os import environ, path
from google.cloud import storage


#environ["GOOGLE_CREDENTIALS"] = "/home/pi/"

PATH = path.dirname(__file__)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket_name = "food-inventory"
    source_file_name = "/home/pi/2021-11-29-105425_1920x1080_scrot.png"
    destination_blob_name = "blob/"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)