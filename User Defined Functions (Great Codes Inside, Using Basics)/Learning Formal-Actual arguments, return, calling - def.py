def changer(P,Q=10):
    P=P/Q
    Q=P%Q
    print (P,"#",Q)
    return P
A=200
B=20
A=changer(A,B)
print (A,"$",B)
B=changer(B)
print (A,"$",B)
A=changer(A)
print (A,"$",B)

#Solving this through dry running made concepts alot more clear.