class Bank:

    def __init__(self, balance: List[int]):
        self.account_balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isValidAccount(account1) or not self.isValidAccount(account2):
            return False
        cur_bal = self.account_balance[account1 - 1]
        if money > cur_bal:
            return False
        self.account_balance[account1 - 1] -= money
        self.account_balance[account2 - 1] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValidAccount(account):
            return False
        self.account_balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isValidAccount(account):
            return False
        cur_bal = self.account_balance[account - 1]
        if money > cur_bal:
            return False
        self.account_balance[account - 1] -= money
        return True



    def isValidAccount(self, accountNumber: int) -> bool:
        return accountNumber >= 1 and accountNumber <= len(self.account_balance)
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)