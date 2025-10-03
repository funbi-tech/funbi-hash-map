
class Car:
    def __init__(self,start_engine,color,brand):
        self.start_engine = "not started"
        self.color = "blue"
        self.brand = "toyota"
        

    def drive(self):
      return "driving"

     
    def uses_fuel(self):
       return "petrol"
    
car1 = Car("started","purple","toyota")
result1 = car1.uses_fuel()
result2 = car1.drive()
result3 = car1.start_engine
result4 = car1.color
result5 = car1.brand
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


 