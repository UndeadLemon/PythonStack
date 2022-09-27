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
        
class user:
    def __init__(self, firstname, lastname, email, age, account_name="default"):
        self.first_name= firstname
        self.last_name= lastname
        self.email= email 
        self.age= age
        self.accounts= {account_name:BankAccount(interest_rate=.02, balance=0)}
    def display_info(self, account_name="default"):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        self.display_user_balance(account_name)
        return self

    def add_account(self, name):
        self.accounts[name] = BankAccount(interest_rate=.02, balance=0)
        return self


    def make_deposit(self, amount, account_name="default"):
        self.accounts[account_name].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, account_name="default"):
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name="default"):
        self.accounts[account_name].display_account_info()
        return self

    def transfer_money(self, amount, account_name, other_user, other_user_account_name="default"):
        self.make_withdrawal(amount, account_name)
        other_user.make_deposit(amount, other_user_account_name)

user_thane = user("Thane", "Abel", "thaneemail@email.com", 472)

user_shark = user("Shark", "Of the Covenant", "sharkofthecovenant@sharks.shark", "ageless")

user_thane.display_info("default").add_account("newaccount").display_info("newaccount").make_deposit(500, "newaccount").display_info("newaccount").make_withdrawal(100, "newaccount").display_info("newaccount")

user_thane.transfer_money(50, "default", user_shark)

user_shark.display_info()
# dorothy_account = BankAccount(.02, 104)
# meredith_account = BankAccount(.07, 20056)

# dorothy_account.deposit(27).deposit(52).deposit(-30).withdraw(27).yield_interest().display_account_info()

# meredith_account.deposit(207).deposit(2004).withdraw(445).withdraw(745).withdraw(421).withdraw(1435).yield_interest().display_account_info()

# BankAccount.display_all_accounts()