import csv 
import sys 
import pandas as pd 

def enterfields(): 
     f=open("art.csv","a",newline='') 
     w=csv.writer(f) 
     l=["ART NO","ART NAME","PRICE"]
     w.writerow(l) 
     f.close() 

def enterdata(): 
     f=open("art.csv","a",newline='') 
     w=csv.writer(f) 
     n=int(input("enter number of ARTS"))
     for x in range(n): 
          fno=input("enter the art no")
          name=input("enter the art name")
          fare=int(input("enter the PRICE"))
          l=[fno,name,fare]
          w.writerow(l)
     f.close() 

def display(): 
     f=open("art.csv","r") 
     stud=csv.reader(f) 
     for i in stud: 
          print(i) 
     f.close() 

def search(): 
     f=open("art.csv", "r") 
     stud=csv.reader(f) 
     r=input("enter artno to search")
     for i in stud: 
          if i[0]==r: 
               print(i) 
     f.close() 

def csv_to_dataframe(): 
     stud=pd.read_csv("art.csv") 
     print(stud)

def dataframe_to_csv(): 
     d={"fno":[1,2,3],"name":['a','b','c']}
     df=pd.dataframe(d) 
     df.to_csv("flight.csv")

#main program
print("*************************WELCOME TO ART GALARY******************")
while True:
     print("MENU")
     print("1-Enter Fields")
     print("2-Enter Data")
     print("3-Display")
     print("4-search")
     print("5-CSV_to_dataframe")
     print("6-Exit")
     ch=int(input("Enter your choice")) 
     if ch==1: 
          enterfields() 
     if ch==2: 
          enterdata()
     if ch==3: 
          display() 
     if ch==4: 
          search() 
     if ch==5: 
          csv_to_dataframe()
     if ch==6: 
          print("thank you")
          sys.exit()
     
