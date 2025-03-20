# to print odd numbers and even numbers separate 

a= int(input("Enter the range starting = "))
b= int(input("Enter the range ending = "))
    
for i in range(a,b+1):
    if i%2 != 0:
      print(i)
    
    else:
      print("\t\t ",i )
