class House:
    def __init__(self,offices,shop):
        self.offices = offices
        self.shop = shop
    
    def to_work(self):
        return f"{self.offices} are coperate"
    def hands_on(self):
        return f"{self.shop} are very busy"

class Building(House):
    def __init__(self,hotels,guest_house):
        super().__init__("opay",50)
        self.hotels = hotels
        self.guest_house = guest_house
    
    def to_work(self):
        return f"{self.hotels} are good for meetings"
    def hands_on(self):
        return f"{self.guest_house} are best to relax"
    
house = House("opay",50)
building = Building("haven","rest_well")

print(house.to_work())

print(building.to_work())





