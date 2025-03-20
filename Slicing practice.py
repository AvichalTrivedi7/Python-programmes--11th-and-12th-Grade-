x="hello world"
print(x[:2],x[:-2],x[-2:]) #till 2nd-1 index from start, till -2-1 index from start, from -2 index to end (-1)
print(x[6],x[2:4]) #element at 6th index, from 2nd index to 4-1 index
print(x[2:-3],x[-4:-2]) #from 2nd index to -3-1 index, from -4 to -2-1 index
print(x[-1:-5:-1]) # from -1 to -5 (reverse due to negative step-up value)
print(x[::-1]) # Reverses the entire string
