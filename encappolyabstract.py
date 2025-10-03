class Interior:
    def __init__(self,furnitures,lighting):
        self.furnitures = "ugly"
        self.lighting = "False"
    
    def confy(self):
        self.furnitures = "beautiful"
        self.lighting = True
        return self.furnitures,self.lighting

class Exterior:
    def __init__(self,fence,store):
        self.fence = fence
        self.store = store

    def confy(self):
        self.fence = "tall"
        self.store = "messy"
        return self.fence,self.store
    
class Bedroom(Interior,Exterior):
    def __init__(self,bedding,wardrope):
        super().__init__("beautiful",True)
        super().__init__("tall","messy")
        self.bedding = bedding
        self.wardrope = wardrope

    def confy(self):
        self.bedding = "white"
        self.wardrope = 10
        return self.bedding,self.wardrope

class Livingroom(Interior,Exterior):
    def __init__(self,chair,tv):
        super().__init__(True,"beautiful")
        super().__init__("tall","messy")
        self.chair = chair
        self.tv = tv

    def confy(self):
        self.chair = "luxury"
        self.tv = "television"
        return self.chair,self.tv
    
class Kitchen(Interior,Exterior):
    def __init__(self,pot,kettle):
        super().__init__("beautiful",True)
        super().__init__("tall","messy")
        self.pot = pot
        self.kettle = kettle

    def confy(self):
        self.pot = "non_stick"
        self.kettle = "big"
        return self.pot,self.kettle
    
    interior = Interior("furniture","lighting")
    exterior = Exterior("fence","store")
    bedroom = Bedroom("bedding","wardrope")
    livingroom = Livingroom("chair","tv")
    furniture1 = Interior("ugly",False)

    #polymorphism
    print(interior.confy())
    print(exterior.confy())
    print(bedroom.confy())
    print(livingroom.confy())

    #abstraction
    print(interior.confy())

    #encapsulation
    interior1 = Interior("ugly","false")
    result = interior.confy()
    print(result)
    


    



    
        




