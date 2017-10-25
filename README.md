## Text extraction automation process in  .py\
\
Small module written in Python used for automation of a document cleaning and text extracting process. For a purpose of having a learning corpus for a Spanish-English contract translation application (IBM Watson Language Translator API), we needed a large amount of text. As a base we used samples of real contracts in pdf or docx, all with contract-specific terms. The model was learning from the text that was generated from these contracts to learn the right sentence constructions. Alongside this corpus we used the dictionary of Spanish-English terms for the correct translation of which offers higher level of customisation.\
 \
### The steps: \
1. rename.sh/replace.py - cleaning file names\
1. merging.py - merging data format specific files into one single file\
1. extracttxt.py - extracting text from these new merged files
