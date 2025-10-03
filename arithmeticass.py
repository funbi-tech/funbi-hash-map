
class Math:

    def __init__(self,multiply,divide,plus,minus):
        self.multiply = multiply
        self.divide = divide
        self.plus = plus
        self.minus = minus

    def add(self):
        return 10+2
        
    def sub(self):
        return 10-2
        
    def div(self):
        return 10/2
        
    def mul(self):
        return 10*2
    
calculate = Math(10*2,10/2,10+2,10-2)
my_calc1 = calculate.mul()
my_calc2 = calculate.div()
my_calc3 = calculate.sub()
my_calc4 = calculate.add()
result = f"it is easier to use {my_calc1} table for {calculate.multiply}"
print(calculate.mul())
print(calculate.div())
print(calculate.sub())
print(calculate.add())
print(result)









        
                 