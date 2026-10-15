numbers = [10, -5, 0, 25, -8, 0, 15, -2]
positive = 0
negative = 0
zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers =", positive)
print("Negative numbers =", negative)
print("Zeros =", zero)
