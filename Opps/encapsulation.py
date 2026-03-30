class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
        
    def get_bankaccount_details(self):
        print(f"{self.name} {self.__balance}")
        
    


b1 = BankAccount("sanjeev kumar",10000)
print(b1._BankAccount__balance)  # type: ignore
b1.get_bankaccount_details()