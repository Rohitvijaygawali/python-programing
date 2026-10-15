n = int(input("Enter number of terms: "))
if n < 0:
    raise ValueError("The number of terms must be non-negative")

first = 0
second = 1
for index in range(n):
    print(first, end=" " if index < n - 1 else "\n")
    first, second = second, first + second

if n == 0:
    print()
