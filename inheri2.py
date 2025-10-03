class Estate:
    def __init__(self,street,house_no,gates):
        self.street = "olu_street"
        self.house_no = 50
        self.gates = "black_gate"

    def organize(self):
        return "commitee"
    def to_pay(self):
        return "dues!"
    
class Omole(Estate):
    def __init__(self,shops,restaurants,hotels):
        super().__init__("olu_street",50,"black_gate")
        self.shops = "90"
        self.restaurants = restaurants
        self.hotels = hotels
    
    def pay_shop(self):
        return f"shop_dues on {self.street} are outrageous "
    def relax(self):
        return f"relaxing in {self.house_no}"

class Peace(Estate):
    def __init__(self,system,business,school):
        super().__init__("olu_street",50,"black_gate")
        self.system = system
        self.business = business
        self.school = "victory_school"

    def to_lock(self):
        return f"rebels tries to escape through the {self.gates}"
    def to_pay(self):
        return f"{self.house_no} houses are being investigated"
    
the_estate = Estate("olu_street",50,"black_gate")
my_estate1 = Omole(50,"cool","just_fine")
my_estate2 =Peace("perfect","going_fine","victory_school")
my_estate1.restaurants = "good"

print(my_estate1.pay_shop())
print(my_estate1.relax())

print(my_estate1.to_pay())
print(my_estate2.to_lock())

print(my_estate1.street)






