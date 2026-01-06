"""
This module will be solely used for file handling processes. 
This interacts directly with utils.py by saving, rewriting data in the relevant text files.
"""

class FileIO:

    def userFile_create(self, userfileNumber: str):
        """
        Creating new user file in transactions/ folder using user account number.
        """
        try:
            with open(f'transactions/{userfileNumber}.txt', 'x') as file:
                pass
        except FileExistsError as e:
            print(f"FILE EXISTS ERROR: {e}") 

    def register_write(self, registerStr: str):
        """
        Creating userdat in userdata.txt file.
        """
        try:
            with open('userdata.txt', 'a') as file:
                file.write(registerStr)
        except Exception as e:
            print(f"ERROR: {e}")

    def return_data(self):
        """
        Returning all the current userdata to create data dictionary that will further be used
        in the program runtime.
        """
        try:
            with open('userdata.txt', 'r') as file:
                data=file.readlines()
                return data
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")
    
    def file_save(self, dataList: list):
        """
        Saving userdata after changing/ updating something. 
        Data are accepted as a list in a parameter.
        """
        try:
            with open('userdata.txt', 'w') as file:
                file.writelines(dataList)
        except Exception as e:
            print(f"ERROR: {e}")

    def transaction_save_transfer(self, accNumbers: list, transactionStr_sender: str, transactionStr_receiver:str):
        """
        All the transfer record will pass as a parameter in string format for this method.
        Transfer record for sender will be in the transactions/senderNumber.txt.
        Receipt record for receiver will be in the transactions/receiverNumber.txt.
        """
        senderNumber = accNumbers[0]
        receiverNumber = accNumbers[1]
        try:
            with open(f'transactions/{senderNumber}.txt', 'a') as fileSender:
                fileSender.write(transactionStr_sender)
            with open(f'transactions/{receiverNumber}.txt', 'a') as fileReceiver:
                fileReceiver.write(transactionStr_receiver)
        except Exception as e:
            print(f"ERROR: {e}")

    def transaction_save_DepoWith(self, accNumber: int, transactionStr_DepoWith: str):
        """
        All the deposit/withdraw record will pass as a parameter in string format for this method.
        All records will be saved in their relevant files depending on the user.
        """
        try:
            with open(f'transactions/{accNumber}.txt', 'a') as file:
                file.write(transactionStr_DepoWith)
        except Exception as e:
            print(f"ERROR: {e}")