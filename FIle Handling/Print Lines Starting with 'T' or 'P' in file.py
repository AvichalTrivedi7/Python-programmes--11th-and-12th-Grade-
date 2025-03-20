def printData():
    f = open('myfile.txt')
    data = f.readlines()
    
    for line in data:
        if line[0] in ['t', 'T', 'P', 'p']:
            print(line)
    
    f.close()

printData()
