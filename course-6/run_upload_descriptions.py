#!/usr/bin/env python3
import os
import requests

data_rel_path = 'supplier-data/descriptions' 
desc_ws_endpoint = 'http://localhost/fruits/' # or replace localhost with the endpoint IP

def post_description(description):
    print('Post description {}'.format(description))
    response = requests.post(desc_ws_endpoint, json=description)
    print('Post result: {} - {}'.format(response.ok, response.status_code))

def upload_descriptions():
    # get all files and dirs found in the specified file path
    data_full_path = os.path.join(os.path.expanduser('~'), data_rel_path)
    file_objects = os.listdir(data_full_path)
    print(file_objects)
    for fo in file_objects:
        if not fo.endswith('.txt'):
            continue
        
        description = {}
        file_path = os.path.join(data_full_path, fo)
        with open(file_path, mode='r', encoding='UTF-8') as f:
            description['name'] = f.readline().strip()
            description['weight'] = int(f.readline().strip().split(' ')[0])
            description['description'] = f.readline().strip()

            image_name = '{}.jpeg'.format(os.path.splitext(fo)[0])
            description['image_name'] = image_name
        
        post_description(description)


if __name__ == '__main__':
    upload_descriptions()

