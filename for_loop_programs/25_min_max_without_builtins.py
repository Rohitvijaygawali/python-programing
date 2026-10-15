numbers = [25, 67, 12, 89, 34, 5, 56]
maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print("Maximum =", maximum)
print("Minimum =", minimum)
