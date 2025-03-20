import csv

file = open('saurav3.csv', 'a+', newline='\n')

def writeCSV():
    writerObj = csv.writer(file)
    writerObj.writerow(['user-id', 'password'])
    
    ans = 'y'
    while ans == 'y':
        uid = input('Enter user id: ')
        pwd = input('Enter password: ')
        writerObj.writerow([uid, pwd])
        file.flush()
        ans = input('Want to add more info? (y/n): ').lower()

    print('Data saved successfully..')

def search():
    file.seek(0)
    uid = input('Enter the user ID to search: ')
    readerObj = csv.reader(file)

    for i in readerObj:
        if i[0] == uid:
            print('Password:', i[1])

writeCSV()
search()
file.close()
