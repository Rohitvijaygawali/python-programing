#even odd number form 1 to 100
e=[]
o=[]
for i in range(1,101):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

print("Even numbers:",e)
print("Odd numbers:",o)