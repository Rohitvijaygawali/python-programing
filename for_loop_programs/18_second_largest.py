numbers = [10, 25, 67, 45, 89, 34]
largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("There is no second-largest distinct number")
else:
    print("Largest =", largest)
    print("Second Largest =", second_largest)
