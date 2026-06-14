"""
All the utilities tools lie here.
For every process, main.py and minibank2.py don't interact directly with fileIO.py. 
This module utils.py acts like a bridge between main.py, minibank2.py and fileIO.py by 
offering its useful tools.
Some tools are intended to use in my further project without writing more tools again.
"""
from fileIO import FileIO
from datetime import datetime
from string import punctuation

#object creation
file = FileIO()

#All the utilities lie here.

class Utilities:

    def transactionCreate_transfer(self, accNumbers: list, Type: list, amount, details: list):
        """
        Responsible for creating {transfer} transaction string for writing the record back in the relevant user file.
        Two transaction strings will be generated: one for send, one for receiver
        for transfer process 
        ---> timestamp, senderNumber, type, amount, To:ReceiverNumber (sender side)
        ---> timestamp, ReceiverNumber, type, amount, FROM:senderNumber (Receiver side)
        """
        now = datetime.now()
        time=now.strftime("%Y-%m-%d %H:%M:%S")
        senderNumber= str(accNumbers[0])
        receiverNumber = str(accNumbers[1])
        amount = str(amount)
        transactionStr_sender = time+','+senderNumber+','+Type[0]+','+amount+','+details[0]+'\n'
        transactionStr_receiver = time+','+receiverNumber+','+Type[1]+','+amount+','+details[1]+'\n'
        file.transaction_save_transfer(accNumbers,transactionStr_sender, transactionStr_receiver)
        print("\n-----TRANSACTION SUCCESSFULLY SAVED-----\n")

    def transactionCreate_DepoWith(self, accNumber: int, Type: str, amount: int, detail: str):
        """
        Responsible for creating {Deposite/ Withdraw} transaction string for writing the record back in the relevant user file.
        Only one transaction string will generated, which differs in DEPOSIT or WITHDRAW.
        For Deposit or Withdraw ---> timestamp,account_no,type,amount,details
        """
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        accNumber = str(accNumber)
        amount = str(amount)
        transactionStr_Depowith = time+','+accNumber+','+Type+','+amount+','+detail+'\n'
        file.transaction_save_DepoWith(accNumber, transactionStr_Depowith)
        print("\n-----TRANSACTION SUCCESSFULLY SAVED-----\n")

    def name_quality(self, username):
        """
        Responsible for checking the quality of name to ensure that there is no
        unnecessary white spaces.
        """
        qualityMeasure = True
        index = 0
        username = username.strip()
        while index<len(username):
            if 'A'<=username[index]<='Z' or 'a' <=username[index]<='z':
                index += 1  
                continue
            if username[index] == ' ':
                index+=1
                continue
            else:
                qualityMeasure = False
                break
        if qualityMeasure:
            return qualityMeasure, self.space_remover(username)
        else:
            return qualityMeasure, None

    def space_remover(self, username):
        """
        Responsible for removing all the spaces.
        In userdata.txt, the names are not saved with 'spaces' to avoid confusion. 
        """
        NoSpaceDATA = ''
        username=username.strip()
        for i in username:
            if i == ' ':
                continue
            else:
                NoSpaceDATA+=i
        return NoSpaceDATA
    
    def registerStrCreate(self, RawRegisterList: list):
        """
        Responsible for creating string to write in registration process.
        The list of data will pass as a parameter and using that the cleaned string
        is used.
        Then it is used to append new user information in userdata.txt file. 
        """      
        registerStr = ''             
        r_accNumber = RawRegisterList[0]
        r_username = RawRegisterList[1]
        r_pasword = RawRegisterList[2]
        r_amount = RawRegisterList[3]

        userFileNumber=RawRegisterList[0]
        file.userFile_create(userFileNumber)                    #creating user file automatically in transactions/
        registerStr = r_accNumber+','+r_username+','+r_pasword+','+r_amount+'\n'
        file.register_write(registerStr)

    def specialChar_count(self, text: str):
        """
        Responsible for checking whether special characters include in the text.
        string.punctutation is used.
        """
        specials: str = punctuation
        SpecialCount = 0
        for i in text:
            if i in specials:
                SpecialCount+=1
        return SpecialCount
    
    def number_count(self, text: str):
        """
        Responsible for checking whether numbers include in the text.
        """
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        NumberCount = 0
        for i in text:
            if i in numbers:
                NumberCount+=1
        return NumberCount
            
    def password_quality(self, r_password: str):
        """
        This is responsible for determining password quality. 
        In this program, a strong password must include at least 8 characters.
        In 8 characters, 
        1. at least 2 numbers must include,
        2. at least 2 special characters must include.
        """
        qualityLength = 8
        length = 0
        for i in r_password:
            length+=1
        if length >= qualityLength:
            SpecialCount: int=self.specialChar_count(r_password)
            NumberCount: int=self.number_count(r_password)
            if SpecialCount >=2 and NumberCount >=2:
                return True
            else:
                return False
        else:
            return False

    def keyValueCreate(self, data: list):
        """
        The method keyValueCreate() accepts data as a parameter in the list form.
        !!!===The data must already been cleaned in somewhere.===!!!
        This method will create keyLists and valuesLists as the lists.  
        """
        keysList = []
        valuesList = []

        for key in data:
            keysList.append(int(key[0]))
        for value in data:
            tempList = value[1:4]
            tempDict= {'r_username': tempList[0], 'r_password': tempList[1], 'r_amount': int(tempList[2])}
            valuesList.append(tempDict)
        return keysList, valuesList
            
    def dataCleaning(self, rawData: list):
        """
        The method dataCleaning() is responsible for get rid of white spaces, escape characters
        such as \n, \t, and empty string values (''). 
        It accepets rawData as the parameter. New list named cleanedData is created and 
        all the data element that has already been purified. Finally, the cleanedData list will be 
        returned.
        """
        index = 0
        cleanedData = []
        while index<len(rawData):
            rawData[index]=rawData[index].strip()
            index+=1
        index = 0
        for i in rawData:
            if i == '' or i == ' ':
                continue
            else:
                cleanedData.append(i)
        return cleanedData 

    def dictCreate(self):
        """
        This method dictCreate() is responsible for returning the data dictionary which has already been
        cleaned and set up all the necessary format. The final data dictionary will be returned to the minibank2.py
        for further minibank logic operation. 
        """
        dataDictionary= []
        index = 0
        rawData = file.return_data()
        if rawData == '' or rawData == ' ':
            return None
        cleanedData=self.dataCleaning(rawData)
        while index<len(cleanedData):
            cleanedData[index]=cleanedData[index].split(',')
            index += 1
        keys, values = self.keyValueCreate(cleanedData)
        dataDictionary = dict(zip(keys, values))
        return dataDictionary
    
    def listCreate(self, dataDictionary: dict):
        """
        Responsible for creating the data list from incoming data dictionary parameter.
        The finalized list will be used in rewriting the userdata.txt file. 
        """
        keysList=[]
        valuesList = []
        dataList = []
        index = 0
        #For keys
        for key in dataDictionary:
            keysList.append(str(key)+',')
        #For values
        for key in dataDictionary:
            valueStr = dataDictionary[key]['r_username']+','+dataDictionary[key]['r_password']+','+str(dataDictionary[key]['r_amount'])
            valuesList.append(valueStr)
        #For final data list
        while index<len(keysList):
            data=keysList[index]+valuesList[index]+'\n'
            dataList.append(data)
            index+=1
        file.file_save(dataList)


            

        

