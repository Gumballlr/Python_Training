class balanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialMount, AccountName):
        self.balance = initialMount 
        self.name = AccountName
        print(f"\nAccount {self.name} created. \nBalance = ${self.balance:.2f}")
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f} ")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(" Deposit Complete")
        self.getBalance()
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(
                f"\n Sorry, your account '{self.name}' only has a balance of ${self.balance:.2f} ")
    def withDraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('\nWithdraw complete.')
            self.getBalance()
        except balanceException as error:
            print(f"\nwithdraw interupted: {error}")
    def transferToAccount( self, amount, account):
        try:
            print('\n---Transfer---\n')
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print('\n---Transfer Complete---\n')
        except balanceException as error:
            print(f'----Transfer interupted --- {error}')

class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount *1.05)
        print("\n ---Deposit complete---Interest Reward")
        self.getBalance()
class SavingAcc(InterestRewardAcc):
    def __init__(self, initialMount, AccountName):
        super().__init__(initialMount, AccountName)
        self.fee =5
    def withDraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance -( amount + self.fee)
            print("\n Withdraw completed--- Saving acc")
            self.getBalance()
        except balanceException as error:
            print(f'\nWithdraw interupted: {error}')
