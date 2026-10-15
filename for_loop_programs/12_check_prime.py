n = int(input("Enter a number: "))
is_prime = n >= 2

for divisor in range(2, n):
    if n % divisor == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
