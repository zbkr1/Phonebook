from os.path 
from CSV_creating import creating
from File_writing import writing_scv
from File_writing import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()