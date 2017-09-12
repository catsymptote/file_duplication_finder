## Author: Catsymptote


#############
## Imports ##
#############

import os
import os.path
#from lib import file_manager
from lib import file_manager
#import file_manager



######################
## Global variables ##
#####################

dir_file = "dir_file.txt"

main_dir_1 = "#main_dir_1"
main_dir_2 = "#main_dir_1"
output_root_dir = "D:\\Projects\\Python\\file_duplication_finder\\_output"

match_dir_1 = output_root_dir + "\\match_dir_1"
match_dir_2 = output_root_dir + "\\match_dir_2"
non_match_dir_1 = output_root_dir + "\\non_match_dir_1"
non_match_dir_2 = output_root_dir + "\\non_match_dir_2"



#########################
## Directory functions ##
#########################

def set_main_directories(main_dir_one, main_dir_two):
    global main_dir_1
    global main_dir_2
    main_dir_1 = main_dir_one
    main_dir_2 = main_dir_two


def get_directories_from_file():
    global main_dir_1
    global main_dir_2
    global output_root_dir

    with open (dir_file) as f:
        dir_file_lines = f.readlines()
    dir_file_lines = [x.strip() for x in dir_file_lines]
    #print (dir_file_lines)
    #print (main_dir_1)
    #print (main_dir_2)
    #print (output_root_dir)
    make_dir_list_safe(dir_file_lines)
    main_dir_1 = dir_file_lines[0]
    main_dir_2 = dir_file_lines[1]
    output_root_dir = dir_file_lines[2]
    #print (main_dir_1)
    #print (main_dir_2)
    #print (output_root_dir)


def make_dir_list_safe(dir_list):
    for i in dir_list:
        # dir_list[0:1] instead of dir_list[i][0:1] due to "for i in dir_list:" and not "for i in range(len(dir_list)):".
        # The for is like this to avoid having to deal with len(dir_list) becoming smaller as indexes are deleted.
        if (dir_list[0:1] == '#' or dir_list[0:1] == '\n'):
            del dir_list[i]



###########################
## Safekeeping functions ##
###########################

def check_if_list_duplicates(a):
    # Taken from: https://stackoverflow.com/questions/1541797/check-for-duplicates-in-a-flat-list
    if (len(a) != len(set(a))):
        return True
    else:
        return False



##############################
## List searching functions ##
##############################

def return_matches(file_list_one, file_list_two):
    return (set(file_list_one) & set(file_list_two))


def return_matches_v2(file_list_one, file_list_two):
    return (set(file_list_one).intersection(file_list_two))


# Taken from: https://stackoverflow.com/questions/35713093/how-can-i-compare-two-lists-in-python-and-return-not-matches
def return_non_matches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]


def return_match_indexes(a, b):
    # Taken from: https://stackoverflow.com/questions/10367020/compare-two-lists-in-python-and-return-indices-of-matched-values
    return [i for i, item in enumerate(a) if item in b]


def return_non_match_indexes(a, b):
    # Taken from: https://stackoverflow.com/questions/10367020/compare-two-lists-in-python-and-return-indices-of-matched-values
    return [i for i, item in enumerate(a) if item not in b]


def return_unique_values(a):
    # Taken from: https://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list
    seen = set()
    #uniq = [x for x in a if x not in seen and not seen.add(x)]
    return [x for x in a if x not in seen and not seen.add(x)]




#############################
## File counting functions ##
#############################

def duplicate_counter():
    print ("First dir:\t" + main_dir_1)
    print ("Second dir:\t" + main_dir_2)
    print("Matches:\t" +
        str(len(return_matches(file_manager.get_all_file_names(main_dir_1),
            file_manager.get_all_file_names(main_dir_2)))))


def non_duplicate_counter():
    print("Unique:\t\t" + str(
        len(file_manager.get_all_file_names(main_dir_1)) + len(file_manager.get_all_file_names(main_dir_2))
        - len(return_matches(file_manager.get_all_file_names(main_dir_1), file_manager.get_all_file_names(main_dir_2)))
        ))



