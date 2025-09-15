# nested while loop
# A code to simulate a bank ATM
print("welcome to Equity Bank ATM")
restart = "Y"
chances = 3
balance = 1500
while chances >= 0:
    pin = int(input("Enter your four digit code: "))
    if pin == 1234:
        print("You have entered the PIN correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Please press 1 for your balance\n")
            print("Please press 2 to make a withdrawal\n")
            print("Please press 3 to deposit\n")
            print("Please press 4 to return card\n")
            option = int(input("What would you like to choose? "))
            if option == 1:
                print("Your account balance is Ksh:", balance, "\n")
                restart = input("Would you like to go back?")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank you")
                    break

            elif option == 2:
                option2 = "y"
                withdrawal = float(input("How much would you like to withdraw? \nKsh500/Ksh100/KSh1200: "))
                if withdrawal in [500, 100, 1200]:
                    balance = balance - withdrawal
                    print("\nYour balance is now Ksh", balance)
                    restart = input("would you like to go back?")
                    if restart in ("n", "NO", "no", "N"):
                        print("Thank you")
                        break
                elif withdrawal != [500, 100, 1200]:
                    print("Invalid amount,Please re-try\n")
                    restart = "y"

            elif option == 3:
                deposit = float(input("How much would you like to deposit?"))
                balance = balance + deposit
                print("Your balance is now Ksh", balance)
                restart = input("would you like to go back?")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank you")
                    break

            elif option == 4:
                print("please wait while your card is being returned...\n")
                print("Thank you for your service")

            else:
                print("Please Enter a correct number")

    elif pin != 1234:
        print("Incorrect password")
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break


