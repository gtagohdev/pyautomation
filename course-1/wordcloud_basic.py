#!/usr/bin/env python3
import datetime
import wordcloud

def validateword(word):
    ''' To validate a word and return True if the word is a normal and acceptable word,
        otherwise return False if the word is an uninteresting word.
    '''
    shortestlen = 3 #define shortest length allowed in word to make it more interesting
    #define list of non-interesting words for filtering
    noninterestingwords = ['THE','AND','SHE','HER', 'WAS', 'HIM', 'FOR', 'HAD', 'BUT','YOU'] 
    if len(word.strip()) < shortestlen or word.strip().upper() in noninterestingwords:
        return False
    return True

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
    wordsfrequency = {}
    with open(filepath, mode='r', encoding='UTF-8') as f:
        for line in f:
            finalline = ''
            for x in line:
                if x.isalpha():
                    finalline += x
                else:
                    #replace non-alpha with single space instead of empty to prevent potential words combination
                    #In case there are additional space found, the spaces shall be removed later
                    finalline += ' ' 
        
            if len(finalline.strip()) > 0: #only process the line if it's not empty
                words = finalline.split() #convert the line into words list
                # retrieve the final word and make sure to remove spaces if there are
                finalwords = [word.strip() for word in words if validateword(word)]
                countfrequency(wordsfrequency, finalwords)
    return wordsfrequency

def generateimage(wordsfreq):
    ''' To generate word cloud output in jpg format using wordcloud module '''
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordsfreq)
    cloud.to_file('sample_output.jpg') #output jpg file to current working directory

if __name__ == '__main__':
    print('Reading contents from sample.txt ...')  
    bf_timestamp = datetime.datetime.now().timestamp()
    # reading input file from current working directory
    wordsfreq = readingwords("sample.txt") 
    read_timestamp = datetime.datetime.now().timestamp()
    print('Contents processed ({} seconds)'.format(str(read_timestamp-bf_timestamp)))
    #print(wordsfreq)
    print('Generating image ...')
    generateimage(wordsfreq)
    generate_timestamp = datetime.datetime.now().timestamp()
    print('sample_output.jpg generated ({} seconds)'.format(str(generate_timestamp-read_timestamp)))
  

