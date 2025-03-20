def readHeShe():
    file = open('myfile.txt')
    data = file.read().split()
    
    cntHe = cntShe = 0
    for i in data:
        i = i.lower()
        if i == 'he':
            cntHe += 1
        elif i == 'she':
            cntShe += 1

    print('Frequency of "He" in file =', cntHe)
    print('Frequency of "She" in file =', cntShe)
    file.close()

readHeShe()
