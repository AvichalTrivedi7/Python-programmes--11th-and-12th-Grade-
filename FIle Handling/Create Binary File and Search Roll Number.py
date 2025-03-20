import pickle

file = open('myBinaryFile.bin', 'ab+')

def inputData():
    ans = 'y'
    while ans == 'y':
        data = eval(input('Enter name and roll number: '))
        pickle.dump(data, file)
        file.flush()
        ans = input('Want to enter more data? Press Y or N: ').lower()

def searchData():
    file.seek(0)
    found = False
    rno = int(input('Enter roll number to search: '))
    
    try:
        while True:
            data = pickle.load(file)
            if data['roll number'] == rno:
                found = True
                print('ROLL NUMBER =', rno, 'AND NAME =', data['name'])
    except:
        if found:
            print('Data found..')
        else:
            print('Data not found..')
    
    file.close()

inputData()
searchData()
