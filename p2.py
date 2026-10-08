y=int(input("enter unit"))

if y :
    print("Year is leap year")
elif y % 100 == 0:
    print("Not leap year ")
elif y% 4 == 0:
    print("leap year ")
else:
    print("")