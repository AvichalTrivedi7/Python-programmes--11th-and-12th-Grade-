#This is how we make a calculator
#Without defining a function btw cuz you are in class 11

print("Welcome to the calculator!")
ans='y'
try:
    while ans=='y':
        num1=int(input("Enter the first operrand:"))
        num2=int(input("Enter the second operrand:"))
        print("The operator can be = (+,-,/,//,*,**,%)")
        oper=input("Enter the opperator you need to operate with between two numbers:")
        if oper=='+':
             print("answer is:",num1+num2)
        elif oper=='-':
             print("answer is:",num1-num2)
        elif oper=='/':
             print("answer is:",num1/num2)
        elif oper=='//':
             print("answer is:",num1//num2)
        elif oper=='*':
             print("answer is:",num1*num2)
        elif oper=='**':
             print("answer is:",num1**num2)
        elif oper=='%':
             print("answer is:",num1%num2)
        else:
             print("Oops, you entered an invalid operator!")
        print("Do you wish to continue?")
        ans=input("Enter y or n:")
        ans=ans.lower()
        if ans!='y' and ans!='n':
            print("Oops you entered what you were not supposed to, we will take it as n")
            print("Thankyou")
except:
    print("Oops, You are supposed to enter a numeric value in opperand section")
        
