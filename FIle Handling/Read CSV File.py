import csv

def readCSV():
    file = open('saurav.csv', newline='\n')
    readerObj = csv.reader(file)
    
    for i in readerObj:
        print(i)
    
    file.close()

readCSV()
