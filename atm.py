b= 50000 

pin = input("Enter your 4-digit PIN: ")

if pin == "1234":
    wa = int(input("Enter withdrawal amount: "))

    if wa <= 0:
        print("Withdrawal amount must be greater than 0.")
    elif wa % 100 != 0:
        print("Withdrawal amount must be a multiple of 100.")
    elif wa >b :
               print("Insufficient balance.")
    else:
        b -= wa
        print("Withdrawal successful.")
        print("Remaining balance:", b)
else:
    print("Incorrect PIN.")
