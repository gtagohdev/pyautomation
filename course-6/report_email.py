#!/usr/bin/env python3
import emails
import reports
import os
from datetime import datetime

report_filename = '/tmp/processed.pdf' # for windows: d:/temp/processed.pdf

def process_data():
    data_rel_path = 'supplier-data/descriptions'
    data_full_path = os.path.join(os.path.expanduser('~'), data_rel_path)
    file_objects = os.listdir(data_full_path)
    print(file_objects)
    fruits_data = []
    for fo in file_objects:
        if not fo.endswith('.txt'):
            continue
          
        file_path = os.path.join(data_full_path, fo)
        with open(file_path, mode='r', encoding='UTF-8') as f:
            fruits_data.append({'name': f.readline().strip(), 'weight': f.readline().strip()})
    
    return fruits_data

def format_display(data_list):
    data_display = ''
    for data_dict in data_list:
        data_display = '{}<br/>name: {}<br/>weight: {}<br/>'.format(data_display, data_dict['name'], data_dict['weight'])

    return data_display

def main():
    data_list = process_data()
    print(data_list)
   
    displaydate = datetime.strftime(datetime.now(), '%B %d, %Y')
    report_title = 'Processed Update on {}'.format(displaydate)
    report_info = format_display(data_list)
    reports.generate_report(report_filename, report_title, report_info)
    print('Report generated - {}'.format(report_filename))

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, report_filename)
    emails.send(message)
    print('Email sent.') 

if __name__ == "__main__":
  main()

