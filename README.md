# pyautomation
#### These are just Python sample programs (two versions) written with the purpose of demonstrating on how to apply Python programming concepts learnt from Google IT Automation with Python courses (both 'Crash Course on Python' and 'Using Python to Interact with the Operating System').
#### The main problem statements for the programs are to generate Word Cloud from a text file using Python module 'wordcloud' and other relevant modules. In fact, Word Cloud can be easily resolved by fully utilizing the functionality provided in 'wordcloud' module alone. However that's not the intention of these programs which are focusing on applying Python in planning and implementing the solution in accordance to the scope of the learning courses. There are many other ways and variants to resolve the problems.
* wordcloud_basic.py  
  This program shows the common way on how to apply the basic concepts to solve word cloud. The program reads a default input text file **(sample.txt)** from current working directory and output word cloud in jpg file **(sample.jpg)** in the same working directory. Replace the contents of the 'sample.txt' to try different text contents if necessary.
    * read line by line from a text file (sample.txt) in current working directory
    * filter out non alpha characters
    * validate words (filter out non-interesting words) and generate words list
    * Count words frequency and keep the counts in dictionary format
    * Call functions in 'wordcloud' module to process the data and generate word cloud image (sample.jpg) in the same working directory
    
* wordcloud_advance.py  
  This program further simplifies the program with more advanced concepts to solve word cloud. The program accepts text file name entered directly from user (through command line) and output word cloud in jpg file (based on file name provided in input) in the same working directory. There are more modules imported to process the contents with different techniques and handle some of the potential errors.
    * accept file name input from command line or prompt user to enter file name (file name in full or relative path)
    * read line by line from a text file name entered by user
    * filter out non alpha characters and words that do not meet minimum length using regular expressions
    * filter out non-interesting words and generate words list
    * Count words frequency and keep the counts in dictionary format
    * Call functions in 'wordcloud' module to process the data and generate word cloud image (based on file name provided by user) in the same working directory
