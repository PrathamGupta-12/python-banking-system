class BankingSystem:
    def __init__(self):
        self.userAccountNumber = []
        self.userAccountDict = {}
        self.action = None


        while self.action != 8:

            print('''
                ========== Banking System ==========
                1. Create Account
                2. Deposit Money
                3. Withdraw Money
                4. Check Balance
                5. Transaction History
                6. Transfer Money
                7. Display All Accounts
                8. Exit
                ====================================
                  ''')
            
            choice = input("Enter the Choice : ")

            try:
                self.action = int(choice)

                if self.action == 1:
                    inputNumber = input("Enter the Account Number : ")

                    try:
                        accountNumber = int(inputNumber)

                        if accountNumber not in self.userAccountNumber:

                            accountHolderName = input("Enter Account Holder Name : ")

                            if not accountHolderName:

                                print("No Name was Entered.")

                            else:
                                initial = input("Enter initial Deposit : ")

                                try:
                                    initialDeposit = int(initial)

                                    if initialDeposit > 0:
                                        print("---> Account created successfully.")

                                        self.userAccountNumber.append(accountNumber)

                                        temp = {}
                                        history = []


                                        temp.update({"Name" : accountHolderName})
                                        temp.update({"Balance" : initialDeposit})
                                        temp.update({"History" : history})

                                        self.userAccountDict[accountNumber] = temp

                                        self.userAccountDict[accountNumber]["History"].append(f"Account created with ₹{initialDeposit}")
                        
                                    else:
                                        print("Enter a valid Deposit Amount.") 

                                except ValueError:
                                    print("---> Initial Deposit was found Invalid.")

                        else:
                            print("---> User of same Account Number already Exists.")

                    except ValueError:
                        print("---> Invalid Account Number Entered.")

                elif self.action == 2:

                    UserNumber = input("Enter Account Number : ")

                    try:
                        accountNumber = int(UserNumber)

                        if accountNumber not in self.userAccountNumber:
                            print("---> Account Number not Registered..")
                        
                        else:
                            deposit = input("Enter Amount : ")

                            try:
                                depositAmount = int(deposit)

                                if depositAmount < 0:
                                    print("---> Negative Amount can not be deposited in the Account.")

                                elif depositAmount == 0:
                                    print("₹0 can not be deposited in the Bank Balance")
                                
                                else:
                                    
                                    self.userAccountDict[accountNumber]["Balance"] += depositAmount

                                    print(f'''
                                        ---> ₹{depositAmount} deposited successfully.
                                        Current Balance : ₹{self.userAccountDict[accountNumber]["Balance"]}
                                          ''')
                                    
                                    self.userAccountDict[accountNumber]["History"].append(f"Deposited ₹{depositAmount}")

                            except ValueError:
                                print("---> Invalid Amount of Money.")

                    except ValueError:
                        print("---> Invalid Account Number.")

                elif self.action == 3:

                    UserNumber = input("Enter Account Number : ")

                    try:
                        accountNumber = int(UserNumber)

                        if accountNumber not in self.userAccountNumber:
                            print("---> Account Number not Registered..")
                        
                        else:
                            withdraw = input("Enter Amount : ")

                            try:
                                withdrawAmount = int(withdraw)

                                if withdrawAmount < 0:
                                    print("---> Negative Amount can not be withdrawn from the Account.")

                                elif withdrawAmount == 0:
                                    print("---> Transaction of ₹0 is Invalid")
                                
                                else:
                                    
                                    if self.userAccountDict[accountNumber]["Balance"] >= withdrawAmount:

                                        self.userAccountDict[accountNumber]["Balance"] -= withdrawAmount

                                        print(f'''
                                            ---> ₹{withdrawAmount} withdrawn successfully.
                                            Current Balance : ₹{self.userAccountDict[accountNumber]["Balance"]}
                                              ''')
                                        
                                        self.userAccountDict[accountNumber]["History"].append(f"Withdrew ₹{withdrawAmount}")

                                    else:
                                        print("---> Balance is not enough.")

                            except ValueError:
                                print("---> Inavlid Amount Entered.")

                    except ValueError:
                        print("---> Invalid Account Number.")    

                elif self.action == 4:

                    UserNumber = input("Enter Account Number : ")

                    try:
                        accountNumber = int(UserNumber)

                        if accountNumber in self.userAccountNumber:

                            print(f'''
                                ------ Account Details ------
                                Account Number : {accountNumber}
                                Name           : {self.userAccountDict[accountNumber]["Name"]}
                                Balance        : ₹{self.userAccountDict[accountNumber]["Balance"]}
                                -----------------------------
                                  ''')
                            
                        else:
                            print("---> Account Number is not Registered.")

                    except ValueError:
                        print("---> Invalid Account Number Entered.")
                
                elif self.action == 5:

                    UserNumber = input("Enter Account Number : ")

                    try:
                        accountNumber = int(UserNumber)

                        if accountNumber in self.userAccountNumber:
                            print('''
                                ------ Transaction History ------
                                  ''')
                        
                            for el in self.userAccountDict[accountNumber]["History"]:

                                print(el)

                            print('''
                                ---------------------------------
                                ''')
                            
                        else:
                            print("---> Account Number is not Registered.")

                    except ValueError:
                        print("---> Account Number is Invalid.")

                elif self.action == 6:

                    sender = input("Enter Sender Account Number : ")

                    try:
                        senderAccountNumber = int(sender)

                        if senderAccountNumber in self.userAccountNumber:

                            receiver = input("Enter Receiver Account Number : ")

                            try:
                                receiverAccountNumber = int(receiver)

                                if receiverAccountNumber in self.userAccountNumber:

                                    amount = input("Enter Amount : ")

                                    try:
                                        transferAmount = int(amount)

                                        if senderAccountNumber == receiverAccountNumber:
                                            print("Money Transfer in Same Account is not Valid.")

                                        elif transferAmount < 0:
                                            print("---> Negative Amounts can not be Transfered.")

                                        elif transferAmount == 0:
                                            print("Transfer of ₹0 is not Valid.")

                                        elif self.userAccountDict[senderAccountNumber]["Balance"] >= transferAmount:

                                            self.userAccountDict[senderAccountNumber]["Balance"] -= transferAmount
                                            self.userAccountDict[receiverAccountNumber]["Balance"] += transferAmount

                                            print(f"---> ₹{transferAmount} transferred successfully.")

                                            self.userAccountDict[senderAccountNumber]["History"].append(f"Transferred ₹{transferAmount} to Account {receiverAccountNumber}")
                                            self.userAccountDict[receiverAccountNumber]["History"].append(f"Received ₹{transferAmount} from Account {senderAccountNumber}")

                                        else:
                                            print("Bank Balance of the Sender is not sufficient.") 

                                    except ValueError:
                                        print("---> Invalid Amount Entered.")

                                else:
                                    print("---> Receiver Account Number is not Registered.")

                            except ValueError:
                                print("---> Invalid Receiver Account Number Entered.")

                        else:
                            print("---> Sender Account Number is not Registered.")

                    except ValueError:
                        print("---> Invalid Sender Account Number Entered.")

                elif self.action == 7:

                    if not self.userAccountDict:
                        print("No User found to be displayed.")
                    else:
                        print('''
                            Account Number     Name        Balance
                              ''')
                        
                        for key in self.userAccountDict:
                            print(f'''
                                {key}     {self.userAccountDict[key]["Name"]}     ₹{self.userAccountDict[key]["Balance"]}
                                  ''')
                
                elif self.action == 8:
                    print("---> Program terminated successfully.")

            except ValueError:
                print("---> Invalid Option Selected")


bank = BankingSystem()