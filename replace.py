import os
import regex

os.chdir('C:\Users\Dominika\Documents\doc')
path = os.getcwd()
filenames = os.listdir(path)

old="doc"
new="docx"

for file in filenames:
    if file.endswith('.doc'):
        print file
        newname=file.replace(old,new)
        os.rename(file,newname)
        print newname
    else:
        print "There are no .doc files"

for file in filenames:
        if regex.search("[^a-zA-Z0-9\.]",file):
            name = regex.sub('[^0-9a-zA-Z\.]', '',file)
            change=file.replace(file,name)
            os.rename(os.path.join(path,file),os.path.join(path,change))
            print name