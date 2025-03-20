def copyData():
    f = open('myfile.txt')
    f2 = open('myfile2.txt', 'w+')
    data = f.readlines()

    for line in data:
        if 'A' not in line and 'a' not in line:
            f2.write(line)
            f2.flush()

    f2.seek(0)
    print(f2.read())
    f.close()
    f2.close()

copyData()
