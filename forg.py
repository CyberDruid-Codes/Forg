#!/usr/bin/env python3

# Made by Daud Jawad
# Made to help cleanup the folders of attachments, files and so on. This could be used as a scheduled task (service)

# This tool move multiple files in one go.
# Just run the command -> python3 forg.py all  - to move all files from the current directories
# Run the command -> python3 forg.py <filename with extension> <second filename with extension> ... - to move specific files
# This has the option to remove duplicate files it detects. To enable this option, uncomment line 95 and 115.
# This will create a folder in the place where it was runned from but if you would like to set a custom path, modify "path_tomove" - line 28 (comment line 26)

#Importing Section
#
import os
import shutil 
import sys 
import datetime
import glob
#

# Initialising the needed objects
files = sys.argv
files_length = len(files) - 1
currentfiles_path = os.path.dirname(os.path.abspath(__file__))+"\\"
# Dynamic path (Creates the folder wherever you run the script)
path_tomove = os.path.dirname(os.path.abspath(__file__))+"\\"+ "Work"+"\\"
# Static Path - can add your custom path, where all the files will be moved to
# path_tomove = "C:\\Users\\path\\to\\moveto\\"
#

# Method to get the name for the folder ( i.e. current day and month )
def date():
    dt = datetime.datetime.now()
    month = '{:02d}'.format(dt.month)
    day = '{:02d}'.format(dt.day)
    folder_date = str(month) +"-"+ str(day)
    return folder_date
#

# Method to check if the folder is there and creating if it is not
def createfolder():

    newpath = path_tomove + date()
    if not os.path.exists(newpath):
        os.makedirs(newpath)
#

# If file already exists, it will be removed
def fileExists(movingpath, inputpath, allinput):
    
    if allinput == True:
        x=len(inputpath) - 1
        tempath = ""

        # takes the input (full path of the file, currently) and selects the file name
        while inputpath[x] != "\\":
            tempath += inputpath[x]
            x -= 1
        
        # Reverses the inputpath and adds it to the what would be the path to move
        finalpath = movingpath + tempath[::-1]

    elif allinput == False: 
        finalpath = movingpath + inputpath

    # Checks if the file is already existing there. If it is, it returns True
    if os.path.exists(finalpath):
        return True
    else: 
        return False
#

# Checks if an input was given ( All or the files to be moved )
if files_length > 0:

    # If the all parameter is given, it will move all files in the current path 
    if files[1] == "all":

        # Checks the files in the current path and adds the name into an array
        files = glob.glob(str(currentfiles_path)+"*")
        files_length = len(files)-1
        
        if len(files)>2:   
            
            # Creates a folder
            createfolder()

            print("All files in the current directory will be moved."+"\nFiles Found: "+str(files_length))
            # While loop that runs until no more input is available in the array. (Omits the script) 

            while files_length >= 0:
                # Ignores files in a folder (In this case, forg script and the "Work" folder we created) - If more files need to be ignored, they can be added using the same syntax
                if files[files_length] != str(currentfiles_path)+"forg.py" and files[files_length] != str(currentfiles_path)+"Work":
                    # Checks if the files exist in the path given (folder with date)
                    if fileExists(path_tomove+str(date())+"\\",str(files[files_length]),True)==False:
                        try:
                            # Moves the file to the location
                            shutil.move(files[files_length], str(path_tomove+str(date())))
                        except:
                            # If the previous step fails, this will show what file could not be moved. 
                            # This can happen if the location is non-existant/reachable/script does not have the right permissions
                            print("File: "+ str(files[files_length])+" could not be moved.")
                            pass
                    else:
                        try:
                            # If the file already exists at the location, a message is displayed. The line below can remove the duplicates. 
                            print("File: "+ str(files[files_length])+" already exists at the location.")
                            #os.remove(files[files_length])
                        except: 
                            pass
                files_length -=1
        else:
            print("No new files to move in the current directory.")
    else:

        # Creates a folder
        createfolder()

        # If Inputs are given (i.e. multiple files, it will move them to the given path)
        print("This is how many files will be moved: "+str(files_length))

        while files_length >= 0:
            if files[files_length] != "forg.py" and files[files_length] != "Work":
                if fileExists(path_tomove+str(date())+"\\",str(files[files_length]),False)==False:
                    try:
                        shutil.move(str(currentfiles_path+files[files_length]), str(path_tomove+str(date())+"\\"+files[files_length]))
                    except:
                        print("File: "+ str(files[files_length])+" could not be moved.")
                        pass
                else: 
                    try:
                        print("File: "+ str(files[files_length])+" already exists at the location.")
                        #os.remove(files[files_length])
                    except: 
                        pass
            files_length -=1
else:

    # If no files are given or inputs, it will return the explanation why it failed
    print("There is no input. Please type all if you want all files from the current directory to be moved, otherwise give the names individually.")
#