#!/usr/bin/env python3
import psutil
import shutil
import emails
import socket
import os

sender = 'automation@example.com'
recipient = '{}@example.com'.format(os.environ.get('USER'))
body_msg = 'Please check your system and resolve the issue as soon as possible.'

def check_cpu():
    try:
        CPU_PCT_THRESHOLD = 80
        cpu_percent = psutil.cpu_percent(interval=2)
        if cpu_percent > CPU_PCT_THRESHOLD:
            print('CPU percent: {}%. (NOT OK) Sending cpu alert...'.format(cpu_percent))
            cpu_msg = emails.generate(sender, recipient, 
                'Error - CPU usage is over 80%', body_msg)
            emails.send(cpu_msg)
        else:
            print('CPU percent: {}%. (OK)'.format(str(cpu_percent)))
    except Exception as e:
        # output error and ignore it for other function to continue
        print('Unexpected errors occurred! {}'.format(str(e)))

def check_memory():
    try:
        MEM_MINIMUM = 500
        mem_info = psutil.virtual_memory()
        mem_available = mem_info.available/(1024*1024)
        if mem_available < MEM_MINIMUM:
            print('Memory available: {}mb. (NOT OK) Sending memory alert...'.format(mem_available))
            mem_msg = emails.generate(sender, recipient, 
                'Error - Available memory is less than 500MB', body_msg)
            emails.send(mem_msg)
        else:
            print('Memory available: {}mb. (OK)'.format(mem_available))
    except Exception as e:
        # output error and ignore it for other function to continue
        print('Unexpected errors occurred! {}'.format(str(e)))

def check_disk_space():
    try:
        SPACE_MINIMUM = 20
        disk_space = shutil.disk_usage(os.path.expanduser('~'))
        free_space_pct = (disk_space.free / disk_space.total) * 100
        if free_space_pct < SPACE_MINIMUM:
            print('Free disk space: {}%. (NOT OK) Sending disk space alert...'.format(free_space_pct))
            disk_msg = emails.generate(sender, recipient, 
                'Error - Available disk space is less than 20%', body_msg)
            emails.send(disk_msg)
        else:
            print('Free disk space: {}%. (OK)'.format(free_space_pct))
    except Exception as e:
        # output error and ignore it for other function to continue
        print('Unexpected errors occurred! {}'.format(str(e)))

def check_localhost():
    try:
        DEFAULT_LOCAL_IP = '127.0.0.1'
        localhost_ip = ''
        try:
            localhost_ip = socket.gethostbyname('localhost')
        except:
            localhost_ip = 'IP resolution failed!'

        if localhost_ip == DEFAULT_LOCAL_IP:
            print('Localhost IP: {} (OK)'.format(localhost_ip))
        else:
            print('Localhost IP: {} (NOT OK) Sending localhost ip resolution alert... '.format(localhost_ip))
            disk_msg = emails.generate(sender, recipient, 
                'Error - localhost cannot be resolved to 127.0.0.1', body_msg)
            emails.send(disk_msg)
    
    except Exception as ee:
        # output error and ignore it for other function to continue
        print('Unexpected errors occurred! {}'.format(str(ee)))

def main():
    check_memory()
    check_disk_space()
    check_localhost()
    check_cpu()

if __name__ == '__main__':
    main()

