import pickle

file = open('myBinaryFile2.bin', 'wb+')

def inputData():
    ans = 'y'
    while ans == 'y':
        data = eval(input('Enter the name, roll number, and marks of student: '))
        pickle.dump(data, file)
        file.flush()
        ans = input('Want to enter more data? (y/n): ').lower()

def updateMarks():
    file.seek(0)
    try:
        rno = int(input('Enter the roll number to search: '))
        newMarks = int(input('Enter new marks: '))

        temp_list = []
        found = False
        
        while True:
            try:
                pos = file.tell()
                data = pickle.load(file)
                if data['roll number'] == rno:
                    data['marks'] = newMarks
                    found = True
                temp_list.append(data)
            except EOFError:
                break
        
        file.seek(0)
        file.truncate()
        for record in temp_list:
            pickle.dump(record, file)

        if found:
            print('Marks updated successfully!')
        else:
            print('Roll number not found.')

    except Exception as e:
        print("Error:", e)

def show():
    file.seek(0)
    try:
        while True:
            data = pickle.load(file)
            print(data)
    except EOFError:
        file.close()

# Main execution
inputData()
updateMarks()
show()
