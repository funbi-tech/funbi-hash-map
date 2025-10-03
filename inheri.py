
class Car:
    def __init__(self,color,weight,height,brand,engine):
        self.color = color
        self.weight = weight
        self.height = height
        self.brand = brand
        self.engine = engine

    def is_moving(self):
        return True
    def at_speed(self):
        return False
    def uses_fuel(self):
        return "petrol"
    
my_car = Car("red",4,7,"toyota",True)


class Benz(Car):
    def __init__(self,uses_logo,is_hyping,cost,model):
        super().__init__("red",4,7,"toyota",True)
        self.uses_logo = uses_logo
        self.is_hyping = is_hyping
        self.cost = cost
        self.model = model

    def speed(self):
        return True
    def is_light(self):
        return True
    
    #def get_color_data(self):
      #return super().color


benz_c5 = Benz(True,True,23000000,"MODEL_C5")
#print(benz_c5.get_color_data)
#benz_c5.is_moving() = False
print(benz_c5.weight)





















