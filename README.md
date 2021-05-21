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

## Installations  
1. Ensure that Python interpreter (3.9.x) had been installed locally
2. Download zip of all files from the repository and unzip to a local directory (e.g: d:\pyautomation-main)
    * https://github.com/gtagohdev/pyautomation/archive/refs/heads/main.zip 
4. Use command prompt windows and change direcotry to the specified directory
5. Install wordcoud python module by running the command:  
    * pip install wordcloud  
6. However the above command may encounter errors in Windows platform (with Python 3.9.x installed). If this is the case, for workaround just run the following command:  
    * pip install wordcloud-1.8.1-cp39-cp39-win_amd64.whl
8. Once 'wordcloud-1.8.1' and the relevant modules are installed properly, you can proceed to program execution.  

## Executions
1. Use command prompt in Windows or Ubuntu and change direcotry to the specified directory (e.g: d:\pyautomation-main or /home/user/pyautomation-main)
2. To run wordcloud_basic.py in command line and check the print out on the screen and look out for output file (sample.jpg) and open it
    * for Windows: wordcloud_basic.py
    * for Ubuntu: ./workcloud_basic.py
4. To run wordcloud_advance.py in command line and check the print out on the screen and look out for output file (xxxxx.jpg) and open it
    * for Windows: wordcloud_advance.py and enter the file name (e.g: sample.txt which found in the same working directory) when prompted
    * or for Windows: wordcloud_advance.py sample.txt
    * try using other file name such as d:\otherfolder\otherfile.txt
    * for Ubuntu: ./wordcloud_advance and enter the file name (e.g: sample.txt which found in the same working directory) when prompted
    * or for Ubuntu: ./wordcloud_advance sample.txt
    * try using other file name such as /home/user/otherfolder/otherfile.txt
 5. Try using other invalid file name or other file format to see the errors generated from the programs.

### Sample screenshot of executions:  
![Sample execution image](https://github.com/gtagohdev/pyautomation/blob/main/sample_execution.png)  

### Sample output image:
![Sample output image](https://github.com/gtagohdev/pyautomation/blob/main/sample_output.jpg)  


