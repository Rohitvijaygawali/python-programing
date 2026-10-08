a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
o=input("Enter the oprator:")

if o =='+':
    print(a+b)
elif o =='-':
    print(a-b)
elif o =='*':
    print(a*b)
elif o =='/':
    if b!=0:
        print(a/b)
    else:
        print("cannot divide by zero")
else :
    print("invalid")

