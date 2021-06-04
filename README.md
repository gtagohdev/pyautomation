# Google IT Automation with Python   
## Course-1: Crash Course on Python   
These are just Python sample programs (two versions) written with the purpose of demonstrating on how to apply Python programming concepts learnt from the course. The main problem statements for the final project lab (Week-6) of the course are to generate Word Cloud from a text file using Python module 'wordcloud' and other dependent modules. In fact, Word Cloud can be easily resolved by fully utilizing the functionality provided in 'wordcloud' module alone. However that's not the intention of the programs, which are focusing on applying Python to solve the solution based on the scope of the learning course. Of course there are many other ways and variants to resolve the problems.
1. **course-1\wordcloud_basic.py**  
  This program shows the common way on how to apply the basic concepts to solve word cloud. The program reads a default input text file **(sample.txt)** from current     working directory and output word cloud in jpg file **(sample.jpg)** in the same working directory. Replace the contents of the 'sample.txt' to try different text     contents if necessary.
    * read line by line from a text file (sample.txt) in current working directory
    * filter out non alpha characters
    * validate words (filter out non-interesting words) and generate words list
    * Count words frequency and keep the counts in dictionary format
    * Call functions in 'wordcloud' module to process the data and generate word cloud image (sample.jpg) in the same working directory
    
2. **course-1\wordcloud_advance.py**  
  This program further simplifies the program with more advanced concepts to solve word cloud. The program accepts text file name entered directly from user (through command line) and output word cloud in jpg file (based on file name provided in input) in the same working directory. There are more modules imported to process the contents with different techniques and handle some of the potential errors.
    * accept file name input from command line or prompt user to enter file name (file name in full or relative path)
    * read line by line from a text file name entered by user
    * filter out non alpha characters and words that do not meet minimum length using regular expressions
    * filter out non-interesting words and generate words list
    * Count words frequency and keep the counts in dictionary format
    * Call functions in 'wordcloud' module to process the data and generate word cloud image (based on file name provided by user) in the same working directory

#### Installations  
1. Ensure that Python interpreter (3.9.x) had been installed locally
2. Download zip of all files from the repository and unzip to a local directory (e.g: d:\pyautomation-main)
    * https://github.com/gtagohdev/pyautomation/archive/refs/heads/main.zip 
4. Use command prompt windows and change direcotry to the specified directory
5. Install wordcoud python module by running the command:  
    * pip install wordcloud  
6. However the above command may encounter errors in Windows platform (with Python 3.9.x installed). If this is the case, for workaround just run the following command:  
    * pip install wordcloud-1.8.1-cp39-cp39-win_amd64.whl
8. Once 'wordcloud-1.8.1' and the relevant modules are installed properly, you can proceed to program execution.  

#### Executions
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

#### Sample screenshot of executions:  
![Sample execution image](https://github.com/gtagohdev/pyautomation/blob/main/sample_execution.png)  

#### Sample output image:
![Sample output image](https://github.com/gtagohdev/pyautomation/blob/main/sample_output.jpg)   


## Course-2: Using Python to Interact with the Operating System   
The last two main labs (week-6 and week-7) found in the coourse are the hands on labs that require learner to write the scripts from scratch. There might be a bit tricky for novice learner as the instructions and questions were not structured properly. Pay more attentions on every detail and the patterns of the contents given in the files.
1. **course-2\findJane.sh**  
   This is part of Week-6 end lab to correct, validate and save applicable file names in output file (oldFiles.txt).  
    * Create empty olfFiles.txt file in current working directory
    * Grep a list of applicable file names only from the given file (list.txt)
    * Correct each applicable file name by adding user home directory in prefix of file name.
    * Validate file existence in the actual file system and save the applicable file name (full absolute path) to oldFiles.txt  
 
2. **course-2\changeJane.py**  
   This is also part of week-6 end lab to perform actual file renaming in file system based on the applicable file name given in the file (oldFiles.txt).
    * Accept input file from command line (assume that oldFiles.txt to be supplied as command line parameter to the program)
    * Read each line from the file and rename any occurence of 'jane' to 'jdoe' that found in the file name
    * Perform the actual file renaming in the file system
 
3. **course-2\ticky_check.py**  
   This is the main programa for week-7 final project lab of the course.  
    * Define search patterns with results grouping (# 1 - log type (INFO or ERROR), # 2 - error description, # 3 - user nameourse) 
    * Read line by line from syslog.log (assume the file found in current working directory)
    * Based on the search results, keep the error statistics (error desc & count) in dictionary variable
    * Based on the search results, keep the user statistics (user name, count of INFO and count of ERROR) in dictionary variable
    * Sort error statistics values in its variable
    * Sort user statistics values in its variable
    * Save error statistics to error_message.csv file using csv common functionality
    * Save user statistics to user_statistics.csv file using csv DictWriter functionality     
      
  Then follow other instructions in the lab to convert csv files into html files for report page displaying via browser.    
  
## Course-4: Troubleshooting and Debugging Techniques   
1. **course-4\dailysync.py**   
   A sample program (week-2 module lab) utilizes rsync tool in Linux platform to perform delta backup recursively at directory level. Performance of the processes can be adjusted or fine-    tuned via parallel processing feature provided by multiprocessing module.
    * This program only processes backup directories in relative to the default working directory (home) 
    * Determine source and target root directory for backup
    * Read first level subdirectory names based on the given root directory to backup from.
    * Use multiprocessing Pool module functionality to perform delta copying on each subdirectory parallelly
    * Use rsync command to backup delta at the given directory recursively  

2. **course-4\start_date_report.py**   
   A sample program (week-4 module lab) to demonstrate problem troubleshooting, performance fine-tuning and modification techniques. Rectifications and            improvements are mainly required in existing and new methods.
    * Method get_start_date() - Rectify type conversion problem for values entered (from str to int)
    * New method getsortedemployees() - To pre-process employees data (read csv rows into lists and order by date column) for subsequent use
    * Method get_same_or_newer(start_date, employees) - Remove unnecessary processes. Search and filter out results to a final list based on date column 
    * Method list_newer(start_date) - Remove unnecessary processes. Generate and print final employees list report based on the input date
   
   
