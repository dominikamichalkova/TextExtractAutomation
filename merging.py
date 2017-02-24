#Script to merge pdf and docx

import time
import os
from PyPDF2 import PdfFileMerger,PdfFileReader

os.chdir('.\contract_files')
path = os.getcwd()
print path

pdfs = [f for f in os.listdir(path) if f.endswith('pdf')] #if condition necessary

merger = PdfFileMerger()

for filename in pdfs:
    merger.append(PdfFileReader(os.path.join(path,filename),'rb'))

merger.write('..\combinedfiles\combinedpdfs.pdf') #must be not indented

print "Merging all documents in directory took: ", time.time() - start, "sec"

# v.02 works too
# merger = PdfFileMerger()
# i = 0
# print len(pdfs)
# for i in range(0, len(pdfs)):
#     merger.append(PdfFileReader(os.path.join(path, pdfs[i]), 'rb'))
# merger.write('..\combinedfiles\combinedpdfs.pdf')



start = time.time()

files = glob.glob(".\contract_files\*.docx")
print files

output = '.\combinedfiles\combinedocs.docx';
input = files;

def text_from_docx(path):

    doc = docx.Document(path)
    for paragraph in doc.paragraphs:
        yield paragraph.text

combined_doc = docx.Document()
for file_path in input:
    for text in text_from_docx(file_path):
        combined_doc.add_paragraph(text)
        #if not file_path is DOCUMENTS_TO_COMBINE[-1]:
            #combined_doc.add_page_break()
        combined_doc.save(output)
