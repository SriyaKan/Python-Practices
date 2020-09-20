# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# number = int(input("Give me a number: "))
# if number % 2 == 0:
#     print("This number is even.")
# else:
#     print("This number is odd.")


# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message
# number = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
if number2 % 2 == 0:
    if number2 % 4 == 0:
        print("This number is a multiple of 4.")
    else: 
        print("This number is even.")
else:
    print("This number is odd.")

num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(num, " divided evenly by ", check)
else:
    print(num, " did not divide evenly by ", check)
