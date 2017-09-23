## Author: Catsymptote


#############
## Imports ##
#############

import os
import os.path
from os import listdir
import sys
from shutil import copyfile



def get_all_file_dirs(directory):
    directory
    file_list = []
    # Loops taken from: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_list.append(os.path.join(path, name))
    #print (len(file_list))
    #print (file_list)
    return file_list


def get_all_folder_dirs(directory):
    #directory
    file_list = []
    # Loops taken from: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    for path, subdirs, files in os.walk(directory):
        for name in subdirs:
            file_list.append(os.path.join(path, name))
    #print (len(file_list))
    #print (file_list)
    return file_list


def get_all_file_names(directory):
    directory
    file_list = []
    # Loops taken from: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_list.append(os.path.basename(name))
    #print (len(file_list))
    #print (file_list)
    return file_list


def ensure_dir(file_path):
    new_directory = os.path.dirname(file_path)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)


def copy_file(old_file, new_file):
    ensure_dir(new_file)
    #print(os.path.isdir("E:\__Paul\Picture & Video\Camera\Backup\OP3\_NoDate\_tmp_tmpCam"))
    if (not os.path.exists(new_file)):
        copyfile(old_file, new_file)
    #else:
        # Same, but add a (number) before the file extension?
        # (Actually, prob not because full URLs)
        #print ("File already exists")



#get_all_file_dirs("E:\__Paul\Picture & Video\Camera\Pictures\Annet\Objects")
#get_all_folder_dirs("E:\__Paul\Picture & Video\Camera\Pictures\Annet\Objects")
