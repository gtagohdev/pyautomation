# Google IT Automation with Python   
The subject consists of 6 separate courses. Though all 6 courses were completed and certified, this repository site is only meant to share labs' results and references for those main and tricky labs that require manual planning, development, troubleshooting and testing.  
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
   
## Course-6: Automating Real-World Tasks with Python   
1. **course-6\transform_images.py**   
  Week-1 module lab is a program to read image files from a specific directory in relative to current working directory (user home), transform and save the images in the destinated directory. 
    * Read all image files from a specific directory
    * Convert to JPEG format; correct the rotation; resize to 128x128
    * Save the image files (jpeg) to a destinated directory
  
2. **course-6\run_upload_feedback.py**  
   Week-2 module lab (create and name the file as run.py as per the lab instruction) is a program to extract text contents from files; structure the data into json format and trigger existing feedback API service to upload the contents to the specific web site.
    * Read all text files from a specific directory
    * For each of the files, read the text line by line and generate the feedback contents in dictionary format
    * Trigger existing feedback API to upload the feedback contents in json format (converted from dictionary format) into a destinated web site 

3. **course-6\cars.py**   
   Week-3 module lab is an existing program that requires rectification and further customization in order to process car sales data; generate pdf report and deliver the report via email.
    * Fix data type error
    * Add a code block to generate a list of sales with car info (make, model and year)
    * Add a code block to generate a dictionary of car_year and total sales of the car_year
    * Sort the car info list in reverse order by sales and generate the summary of the top sales for the car
    * Sort the car_year dictionary in reverse order by total sales and generate the summary of the top total sales for car_year
    * Add code block to call existing reports function to generate pdf report
    * Add code block to call existing emails function to fire email and attach the pdf report

4. **course-6\reports.py**  
   This is the supporting program created for week-4 module lab. It provides functions to generate pdf report. 

5. **course-6\emails.py**  
   This is the supporting program created for week-4 module lab. It provides functions to fire email with or without attachment via local simple SMTP server.

6. **course-6\changeImage.py**   
   Week-4 module lab - task 1 is a program to transform all image files from tiff to jpeg format in the the same specific directory.
    * Read all image files from a specific directory in relative to current working directory (user home)
    * Convert each image to jpeg format
    * Resize jpeg image to 600x400 and save the jpeg file (same file name with jpeg extension) in the same directory as the original image file
   
7. **course-6\supplier_image_upload.py**   
   Week-4 module lab - task 2 is a program to upload every jpeg file generated in a specific directory to a destinated web site via API service call.
    * Read all jpeg image files from a specific directory in relative to current working directory (user home)
    * Upload each of the files to a destinated web site via API service call with file attachment

8. **course-6\run_upload_descriptions.py**  
   Week-4 module lab - task 3 is a program to extract product data files from a specific directory and upload products information to a destinated web site for displaying.
    * Read all text files from a specific directory in relative to current working directory (user home)
    * For each of the files, read the text line by line and generate the products information (dictionary format) that include the respective jpeg image path
    * Trigger existing fruits API to upload the products information as json format (converted from dictionary format) into a destinated web site 
 
9. **course-6\report_email.py**  
   Week-4 module lab - task 4 is a program to generate a report of products information in pdf format and deliver the report as attachment via email.
    * Read and process products data from text files in relative to current working directory (user home)
    * Prepare products information in the requested format
    * Invoke function from reports.py module to generate pdf report in a specific directory
    * Invoke function from emails.py module to delivery the pdf report as attachment via email 

10. **course-6\health_check.py**  
   Week-4 module lab - task 5 is a program to perform health checks on a system and fire alert to user via email whenever any of the unhealthy conditions is met.
    * Retrieve memory information, validate and fire email alert only when memory free space is lower than 500MB
    * Retrieve disk usage information, validate and fire email alert only when disk free space percent is lower than 20%
    * Retrieve ip information from localhost and fire email alert only when locahost is not resolvable to default local IP 127.0.0.1
    * Retrieve CPU usage information, validate and fire email alert only when CPU utilization exceeds 80% threshold
    






