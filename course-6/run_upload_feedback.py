#!/usr/bin/env python3
import os
import requests

data_full_path = '/data/feedback' # for windows example: d:/temp/feedback
feedback_ws_endpoint = 'http://localhost/feedback/' # or replace localhost with the endpoint IP

def upload_feedback(feedback):
    print('Post feedback {}'.format(feedback))
    response = requests.post(feedback_ws_endpoint, json=feedback)
    print('Post result: {} - {}'.format(response.ok, response.status_code))

def runmain():
    # get all files and dirs found in the specified file path
    file_objects = os.listdir(data_full_path)
    print(file_objects)
    for fo in file_objects:
        if not fo.endswith('.txt'):
            continue
        
        feedback = {}
        file_path = os.path.join(data_full_path, fo)
        with open(file_path, mode='r', encoding='UTF-8') as f:
            feedback['title'] = f.readline().strip()
            feedback['name'] = f.readline().strip()
            feedback['date'] = f.readline().strip()
            feedback['feedback'] = f.readline().strip()

        upload_feedback(feedback)


if __name__ == '__main__':
    runmain()


