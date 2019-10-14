# Finding duplicate files
-----------------------
catsymptote@gmail.com

This program looks in multiple (two) directories (and their subdirectories) after image files (or any files).
It checks the file names against each other (just the file names, not including the path), and finds:
	- Matches (copied from folder 1 or 2)
	- Non-matches from folder 1
	- Non-matches from folder 2

It then copies the chosen files to the _output folder in the program main directory.

Possibility for using hashes instead of file names may be included at a later stage.



## New method (GUI):
1.
Open the GUI.py file.

2.
If you want to change the input and output directories, click the relevant buttons, and change the directories.

3.
Click the relevant buttons to perform the different functionality.



## Old method (No GUI):
1.
Set the directories of the two folders (it is important which is which) in the "dir_file.txt".
	Do not change the line numbering (read the info in the dir_file)

2.
Chose which of these 3 functions the program will do by running one of the Python scripts in the main dir.

3.
Get the files from the "_output" folder in the main dir.
