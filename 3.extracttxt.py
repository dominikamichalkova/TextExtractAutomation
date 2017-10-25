#extracting text from .docx and .pdf files (that were creating by mergin all contract files of the same file format) and store it in .txt file
import fileinput
import os
import Tkinter, tkFileDialog
import docx
import PyPDF2


root = Tkinter.Tk()
root.withdraw()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory with your merged files')
os.chdir(dirname)
print os.getcwd()

filenames = os.listdir(dirname)

infile = '.\combinedocs.docx'
outfile = '.\docx2txt.txt'

document = docx. Document(infile)

for p in document.paragraphs:
    text = p.text.encode('utf-8')
    f = open(outfile, 'a')
    f.write(text)
    f.close()

#extracting text from .pdf file and store it in .txt file

pdfFile = open('.\combinedpdfs.pdf','rb');
pdfReader = PyPDF2.PdfFileReader(pdfFile)
numpages = pdfReader.numPages
print "%s" %(str(numpages))

i = 0
for i in range(0,numpages):
    page = pdfReader.getPage(i)
    text = page.extractText().encode('utf-8')
    f = open('.\pdf2txt.txt','a') #'a' parameter = append mode; 'w' mode would overwrite everything what is already in file
    # print text
    f.write(text)
    f.close()

#remove blank lines in the output file
for line in fileinput.FileInput('.\pdf2txt.txt',inplace=1):
    if line.rstrip():
        print line


# script to split text into multiple smaller ones

split = 20000  #n-th line when split occurs
smallfile = None
i=0

files = os.listdir(os.getcwd())

#crete new dir to store monolingual corpus files - final stage
outputdir = '..\monolingualCorpus'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

for file in files:
    if file.endswith(".txt"):
        with open(file) as bigfile:
            for linenumber, line in enumerate(bigfile):
                if linenumber % split == 0:
                    if smallfile:
                        i+=1
                        smallfile.close()
                    multiling_file = os.path.join(outputdir,'monoling_file_{}.txt'.format(i))
                    smallfile = open(multiling_file, "w")
                smallfile.write(line)
            if smallfile:
                smallfile.close()