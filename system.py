print("Welcome to Plate Banking System")
def creation_account():
    existing_acc_numbers = []
    create_acc_number = str(input("Please enter account number (Four Digit Number):   "))
    with open("plates.txt", "r") as plate2:
        for line in plate2.readlines():
            if str(create_acc_number) in line:
                existing_acc_numbers.append(line)
    if len(existing_acc_numbers) >= 1:
        print("Already Existing Account Number.")
        creation_account()
    create_acc_pin = str(int(input("Please enter PIN (Four Digit Number):   ")))
    create_acc_deposit = str(int(input("Please enter initial deposit :   ")))
    print("Your Account number is - " + create_acc_number)
    print("Your Account PIN is - " + create_acc_pin)
    print("Your initial deposit is - " + create_acc_deposit)
    confirmation = str(input("Are these details correct ? [Y/N]"))
    if confirmation == "Y":
        create_data = create_acc_number + "-" + create_acc_pin + "/" + create_acc_deposit
        with open("plates.txt","a") as plate:
            plate.write(create_data)
            plate.write("\n")
        print("Account Created !")
        interface(create_acc_number,create_acc_pin,create_acc_deposit)
def interface(account,pin,balance):
    print("""
    [1] Check Account Balance
    [2] Deposit Money
    [3] Withdraw Money
    [4] Change PIN""")
    user_input = int(input(""))
    if user_input == 1:
        print("Your account balance is :  " + str(balance))
    elif user_input == 2:
        deposit = int(input("Amount : "))
        final_balance = str(int(balance) + deposit)
        print("Your new account balance is :  " + final_balance)
        data = str(account) + "-" + str(pin) + "/" + str(final_balance)
        with open("plates.txt","a") as writer:
            writer.write(data)
            writer.write("\n")
    elif user_input == 3:
        withdrawal = int(input("Amount : "))
        final_balance = str(int(balance) - withdrawal)
        print("Your new account balance is :  " + final_balance)
        data = str(account) + "-" + str(pin) + "/" + str(final_balance)
        with open("plates.txt", "a") as writer:
            writer.write(data)
            writer.write("\n")
    elif user_input == 4:
        verification_pin = str(input("Please enter old PIN :  "))
        if verification_pin == str(pin):
            new_pin = int(input("New PIN :  "))
            data = str(account) + "-" + str(new_pin) + "/" + str(balance)
            with open("plates.txt", "a") as writer:
                writer.write(data)
                writer.write("\n")
plates = []
print("""
[1] Login
[2] Create Account""")
user_choice = int(input(""))
if user_choice == 1:
    acc_number = int(input("Please enter account number :  "))
    with open("plates.txt","r") as plate:
        for line in plate.readlines():
            if str(acc_number) in line:
                plates.append(line)
    if len(plates) > 1:
        plates = plates[int(len(plates))-1]
    if type(plates) == list:
        x = plates[0].split("-",2)
    else:
        x = plates.split("-", 2)
    y = x[1].split("/",2)
    account_balance = y[1]
    verified_pin = y[0]
    unverified_pin = str(int(input("Please enter PIN :  ")))
    if str(verified_pin) == unverified_pin:
       print("Access Granted")
       interface(acc_number,verified_pin,account_balance)
elif user_choice == 2:
    creation_account()