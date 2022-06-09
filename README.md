# Forg

Forg - Files Orgaiser 

This is a python script that organises your downloads folder (or any other folder you run it into) to  organised sub-folders.

This helps de-clutter the folders by setting folders with the date. This helps organise the day-to-day tasks by folders, to be easily found and stored. 

Forg can run as a scheduled task or manually. 

Command: python3 forg.py all (for all files to be moved automatically) or python3 forg.py <filename with extension> <filename2 with extension> ... (for specific files) 
  
This has the option to remove duplicate files, if it detects any. To enable this, uncomment lines 95 and 115. 
  
By default, Forg is set to create a folder called "Work" in the folder runned and in this folder create sub-folders with the date as name. The path can be changed though, by setting the static path (seen at the top of the script) 
