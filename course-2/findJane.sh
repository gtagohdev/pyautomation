#!/bin/bash
# create empty olfFiles.txt file in current working directory
> oldFiles.txt
# grep list of applicable file names only from the given file
files="$(grep ' jane ' ../data/list.txt | cut -d' ' -f3)"
echo $files

# Correct each file name line by adding user home directory in prefix of file name.
# Validate actual file existence and save the file name line to oldFiles.txt
for fileName in $files
  do
    # prefix file name with user home directory as full absolute path name
    relFileName="$(echo ~)$fileName"
    echo $relFileName
    # Verify file existence in file system and only output applicable file name to oldFiles.txt
    if test -e $relFileName; then echo "$relFileName" >> oldFiles.txt; else echo not_found; fi

  done

