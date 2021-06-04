#!/usr/bin/env python3

import csv
import datetime
import requests
import operator

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def getsortedemployees():
    ''' Read csv rows into lists and order by date column '''
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    return sorted(list(reader), key=operator.itemgetter(3))

def get_same_or_newer(start_date, employees):
    ''' search and filter out results to a final list based on date column '''
    return [x for x in employees if datetime.datetime.strptime(x[3], '%Y-%m-%d') >= start_date]
    
def list_newer(start_date):
    ''' generate and print final employees list report based on the input date '''
    employees = getsortedemployees()
    #print(employees)
    filtered_employees = get_same_or_newer(start_date, employees)
    #print(filtered_employees)
    for fname, lname, x, sdate in filtered_employees:
        fdate = datetime.datetime.strptime(sdate, '%Y-%m-%d')
        displaydate = datetime.datetime.strftime(fdate, '%b %d, %Y')
        displayname = ['{} {}'.format(fname, lname)]
        print('Started on {}: {}'.format(displaydate, displayname))

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

