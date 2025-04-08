class Account:
    def __init__(self, account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, count):
        if count>=0:
            self.__balance = count
        else:
            print("баланс отриц")

    def deposit(self, count):
        if count > 0:
            self.balance = self.__balance + count
            print(f"твой деп  {count} твой баланс {self.__balance}")

    def deposit(self, count):
        if count>0 and count <= self.__balance:
            self.balance = self.__balance - count
            print(f"ты вывел {count} твой баланс {self.__balance}")

class CheckingAccount(Account):
    def init(self,account_number,balance=0):
        super.__init__(account_number, balance)

    def withdraw(self, amount):
        if amount > 0:
            self._Account__balance -= amount
            print(f"снято : {amount}. твой баланс: {self.balance}")
        else:
            print("неверная сумма")

class SavingsAccount(Account):
    def init(self, account_number, balance=0, interest_rate=0.01):
        super().init(account_number, balance)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self.__interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        interest = self.balance * self.interest_rate
        self.__balance += interest
        print(f"проценты: {interest}. твой баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            super().withdraw(amount)
        else:
            print("неверная сумма ")


savings = SavingsAccount("123456", 10000)
savings.deposit(int(input()))
savings.withdraw(int(input()))

checking = CheckingAccount("user", 10000)
checking.deposit(int(input()))
checking.withdraw(int(input()))


