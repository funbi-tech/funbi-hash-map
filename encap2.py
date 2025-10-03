

class BankAccount:
    def __init__(self,name,account_type,balance):
        self.name = name
        self._account_type = "current"     #protected has single underscore_
        self.__balance = balance            #private has double underscore__

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

        else:
            print("deposit must be positive")

    def withdrawal(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insuffficient fund")

    def get_balance(self):
        return self.__balance


acc = BankAccount("funbi","current",5000)

print(acc.name)
print(acc._account_type)
#print(account.__balance) not accessible
print(acc.get_balance())
acc.deposit(1000)
print(acc.get_balance())
acc.withdrawal(2000)
print(acc.get_balance())



