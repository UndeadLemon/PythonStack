class BankAccount:

    all_accounts = []

    def __init__(self, interest_rate, balance=0):
        self.interest_rate = interest_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance = {self.balance}")
        print(f"Interest rate is = {self.interest_rate}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= (1+self.interest_rate)
        return self
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        

dorothy_account = BankAccount(.02, 104)
meredith_account = BankAccount(.07, 20056)

dorothy_account.deposit(27).deposit(52).deposit(-30).withdraw(27).yield_interest().display_account_info()

meredith_account.deposit(207).deposit(2004).withdraw(445).withdraw(745).withdraw(421).withdraw(1435).yield_interest().display_account_info()

BankAccount.display_all_accounts()