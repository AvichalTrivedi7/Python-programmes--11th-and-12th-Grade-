list1 = eval(input('Enter elements of list1: '))
list2 = eval(input('Enter elements of list2: '))
list_merged = list1 + list2
print("New list is:", list_merged)
list_merged.sort()
print("The list in sorted manner is: ", list_merged)
print("Element having Maximum value is: ", list_merged[len(list_merged)-1])
print("Element having minimum value is: ", list_merged[0])
print('elements on odd indexing are:')
for i in range(len(list_merged)):
    if i % 2 != 0:
        print(list_merged[i])
