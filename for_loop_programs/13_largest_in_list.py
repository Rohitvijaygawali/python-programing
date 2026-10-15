numbers = [25, 67, 12, 89, 34, 56]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest =", largest)
