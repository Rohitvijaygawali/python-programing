n = int(input("Enter a number: "))
reversed_digits = ""

for digit in str(abs(n)):
    reversed_digits = digit + reversed_digits

reverse = int(reversed_digits)
if n < 0:
    reverse = -reverse

print("Reverse =", reverse)
