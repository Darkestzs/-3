class GameBank:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    def get_balance(self):
        return self._balance
    def set_balance(self, value):
        if value >= 0:
            self._balance = value
    def __log_transaction(self, action, amount):
        print(f"[LOG] {action}: {amount}, Баланс: {self._balance}")
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("Пополнение", amount)
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("Снятие", amount)
            return True
        return False
bank = GameBank(1000)
bank.deposit(500)  # Баланс: 1500
bank.withdraw(300)  # Баланс: 1200
print(f"Текущий баланс: {bank.get_balance()}")
