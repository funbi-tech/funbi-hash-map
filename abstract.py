class Car:
    def __init__(self,start_engine):
        self.start_engine = False
    
    def start_car(self):
        self.start_engine = True

        return self.start_engine

benz = Car(False)
start_engine = True
start_engine = benz.start_car()
print(benz.start_engine)



class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        self.username = "funbi"
        self.password = 24567
        return self.username,self.password

account = Account("username","password")
print(account.login())

class Water:
    def __init__(self,turn_on_tap,turn_off_tap):
        self.turn_on_tap = turn_on_tap
        self.turn_off_tap = turn_off_tap
    
    def tap(self):
        self.turn_on_tap = "running_water"
        self.turn_off_tap = "no_water"
        return self.turn_on_tap,self.turn_off_tap

water = Water("turn_on_tap","turn_off_tap")
print(water.tap())








 