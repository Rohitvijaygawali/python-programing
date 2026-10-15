n = int(input("Enter a number: "))
digit_count = 0

for _digit in str(abs(n)):
    digit_count += 1

print("Number of digits =", digit_count)
