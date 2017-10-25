#extracting text from .docx and .pdf file and store it in .txt file
import docx
import PyPDF2
import fileinput

infile = '.\combinedfiles\combinedocs.docx'
outfile = '.\combinedfiles\docx2txt.txt'

document = docx. Document(infile)

for p in document.paragraphs:
    text = p.text.encode('utf-8')
    f = open(outfile, 'a')
    f.write(text)
    f.close()
    
pdfFile = open('C:\Users\IBM_ADMIN\PycharmProjects\STStransl-auto\combinedfiles\combinedpdfs.pdf','rb');
pdfReader = PyPDF2.PdfFileReader(pdfFile)
numpages = pdfReader.numPages
print "%s" %(str(numpages))

i = 0
for i in range(0,numpages):
    page = pdfReader.getPage(i)
    text = page.extractText().encode('utf-8')
    f = open('.\combinedfiles\pdf2txt.txt','a') #'a' parameter = append mode; 'w' mode would overwrite everything what is already in file
    # print text
    f.write(text)
    f.close()

#remove blank lines in the output file
for line in fileinput.FileInput('.\combinedfiles\pdf2txt.txt',inplace=1):
    if line.rstrip():
        print line


# script to split text into multiple smaller ones

split = 35000  #n-th line when split occurs
smallfile = None
i=0

with open('.\combinedfiles\pdf2txt.txt') as bigfile:
    for linenumber, line in enumerate(bigfile):
        if linenumber % split == 0:
            if smallfile:
                i+=1
                smallfile.close()
            multiling_file = '.\multilingualCorpus\multiling_file_{}.txt'.format(i)
            smallfile = open(multiling_file, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()
