n = int(input("Enter n: "))
if n < 0:
    raise ValueError("n must be non-negative")

total = 0
for number in range(1, n + 1):
    total += number

print("Sum =", total)
