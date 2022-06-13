# Forg

Forg - Files Orgaiser 

This is a python script that organises your downloads folder (or any other folder you run it into) to  organised sub-folders.

This helps de-clutter the folders by setting folders with the date. This helps organise the day-to-day tasks by folders, to be easily found and stored. 

Command: python3 forg.py all (for all files to be moved automatically) or python3 forg.py filename1.png filename2.pdf ... (for specific files) 
  
This has the option to remove duplicate files, if it detects any. To enable this, uncomment lines 95 and 115. 
  
By default, Forg is set to create a folder called "Work" in the folder runned and in this folder create sub-folders with the date as name. The path can be changed though, by setting the static path (seen at the top of the script) 

Forg can run as a scheduled task or manually. Example: Task Scheduler in Windows. 
Steps:
1. Create a Task and name it acordingly
2. Set the Schedule to run once a day (at a certain time) 
3. Actions - Set the action to "Start a program"
3.1. For the Script, browse for the python executable
3.2. Arguments - Set it to "forg all" 
3.3. Start in - Set it to the path where the forg.py script resides (Generally, Downloads)
4. In General, set the task to run only when the user is logged in

Thank you!
