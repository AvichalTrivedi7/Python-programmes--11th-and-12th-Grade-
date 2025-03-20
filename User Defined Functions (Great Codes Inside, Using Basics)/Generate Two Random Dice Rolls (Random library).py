import random

def rolladice():
    myList = []
    for _ in range(10):
        randomNumber1 = random.randint(1, 6)
        randomNumber2 = random.randint(1, 6)
        myList.append(randomNumber1 + randomNumber2)
    return myList

print(rolladice())
