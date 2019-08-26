# Create a named folder using windows/linux 'mkdir' command
# Python 3 program
# Author: Munshi Muzahid Hasan Tushar
# Date: 26 August, 2019
# Version: alpha 1.0 (Tkinter GUI)

import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.messagebox import *



root = tkinter.Tk()
root.withdraw() # To hide Tkinter window
root.iconbitmap(default=r'location_of_the_script\favicon.ico') # Tkinter custom icon, default will change icon in simpledialog also
CurrDir = os.getcwd() # To get the base dir

SelectDir = filedialog.askdirectory(parent=root, initialdir=CurrDir, title='Please select a directory') # Prompt to select the directory
messagebox.showinfo("Selected Directory",SelectDir) # Showing selected direcory in information messagebox
os.chdir(SelectDir) # Changing to selected directory


FolderName = simpledialog.askstring(title='Create new folder', prompt='Enter folder name:') # New folder creation prompt
CreatedFolder = os.mkdir(FolderName)
messagebox.showinfo("Folder Created!",FolderName) # Success infomation messagebox
