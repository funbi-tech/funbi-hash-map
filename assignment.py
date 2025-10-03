
class State:

    def __init__(self,road,traffic_light,house,has_school):
        self.road = road
        self.traffic_light = traffic_light
        self.house = house
        self.has_school = has_school

    
    def transport(self):
        return "transporting"
    
    def traffick(self):
        return "trafficking"
    
    def system(self):
        return "systeming"
    
lagos = State(80,50,"good",True)
my_name = input("enter your local_government")
my_road = ['lagos.road']
my_traffic_light = ['lagos.traffic_light']
my_house = ['lagos.house']
my_has_school = ['lagos.has_school']
my_final_result = "my name is "+my_name+" my road is "+str(lagos.road)+" also my traffic_light is "+str(lagos.traffic_light)
print(my_final_result)

























