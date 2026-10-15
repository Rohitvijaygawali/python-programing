first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
first = abs(first)
second = abs(second)
gcd = 0

for divisor in range(1, min(first, second) + 1):
    if first % divisor == 0 and second % divisor == 0:
        gcd = divisor

print("GCD =", gcd)
