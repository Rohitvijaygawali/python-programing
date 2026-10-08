# Armstrong number
num = int(input("Enter a number: "))
digit = str(num)
sum = 0
for i in digit:
    digit = temp%10
    sum = sum+digit**digit
    temp=temp/10

     
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")