
# Encapsulation: protecting an object's data

# Encapsulation means hiding an object's internal data and forcing access to go through controlled methods, 
# so the object can protect itself from invalid states. Picture a bank account — you can't just edit the 
# balance number directly; you must deposit or withdraw, which enforce rules.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # the __ marks it private

    def deposit(self, amount):
        if amount <= 0:
            print("deposite must be positive")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("insufficient funds")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# _balance is stored privately. You can't reliably write account.__balance = -999 from outside (Python renames it internally to block that).
# The only sanctioned ways to change the balance are deposit and withdraw, and each contains a guard (if) that rejects nonsense.
# The object now enforces its own rules — invalid states become impossible.

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())
acc.withdraw(1000)
acc.deposit(-5)
