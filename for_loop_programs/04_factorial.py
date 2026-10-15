n = int(input("Enter a non-negative number: "))
if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")

factorial = 1
for number in range(1, n + 1):
    factorial *= number

print("Factorial =", factorial)
