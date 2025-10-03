
class Family:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def to_party(self):
        return "party_hard"
    def family_land(self):
        return "sold_out"
       
class Hajo(Family):
    def __init__(self,unity,peace):
         super().__init__("ola","ogun")
         self.unity = "cooperation"
         self.peace = "money"

    def elders(self):
        return f"respecting elders of the {self.name} family"
    def union(self):
        return f"loud_wedding are always hectic for {self.position}"
    def to_party(self):
        return f"partying are enjoyable in both {self.name} and {self.position} family"

    
family = Hajo("united","being_rich")

print(family.union()) 
print(family.elders())
print(family.to_party())






