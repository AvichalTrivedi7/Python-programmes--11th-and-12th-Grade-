f = open('myfile.txt')

def show():
    try:
        while True:
            data = f.readline().split()
            for i in data:
                print(i, '#', end='')
    except:
        f.close()

show()
