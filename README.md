# Downloads-organizer(b01jan)
 I made this project for the purpose of organizing my Donwloads-folder.
 The script creates several folders in Downloads and moves files with specific extensions to their corresponding folder.
 Folders that are downloaded are also automaticly moved to the 'FOLDERS' folder.
 The script is very easy to addapt to suit your needs, so feel free to tinquer with it.
 
 I recommend using .exe version of the script, which can easily be made with pyinstaller.
 I personnally put the .exe file in my startup folder so that it automaticly organizes my files when I log in on my computer (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp).
 
 Based on suggestions, I made an exe version of the script which organizes the direcotry where the organize_local_directory.exe is located  so that it can easily be used on any folder.
 
 This is my first project to be posted on github. So please adjust your expectations accordingly :) .
 
## Requirements(b01jan)
 The script only uses standard python modules so there is no need to install aditional modules.
 The script itself requires a Python interpreter to run. I normally run it in my IDE.
 
## How to use(b01jan, chloro)
Change the directory_path variable in the organizer.py script and then run the script anyway you see fit.

You can use a simple GUI application from main.py, also available from the execution.(chloro)

 
## Important(b01jan)
 Depending on the size of your (Downloads-) folder it can take quite a while for all the files to move/organize during the first run. Don't terminate the script while it's running because that may corrupt some of your files.

## Changes(chloro)

Changed the directory_path which was hard corded originally into the downloads path.

Moved the directory dictionary to another python file .

Made an GUI app using flet(main.py).

Made the filtering to cover more programming language(e.g. javascript) and other minor changes.
