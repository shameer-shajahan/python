class Bank:

    acno : str

    bank_name : str

    balance : int

    ac_type : str

    def create_acc(self,acno,ac_type):
        
        self.bank_name="sbt"

        self.__balance=2000

        self.acno=acno

        self.ac_type=ac_type

    def deposit(self,amount):
    
        self.__balance+=amount

        print(f"your {self.bank_name} acc with {self.acno} has been credited with amount {amount} available balance {self.__balance}")

    def withdraw(self,amount):

        if amount>self.__balance:

            print(f"transaction faild insufficiant money in your {self.acno} available balance {self.balance}")

        else:

            self.__balance-=amount

            print(f"your {self.bank_name} acc with {self.acno} has been debitted with amount {amount} available balance {self.__balance}")

    def get_balance(self):

        print(f"avl balance {self.__balance}")

        

user_account=Bank()

user_account.create_acc(353454,"saving")

user_account.deposit(5000)

user_account.withdraw(1000)

# print(user_account.get_balance)








