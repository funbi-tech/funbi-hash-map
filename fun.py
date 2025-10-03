
class Arithmetic:

    def __init__(self,first_value,second_value):
        self.first_value = first_value
        self.second_value = second_value


    def mul(self):
        return self.first_value*self.second_value
    
    def add(self):
        return self.first_value+self.second_value
    
calc = Arithmetic(100,60)
calc1 = calc.first_value
calc2 = calc.second_value
result = calc.first_value+calc.second_value
print(result)


    
    
    