

class BankAccount:
    def __init__(self,acc_name,acc_type,acc_balance):
        self.acc_name = "funbi"
        self._acc_type = "current"    #protected
        self.__acc_balance = acc_balance     #private

    def deposit(self,amount):
        if amount > 0:
            self.__acc_balance += amount

        else:
            print("cool cash")

    def withdraw(self,amount):
        if amount <= self.__acc_balance:
            self.__acc_balance -= amount

        else:
            print("you are broke")

    def my_balance(self):
        return self.__acc_balance

my_acc = BankAccount("funbi","current",20000)

print(my_acc.acc_name)
print(my_acc._acc_type)
print(my_acc.my_balance())
my_acc.deposit(5000)
print(my_acc.my_balance())
my_acc.withdraw(30000)
print(my_acc.my_balance())




