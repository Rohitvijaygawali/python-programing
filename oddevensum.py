#accept 4 digit number and print odd and even sum 
num = int(input("Enter a 4-digit number: "))
odd_sum = 0
even_sum = 0
for digit in str(num):
    digit = int(digit)
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

print(f"Sum of even digits: {even_sum}")
print(f"Sum of odd digits: {odd_sum}")