#THIS IS ERROR HANDLING

try:
    x=what
    
except Exception as e:
    print(e)                #wow it worked lmao


#PART-2

try:
    f=open('file_test',r)
    x=what
except FileNotFoundError and NameError:
    print("it ignored the exact two errors i mentioned, and can run into another error if there were")
    

'''I could use the else: block to continue executing statements after try: block
Since i need to catch specific errors, im not going to fill up try: block.''' 

'''And finally: block can be used to execute necessary statements
no matter what happens in try: and except: blocks finally: block will always execute'''

#PART-3

try:
    x=2+3
    if x==5:
        raise Exception

except:
    print("It raised exception and made this except clause run!")

'''you can manually raise an exception too!'''
