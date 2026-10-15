n = int(input("Enter a number: "))
digits = str(abs(n))
power = len(digits)
digit_sum = 0

for digit in digits:
    digit_sum += int(digit) ** power

if n >= 0 and digit_sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
