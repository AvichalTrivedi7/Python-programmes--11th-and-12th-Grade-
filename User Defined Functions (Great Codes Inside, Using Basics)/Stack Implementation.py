status = []

def Push_element(list1):
    status.append(list1)

def Pop_element():
    while len(status) > 0:
        print(status.pop())
    else:
        print('Stack Empty...')

for i in range(5):
    list1 = eval(input('Enter the list: '))
    Push_element(list1)

Pop_element()
