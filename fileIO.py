"""
This module will be solely used for file handling processes. 
This interacts directly with utils.py by saving, rewriting data in the relevant text files.
"""
from pathlib import Path

class FileIO:

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent
        self.userdata_path = self.base_dir / 'userdata.txt'
        self.transactions_dir = self.base_dir / 'transactions'
        self.userdata_path.touch(exist_ok=True)
        self.transactions_dir.mkdir(exist_ok=True)

    def transaction_path(self, accNumber):
        self.transactions_dir.mkdir(exist_ok=True)
        return self.transactions_dir / f'{accNumber}.txt'

    def userFile_create(self, userfileNumber: str):
        """
        Creating new user file in transactions/ folder using user account number.
        """
        try:
            with open(self.transaction_path(userfileNumber), 'x') as file:
                pass
        except FileExistsError as e:
            print(f"FILE EXISTS ERROR: {e}") 

    def register_write(self, registerStr: str):
        """
        Creating userdat in userdata.txt file.
        """
        try:
            with open(self.userdata_path, 'a') as file:
                file.write(registerStr)
        except Exception as e:
            print(f"ERROR: {e}")

    def return_data(self):
        """
        Returning all the current userdata to create data dictionary that will further be used
        in the program runtime.
        """
        try:
            with open(self.userdata_path, 'r') as file:
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
            with open(self.userdata_path, 'w') as file:
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
            with open(self.transaction_path(senderNumber), 'a') as fileSender:
                fileSender.write(transactionStr_sender)
            with open(self.transaction_path(receiverNumber), 'a') as fileReceiver:
                fileReceiver.write(transactionStr_receiver)
        except Exception as e:
            print(f"ERROR: {e}")

    def transaction_save_DepoWith(self, accNumber: int, transactionStr_DepoWith: str):
        """
        All the deposit/withdraw record will pass as a parameter in string format for this method.
        All records will be saved in their relevant files depending on the user.
        """
        try:
            with open(self.transaction_path(accNumber), 'a') as file:
                file.write(transactionStr_DepoWith)
        except Exception as e:
            print(f"ERROR: {e}")
