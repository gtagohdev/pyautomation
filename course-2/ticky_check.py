#!/usr/bin/env python3
import re
import csv
import operator
from collections import OrderedDict

userstsc = {}
errorstsc = {}
# define search patterns with results grouping
# 1 - log type (INFO or ERROR)
# 2 - error description
# 3 - user name
search_patterns = r'ticky: (INFO|ERROR) ([\w\s\'\"\.]+)[\[\]#\d ]*\((.+)\)$'
# read line by line from syslog.log (assume the file in current working directory)
with open('syslog.log', 'r') as log:
    for line in log:
        result = re.search(search_patterns, line)
        if result:
            #get detailed statistics from userstsc. create new detailedstsc if not found
            detailedstsc = userstsc.get(result.group(3).strip(), 
                    dict({'Username':result.group(3).strip(), 'INFO':0, 'ERROR':0}))
            if result.group(1).strip() == 'ERROR':           
                #increase error desc count
                errorstsc[result.group(2).strip()] = errorstsc.get(result.group(2).strip(), 0) + 1
                #increase ERROR count for the user
                detailedstsc["ERROR"] += 1
                userstsc[result.group(3).strip()] = detailedstsc 
            elif result.group(1).strip() == 'INFO':
                #increase INFO count for the user
                detailedstsc["INFO"] += 1
                userstsc[result.group(3).strip()] = detailedstsc
# sorting user and error statistics
sorted_errorstsc = sorted(errorstsc.items(), key=operator.itemgetter(1), reverse=True)
sorted_userstsc = sorted(userstsc.items())
print('Sorted error statistics: {}'.format(sorted_errorstsc))
print('Sorted user statistics: {}'.format(sorted_userstsc))
# save error statistics to error_message.csv file using csv common functionality
with open('error_message.csv', 'w') as errorfile:
    writer = csv.writer(errorfile)
    writer.writerow(['Error', 'Count'])
    writer.writerows(sorted_errorstsc)
# save user statistics to user_statistics.csv file using csv DictWriter functionality
with open('user_statistics.csv', 'w') as userfile:
    writer = csv.DictWriter(userfile, fieldnames=['Username', 'INFO', 'ERROR'])
    writer.writeheader()
    writer.writerows(OrderedDict(sorted_userstsc).values())