############################
## File copying functions ##
############################

def copy_non_duplicates_from_1():
    non_match_1 = return_non_match_indexes( file_manager.get_all_file_names(main_dir_1),
                                            file_manager.get_all_file_names(main_dir_2) )
    #
    for i in range(len(non_match_1)):
        old_path = file_manager.get_all_file_dirs(main_dir_1)[non_match_1[i]]
        new_path = non_match_dir_1 + "\\" + os.path.relpath(old_path, main_dir_1)
        file_manager.copy_file(old_path, new_path)


def copy_non_duplicates_from_2():
    non_match_2 = return_non_match_indexes( file_manager.get_all_file_names(main_dir_2),
                                            file_manager.get_all_file_names(main_dir_1) )
    #
    check_if_list_duplicates(file_manager.get_all_file_names(main_dir_1))
    check_if_list_duplicates(file_manager.get_all_file_names(main_dir_2))

    for i in range(len(non_match_2)):
        old_path = file_manager.get_all_file_dirs(main_dir_2)[non_match_2[i]]
        new_path = non_match_dir_2 + "\\" + os.path.relpath(old_path, main_dir_2)
        file_manager.copy_file(old_path, new_path)


def copy_duplicates_from_1():
    match_1 = return_match_indexes( file_manager.get_all_file_names(main_dir_1) ,
                                    file_manager.get_all_file_names(main_dir_2) )
    #
    for i in range(len(match_1)):
        old_path = file_manager.get_all_file_dirs(main_dir_1)[match_1[i]]
        new_path = match_dir_1 + "\\" + os.path.relpath(old_path, main_dir_1)
        file_manager.copy_file(old_path, new_path)


def copy_duplicates_from_2():
    match_2 = return_match_indexes( file_manager.get_all_file_names(main_dir_2),
                                    file_manager.get_all_file_names(main_dir_1) )
    #
    for i in range(len(match_2)):
        old_path = file_manager.get_all_file_dirs(main_dir_2)[match_2[i]]
        new_path = match_dir_2 + "\\" + os.path.relpath(old_path, main_dir_2)
        file_manager.copy_file(old_path, new_path)


"""
def copy_duplicates_old():
    print("hi")
    files = return_matches( file_manager.get_all_file_names(main_dir_1),
                                file_manager.get_all_file_names(main_dir_2))
    #
    for i in range(len(files[0])):
        file_manager.copy_file(
            os.path.join(main_dir_1, files[0][i]),
            os.path.join(copy_dir_1, files[0][i])
        )
    print ("hi again")
    for i in range(len(files[1])):
        file_manager.copy_file(
            os.path.join(main_dir_2, files[1][i]),
            os.path.join(copy_dir_2, files[1][i])
        )
"""

"""
    for i in range(len(match_1)):
        file_manager.copy_file(
            os.path.join(main_dir_1, files[0][i]),
            os.path.join(copy_dir_1, files[0][i])
        )

    for i in range(len(files[0])):
        file_manager.copy_file(
            os.path.join(main_dir_1, files[0][i]),
            os.path.join(copy_dir_1, files[0][i])
        )
    print ("hi again")
    for i in range(len(files[1])):
        file_manager.copy_file(
            os.path.join(main_dir_2, files[1][i]),
            os.path.join(copy_dir_2, files[1][i])
        )
"""



######################
## Launch functions ##
######################

#set_main_directories("E:\\__Paul\\Picture & Video\\Camera\Pictures",
#    "E:\\__Paul\\Picture & Video\\Camera\Backup\OP3\\_NoDate\\tmp_camera" )
#set_main_directories(   "E:\\__Paul\\Picture & Video\\Camera\\Pictures\\Annet\\obj_tmp_1",
#                        "E:\\__Paul\\Picture & Video\\Camera\\Pictures\\Annet\\obj_tmp_2")
get_directories_from_file()
duplicate_counter()
non_duplicate_counter()
"""
duplicate_counter()
copy_non_duplicates_from_1()
copy_non_duplicates_from_2()
copy_duplicates_from_1()
copy_duplicates_from_2()
"""
