# Python GUI with Tkinter
# Interaction with Checkboxes, entries ++
# Catsymptote


from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Checkbutton, Label
from tkinter import StringVar, IntVar

import sys
import os

from lib import file_duplication_finder


def get_directory():
    current_directory = filedialog.askdirectory()
    print (current_directory)
    sys.stdout.flush()


def change_dir_in_1():
    global dir_in_1
    global dir_in_1_var
    dir_in_1_var = filedialog.askdirectory()
    dir_in_1.set(dir_in_1_var)
    print("First input directory:\t" + str(dir_in_1_var))
    sys.stdout.flush()


def change_dir_in_2():
    global dir_in_2
    global dir_in_2_var
    dir_in_2_var = filedialog.askdirectory()
    dir_in_2.set(dir_in_2_var)
    print("Second input directory:\t" + str(dir_in_2_var))
    sys.stdout.flush()


def change_dir_out():
    global dir_out
    global dir_out_var
    dir_out_var = filedialog.askdirectory()
    dir_out.set(dir_out_var)
    print("Output directory:\t" + str(dir_out_var))
    sys.stdout.flush()



# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


#dir_in_1 = "Input folder 1"
#dir_in_2 = "Input folder 2"
#dir_out = "Output folder"

dir_in_1 = StringVar()
dir_in_1_var = file_duplication_finder.get_dirs()[0]
dir_in_2 = StringVar()
dir_in_2_var = file_duplication_finder.get_dirs()[1]
dir_out = StringVar()
dir_out_var = file_duplication_finder.get_dirs()[2]

dir_in_1.set(dir_in_1_var)
dir_in_2.set(dir_in_2_var)
dir_out.set(dir_out_var)


#file_duplication_finder.copy_non_duplicates_from_2


button_1 = Button(
    root_window,
    text="Matches from 1",
    command=file_duplication_finder.copy_duplicates_from_1
)

button_2 = Button(
    root_window,
    text="Matches from 2",
    command=file_duplication_finder.copy_duplicates_from_2
)

button_3 = Button(
    root_window,
    text="Differences from 1",
    command=file_duplication_finder.copy_non_duplicates_from_1
)

button_4 = Button(
    root_window,
    text="Differences from 2",
    command=file_duplication_finder.copy_non_duplicates_from_2
)


button_1.grid(columnspan=1, row=0, column=0)
button_2.grid(columnspan=1, row=0, column=1)
button_3.grid(columnspan=1, row=0, column=2)
button_4.grid(columnspan=1, row=0, column=3)


button_browse_in_1 = Button(
    root_window,
    text="Input folder 1",
    command=change_dir_in_1
)

button_browse_in_2 = Button(
    root_window,
    text="Input folder 2",
    command=change_dir_in_2
)

button_browse_out = Button(
    root_window,
    text="Output folder",
    command=change_dir_out
)

button_browse_in_1.grid(columnspan=1, row=1, column=0)
button_browse_in_2.grid(columnspan=1, row=2, column=0)
button_browse_out.grid(columnspan=1, row=3, column=0)


#label_in_1 = Label(root_window, text=dir_in_1)
#label_in_2 = Label(root_window, text=dir_in_2)
#label_out = Label(root_window, text=dir_out)

label_in_1 = Label(root_window, textvariable=dir_in_1)
label_in_2 = Label(root_window, textvariable=dir_in_2)
label_out = Label(root_window, textvariable=dir_out)

label_in_1.grid(columnspan=3, row=1, column=1, sticky=W)
label_in_2.grid(columnspan=3, row=2, column=1, sticky=W)
label_out.grid(columnspan=3, row=3, column=1, sticky=W)


# Stop ---------------
root_window.mainloop()
# Stop ---------------


print("-----<> Done <>-----")
#print(dir_in_1_var)
#print(dir_in_2_var)
#print(dir_out_var)
