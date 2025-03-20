def checkList(l):
    return min(l), max(l), sum(l) / len(l)

marks = eval(input('Enter the marks of students: '))
minList, maxList, avgList = checkList(marks)

print('MAXIMUM MARKS:', maxList)
print('MINIMUM MARKS:', minList)
print('AVERAGE MARKS:', avgList)
