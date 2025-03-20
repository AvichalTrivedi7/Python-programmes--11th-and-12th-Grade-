def LinearSearch():
    list1 = eval(input('Enter the list of elements: '))
    element = eval(input('Enter the element to search: '))
    
    if element in list1:
        print('Element found in position', list1.index(element) + 1)
    else:
        print('Element not found..')

LinearSearch()
