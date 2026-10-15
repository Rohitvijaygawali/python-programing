for number in range(2, 101):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        print(number)
