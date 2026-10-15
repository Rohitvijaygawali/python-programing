start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
prime_sum = 0

for number in range(start, end + 1):
    if number < 2:
        continue
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        prime_sum += number

print("Sum of prime numbers =", prime_sum)
