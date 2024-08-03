# Project Name: Names and burthdates 

The code processes a text file named "DOB.txt" that contains names and birthdates. The code extracts and displays the names and birthdates separately.

## Functionality

File Path Storage: The code starts by storing the file path of "DOB.txt" in the FILE_PATH variable.
File Reading: The file is opened in read mode ('r') using UTF-8 encoding. The readlines() method reads all lines from the file into the DOB_INFO list.
Name Processing: The code iterates through each line in DOB_INFO. It splits each line into words using split(), then combines the first two words (assumed to be the name and surname) using join(). The combined names are printed.
Birthdate Processing: The code iterates through DOB_INFO again. It splits each line into words and combines all words from the third word onwards (assumed to be the birthdate). The combined birthdates are printed.

## Example

If "DOB.txt" contains:

John Doe 01/01/2000
Jane Smith 12/31/1995

## The output would be:

Name:John Doe
Name:Jane Smith

Birthdate:01/01/2000
Birthdate:12/31/1995
