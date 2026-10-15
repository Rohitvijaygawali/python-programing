n = int(input("Enter a number: "))
digit_sum = 0

for digit in str(abs(n)):
    digit_sum += int(digit)

print("Sum of digits =", digit_sum)
