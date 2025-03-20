import csv

def readCSV():
    file = open('saurav2.csv', newline='\n')
    readerObj = csv.reader(file)

    for i in readerObj:
        if i[2].isdigit() and 500 <= float(i[2]) <= 1000:
            print(i[1])

    file.close()

readCSV()
