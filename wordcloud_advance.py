#!/usr/bin/env python3
import datetime
import wordcloud
import re
import sys
import os

def countfrequency(wordsdict, words):
    ''' To count the occurences of each applicable word in the list and keep each word 
        and the corresponding count in the dictionary
    '''
    for word in words:
        #keep the word in either upper or lower capital for searching
        wordsdict[word.upper()] = wordsdict.get(word.upper(), 0) + 1

def readingwords(filepath):
    ''' To read text content from a file and transform the text into list
    of words and counting the frequency of each word '''
    #define list of non-interesting words for filtering
    noninterestingwords = ['THE','AND','SHE','HER', 'WAS', 'HIM', 'FOR', 'HAD', 'BUT','YOU']
    wordsfrequency = {}
    nonalpha_patterns = r'[^a-zA-Z]|\b[a-zA-Z]{1,2}\b'
    with open(filepath, mode='r', encoding='UTF-8') as f:
        for line in f:
            #replace all non-alpha or word shorter than 3 chars with single space
            finalline = re.sub(nonalpha_patterns, ' ', line)
            #convert to words list
            tmpwords = finalline.split()
            #filter out non-interesting words
            finalwords = [word.strip() for word in tmpwords if word.strip().upper() not in noninterestingwords]
            if len(finalwords) > 0: #only process if the words list is not empty                
                countfrequency(wordsfrequency, finalwords)
    return wordsfrequency

def generateimage(wordsfreq, output_filename):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordsfreq)
    cloud.to_file('{}.jpg'.format(output_filename)) #output jpg file to the current working directory

def runmain():
    filepath = ''
    sysinput = sys.argv
    if len(sysinput) < 2:
        filepath = input('Please enter a text file name (full path name): \n>>>>> ')
    else:
        #getting input file name from command line parameter
        filepath = sysinput[1]
    assert len(filepath.strip()) > 0, 'A text file name was not specified!'

    print('Reading contents from {} ...'.format(filepath))  
    bf_timestamp = datetime.datetime.now().timestamp()
    try:
        # reading input file from current working directory
        wordsfreq = readingwords(filepath.strip()) 
        read_timestamp = datetime.datetime.now().timestamp()
        print('Contents processed ({} seconds)'.format(str(read_timestamp-bf_timestamp)))
        #print(wordsfreq)
        #Derive output file name from the input file name
        fbasename = os.path.basename(filepath)
        output_filename = os.path.splitext(fbasename)[0]
        print('Generating image ...')
        generateimage(wordsfreq, output_filename)
        generate_timestamp = datetime.datetime.now().timestamp()
        print('{}.jpg generated ({} seconds)'.format(output_filename, str(generate_timestamp-read_timestamp)))
    except FileNotFoundError as eFile:
        print('ERROR: Ops! There were something incorrect!\n{}\nTry again.'.format(str(eFile)))
    except UnicodeDecodeError as eEncode:
        print('ERROR: Ops! Invalid file contents! Only text contents are supported.\n{}\nTry again.'.format(str(eEncode)))

if __name__ == '__main__':
    runmain()
   
