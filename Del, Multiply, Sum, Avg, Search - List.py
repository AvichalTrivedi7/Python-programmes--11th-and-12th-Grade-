list=eval(input("Enter the list   :"))
print("this is the list you have input  :",list)
del list[1:4] #To delete elements from index 1 to 4
print(list)
print("\n")

for i in range(0,len(list)):
    print(list[i],end=" ") #this is the way to print the list
print("\n")

list2=[29,40,50,28,58,75,'ok']
for i in list2:
    print(i,end=" ") #this is the way to print the indices till the end of the list
print("\n")

multiply=list2*5 
print(multiply) #to repeat the list 5 times
print("\n")

L1=[12,23,34,45,56,67]
sum=0
for i in L1:
    sum=sum+i
print(sum) #to find the sum of the list
print("\n")

L2=[13,24,35,46,57,68,79]
avg=0
for i in L2:
    avg=avg+i
print(avg/len(L2)) #to get the average of the list
print("\n")
#i love this one
#so i did it on input method
#got some help too

list=eval(input("Input the list you want to search in  :"))
search=eval(input("Input the keyword to search  :"))
flag = 0
for i in range(len(list)):
    if list[i]==search:
        print("The value is present on index number :",i)  #Linear search through the list.
        flag = 1
if(flag == 0):
    print("There is no such element")

  
    
    
    

