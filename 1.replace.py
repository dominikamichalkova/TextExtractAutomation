#Python script to rename file names that contain blank spaces and other special characters and replace them
#alternative = script.sh which must be placed in a folder with files you want change their names for

import os
import regex
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory with your files')
os.chdir(dirname)
print os.getcwd()

filenames = os.listdir(dirname)

for file in filenames:
        if regex.search("[^a-zA-Z0-9\.]",file):
            print file
            name = regex.sub('[^0-9a-zA-Z\.\_\-]', '',file)
            change=file.replace(file,name)
            os.rename(os.path.join(dirname,file),os.path.join(dirname,change))
            print name