"""
All the minibank logic lie here.
Intereacts directly with main.py and utils.py.
"""

from pprint import pprint
from utils import Utilities

#object creation
utilities = Utilities()

class MiniBank:
    
    def startMenu(self):
        """
        The entry of minibank. Responsible for bridging the methods for 
        log in, registration, and exit. 
        """
        startOptions = ['1', '2', '0']
        print("\n____Lin's Minibank_____\n")
        while True:
            startChoice = input("Enter 1 to log in.\nEnter 2 to register.\nEnter 0 to exit."
                            "\nEnter here: ")
            if startChoice in startOptions:
                if startChoice == '1':
                    self.logIn()
                    # pprint(userData, sort_dicts=False)                      #----> delete later <----#
                elif startChoice == '2':
                    self.register()
                elif startChoice == '0':
                    print("Bye. Have a nice day...")
                    exit(0)
            else:
                print("Ivalid Input. Try Again.")
    
    def logIn(self):
        """
        Responsible for user log in. 
        User must enter the correct account number, username, and password. 
        """
        userData = utilities.dictCreate()
        signal = False                  #intend to check user acc number existence
        print("\n_____Log in Session_____\n")
        while True:
            print("Please enter 0 to step back.")
            try:
                accNumber = int(input("Enter account number: "))
                if accNumber == 0:
                    break
            except ValueError:
                print("Invalid Input. Try agin")
                continue
            username = input("Enter username: ")
            showcaseName = username
            r_username = utilities.space_remover(username)
            if username == '0':
                break
            password = input("Enter password: ")
            if password == '0':
                break
            if userData == {}:
                print("Account number does not exist...")
            else:
                for i in userData:
                    if accNumber == i:
                        signal = True
                        break
                if signal:
                    if r_username == userData[accNumber]['r_username'] and password == userData[accNumber]['r_password']:
                        self.userMenu(accNumber, showcaseName)
                        break
                    else:
                        print("Details info not right. Try again.")
                else:
                    print("Account number does not exist...")
    
    def register(self):
        """
        Responsible for new user registration. 
        Name and password strength are controlled to avoid security leak and maintain high professional
        standards.
        If there is no prior user, the first incoming user will have account number 1000.
        """
        userData = utilities.dictCreate()
        RegisterRawList = []
        print("\n_____Registration Session_____\n")
        #Getting first data of the reversed dictionary
        if not userData:
            r_accNumber=1000                            #if the user is the very first user....
        else:
            r_accNumber = next(reversed(userData))+1    
        RegisterRawList.append(str(r_accNumber))
        r_username = input("Enter username to register: ")
        r_username = utilities.space_remover(r_username)
        RegisterRawList.append(r_username)
        while True:
            r_password = input("Set a strong password: ")
            passQualityCheck=utilities.password_quality(r_password)
            if passQualityCheck:
                RegisterRawList.append(r_password)
                break
            else:
                print("Weak password...")
        while True:
            try:
                r_amount = int(input("Enter initial balance (at least 1000): "))
                if r_amount >0:
                    if r_amount<1000:
                        print("Initial amount must be at least 1000...")
                        continue
                    else:
                        break
                else:
                    print("Initial balance is not valid...")
                    continue
                break
            except ValueError as e:
                print("Invalid Input. Try again.")
                continue
        print(f"\n-----SUCCESSFULLY REGISTERED. YOUR ACCOUNT NUMBER IS {r_accNumber}.-----\n")
        RegisterRawList.append(str(r_amount))
        utilities.registerStrCreate(RegisterRawList)
        
    def userMenu(self, accNumber, username):
        """
        Responsible for connecting the logic of transfer, withdraw, deposit, and update 
        account information between user the system
        """
        username = username.upper()
        print(f"\n_____WECLOME {username}_____\n")
        while True:
            userMenuChoice = input("Enter 1 to transfer money.\nEnter 2 to withdraw money.\n" \
                            "Enter 3 to deposit money.\nEnter 4 to update account infomation." \
                            "\nEnter 0 to log out.\nEnter here: ")
            if userMenuChoice=='1':
                self.transfer(accNumber)
            elif userMenuChoice == '2':
                self.withdrawal(accNumber) 
            elif userMenuChoice == '3':
                self.deposit(accNumber)
            elif userMenuChoice == '4':
                self.accountInfo_update(accNumber)
            elif userMenuChoice == '0':
                break
            else:
                print("Invalid Input. Try again.")
            
    def transfer(self, accNumber):
        """
        Responsible for all the transfer processes happens between the users.
        1. User must not transfer to his/her own account
        2. Transfer balance must not exceed current balance, and must be a valid number.
        3. User needs to re-enter the password to confirm transaction.
        Transactions will be saved in user file in transactions/.
        """
        userData = utilities.dictCreate()
        TransferSignal = False
        Type = ['TRANSFER','RECEIVE']
        accNumbers = []
        print("\n_____Transfer Session_____\n")
        while True:
            try:
                receiverAccNumber = int(input("Enter receiver's account number: "))
                if receiverAccNumber == accNumber:              #--->same number is not allowed.
                    print("You cannot transfer to your own account...")
                    continue
            except ValueError:
                print("Invalid Input. Try again.")
                continue
            #receiver account existence
            for i in userData:
                if receiverAccNumber == i:
                    TransferSignal = True
                    break
            if TransferSignal == True:                          #---> receiver exists
                while True:
                    print(f"Receiver's account number : {receiverAccNumber} | Name : {userData[receiverAccNumber]['r_username']}")
                    try:
                        transferBalance = int(input('Enter transfer amount: '))
                        if transferBalance>userData[accNumber]['r_amount']:
                            print('Not enough money to transfer....')
                            continue
                        elif transferBalance<=0:
                            print("Transfer balance is not valid...")
                            continue
                        break
                    except ValueError:
                        print("Only enter digits....")
                while True:
                    passCheck = input("Re-enter password to confirm transfer: ")
                    if passCheck == userData[accNumber]['r_password']:
                        userData[accNumber]['r_amount'] -= transferBalance
                        userData[receiverAccNumber]['r_amount'] += transferBalance
                        print(f"\nTRANSACTION COMPLETE.\n ")
                        print(f"Your current balance: {userData[accNumber]['r_amount']}")
                        break
                    else:
                        print("Wrong Password...")
            else:
                print("Receiver not found...")
                continue
            utilities.listCreate(userData)
            accNumbers=[accNumber, receiverAccNumber]
            utilities.transactionCreate_transfer(accNumbers, Type, transferBalance, [f"TO:{receiverAccNumber}", f"FROM:{accNumber}"])                                       
            break

    def withdrawal(self, accNumber):
        """
        Responsible for withdrawing money from account. 
        1. Withdrawal amount must be valid and not exceed the current amount.
        2. User need to re-type the password to confirm the process
        Transactions will be saved in user file in transactions/.
        """
        userData = utilities.dictCreate()
        print("\n_____Withdrawal Session_____\n")
        Type = 'WITHDRAW'
        while True:
            try:
                withdrawBalance = int(input("Enter amount to withdraw: "))
                if withdrawBalance>userData[accNumber]['r_amount']:
                    print("Not enough money to withdraw...")
                    continue
                elif withdrawBalance<=0:
                    print("Withdrawal balance is not valid...")
                    continue
                
                break
            except ValueError:
                print("Only enter digits...")
                continue
        while True:
            passCheck = input("Re-enter password to confirm withdrawal: ")
            if passCheck == userData[accNumber]['r_password']:
                #print("APPROVED")
                userData[accNumber]['r_amount'] -= withdrawBalance
                print(f"\nWITHDRAWAL COMPLETE.\n ")
                break
            else:
                print("Wrong Password...")
        utilities.listCreate(userData) 
        utilities.transactionCreate_DepoWith(accNumber, Type, withdrawBalance, "-")  

    def deposit(self, accNumber):
        """
        Responsible for money deposit in the bank. 
        1. The deposit amount must be valid.
        2. User needs to confirm the process by re-entering the password
        Transactions will be saved in user file in transactions/.
        """
        userData = utilities.dictCreate()
        Type = 'DEPOSIT'
        print("\n_____Deposit Session_____\n")
        while True:
            try: 
                depositBalance = int(input("Enter amount to deposit: "))
                if depositBalance <= 0:
                    print("Deposit balance is not valid...")
                    continue
                break
            except ValueError:
                print("Only enter digits...")
                continue
        while True:
            passCheck = input("Re-enter password to confirm deposit: ")
            if passCheck == userData[accNumber]['r_password']:
                userData[accNumber]['r_amount'] += depositBalance
                print(f"\nDEPOSIT COMPLETE.\n ")
                break
            else:
                print("Wrong Password...")
        utilities.listCreate(userData) 
        utilities.transactionCreate_DepoWith(accNumber, Type, depositBalance, "+")          

    def accountInfo_update(self, accNumber):
        """
        Responsible for updating user information such as name and password.
        Name and password strength quality will be also checked in here as well. 
        At the end of this method, the new data dictionary will be rewritten in 
        the file userdata.txt.
        """
        userData = utilities.dictCreate()
        print("\n_____Updating Account Infomation_____\n")
        while True:
            UpdateChoice = input("Enter 1 to change name.\nEnter 2 to change password.\n" \
                                "Enter 3 to check account information.\nEnter here: ")
            if UpdateChoice == '1':
                while True:
                    newName = input("Enter new name: ")
                    nameQuality, newName=utilities.name_quality(newName)
                    if nameQuality:
                        passCheck = input("Enter password to confirm: ")
                        if passCheck == userData[accNumber]['r_password']:
                            result, NewUserData = self.nameChange(accNumber, newName)
                            break
                        else:
                            print("Wrong Password. Try again...")
                            continue
                    else:
                        print("New name is not valid....")
                        continue
                if result:
                    print("\n-----NAME SUCCESSFULY CHANGED-----\n")
                else:
                    print("Something went wrong...")
            elif UpdateChoice == '2':
                while True:
                    newPass = input("Set new password: ")
                    passQualityCheck=utilities.password_quality(newPass)
                    if passQualityCheck==False:
                        print("Weak password...")
                        continue
                    passCheck = input("Enter current password to confirm: ")
                    if passCheck == userData[accNumber]['r_password']:
                        result, NewUserData=self.passwordChange(accNumber, newPass)
                        break
                    else:
                        print("Wrong password....")
                        continue
                if result:
                    print("\n-----PASSWORD SUCCESSFULLY CHANGED.-----\n")
                else:
                    print("Something went wrong...")
            elif UpdateChoice == '3':
                print('Account Number = ', accNumber)
                print('Name = ', userData[accNumber]['r_username'])
                print("Pass = ", userData[accNumber]['r_password'])
                print('\n')
                continue
            else:
                print("Invalid Input. Please enter 1 or 2.")
                continue
            utilities.listCreate(NewUserData) 
            break
        
    def nameChange(self, accNumber,newName):
        """
        Respnsible for updating name.
        New updated dictionary will be returned along with bool data.
        """
        userData = utilities.dictCreate()
        try:
            userData[accNumber]['r_username'] = newName
            return [True, userData]
        except Exception as e:
            print(f"ERROR: {e}")
            return [False, None]

    def passwordChange(self, accNumber, newPass):
        """
        Respnsible for updating password.
        New updated dictionary will be returned along with bool data.
        """
        userData = utilities.dictCreate()
        try:
            userData[accNumber]['r_password'] = newPass
            return [True, userData]
        except Exception as e:
            print(f'ERROR: {e}')
            return [False, None]