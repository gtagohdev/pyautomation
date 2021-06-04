#!/usr/bin/env python3
import os
import requests

image_rel_path = 'supplier-data/images'
image_ws_endpoint = 'http://localhost/upload/' # or replace the localhost with endpoint IP

def post_image(image_filename):
    with open(image_filename, 'rb') as image_file:
        print('Post image file {}'.format(image_filename))
        response = requests.post(image_ws_endpoint, files={'file': image_file})
        print('Post result: {} - {}'.format(response.ok, response.status_code))

def upload_images():
    # get all files and dirs found in the specified file path
    image_full_path = os.path.join(os.path.expanduser('~'), image_rel_path)
    file_objects = os.listdir(image_full_path)
    print(file_objects)
    for fo in file_objects:
        if not fo.endswith('.jpeg'):
            continue
        
        image_filename = os.path.join(image_full_path, fo)
        post_image(image_filename)

if __name__ == '__main__':
    upload_images()


