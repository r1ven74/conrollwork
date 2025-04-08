class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Номер счета (приватный атрибут)
        self.__balance = balance  # Баланс (приватный атрибут)

    @property
    def account_number(self):
        return self.__account_number  # Геттер для номера счета

    @property
    def balance(self):
        return self.__balance  # Геттер для баланса

    @balance.setter
    def balance(self, count):
        if count >= 0:
            self.__balance = count  # Сеттер для баланса
        else:
            print("Баланс не может быть отрицательным")  # Сообщение об ошибке

    def deposit(self, count):
        if count > 0:
            self.balance += count  # Увеличиваем баланс
            print(f"Вы внесли {count}. Ваш баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной")  # Сообщение об ошибке

    def withdraw(self, count):
        if count > 0 and count <= self.__balance:
            self.balance -= count  # Уменьшаем баланс
            print(f"Вы withdrew {count}. Ваш баланс: {self.balance}")
        else:
            print("Неверная сумма для снятия")  # Сообщение об ошибке


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)  # Вызов конструктора родительского класса

    # Метод для снятия средств
    def withdraw(self, amount):
        if amount > 0:
            super().withdraw(amount)  # Используем метод родительского класса
        else:
            print("Неверная сумма для снятия")  # Сообщение об ошибке


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)  # Вызов конструктора родительского класса
        self.__interest_rate = interest_rate  # Процентная ставка (приватный атрибут)

    @property
    def interest_rate(self):
        return self.__interest_rate  # Геттер для процентной ставки

    def deposit(self, amount):
        super().deposit(amount)  # Используем метод родительского класса
        interest = self.balance * self.interest_rate  # Рассчитываем проценты
        self.balance += interest  # Добавляем проценты к балансу
        print(f"Проценты: {interest}. Ваш баланс: {self.balance}")

    def withdraw(self, amount):
        super().withdraw(amount)  # Используем метод родительского класса


# Пример использования классов
savings = SavingsAccount("123456", 10000)
savings.deposit(int(input("Введите сумму для депозита в сберегательный счет: ")))
savings.withdraw(int(input("Введите сумму для снятия с сберегательного счета: ")))

checking = CheckingAccount("user", 10000)
checking.deposit(int(input("Введите сумму для депозита в расчетный счет: ")))
checking.withdraw(int(input("Введите сумму для снятия с расчетного счета: ")))
