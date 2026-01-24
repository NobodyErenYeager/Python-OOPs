class Account:
    def __init__(self, act_num, balance):
        self.account = act_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not Enough funds!")

    
    def get_balance(self):
        print(f"Balance: {self.balance}")


class InterestAccount(Account):
    def __init__(self, act_num, balance, interest_rate):
        Account.__init__(self, act_num, balance)
        self.interest_rate = interest_rate

    def calc_interest(self):
        print(f"Interest Rate: {self.balance * self.interest_rate}")


class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def history(self):
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(InterestAccount, Transactions):
    def __init__(self, act_num, balance, interest_rate):
        InterestAccount.__init__(self, act_num, balance, interest_rate)
        Transactions.__init__(self)

    def transaction(self, amount, type="withdraw"):
        if type == "deposit":
            InterestAccount.deposit(self, amount)
            Transactions.add_transaction(self, f"Deposit: {amount}")
        else:
            InterestAccount.withdraw(self, amount)
            Transactions.add_transaction(self, f"Withdraw: {amount}")


savings = SavingsAccount("SA001",5000,0.08)
savings.transaction(2500, "deposit")
savings.transaction(650)

savings.calc_interest()
savings.get_balance()

savings.history()
