

  
class Father:
    def __init__(self,name,skin_color,sex,intelligence,height):
        self.name = name
        self.skin_color = skin_color
        self.sex = sex
        self.intelligence = intelligence
        self.height = height

    def work(self):
        return "up and running"
    def to_pray(self):
        return "kinda lazy"
    
class Mother:
    def __init__(self,name,size,sex,emotion,beauty):
        self.name = name
        self.size = size
        self.sex = sex
        self.emotion = emotion
        self.beauty = beauty

    def chores(self):
        return "never ending"
    def to_cook(self):
        return "never gone wrong"  
  
   #1st childclass 
class Boy(Father,Mother):
    def __init__(self,name,sex,emotion,height):
        super().__init__("big_daddy","dark","male",False,70)
        super().__init__("big_mama","plus_size","female",True,True)
        self.name = "big_boy"
        self.sex = "male"
        self.emotion = False
        self.height = 40

    def to_play(self):
        return f"playful just as {self.name}"
    def to_cry(self):
        return f"{self.name} has the biggest heart"
    def to_cook(self):
        return f"no one come close to {self.name} cooking"
    def to_work(self):
        return f"this boy is {self.intelligence} at work"
    

#second child class
class Girl(Father,Mother):
    def __init__(self,name,beauty,emotion,age):
        super().__init__("dad","dark","male",False,70)
        super().__init__("mom","slim","female",False,False)
        self.name = "big_girl"
        self.beauty = False
        self.emotion = False
        self.age = 30

        #method overriding (inheritance)
    def chores(self):
        return f"{self.name} is also a {self.size}"
    def to_pray(self):
        return f"big_girl's {self.skin_color} side"
 #polymorphism   
def my_only_child(Father):
    return boy.to_work()

  
  #creating objects  
boy = Boy("big_boy","male",False,40)
girl = Girl("big_girl",False,False,30)
 
my_boy = boy.to_work()
my_girl = girl.to_pray()

#polymorphism
print(my_only_child(my_boy))
print(my_only_child(my_girl))





       #attribute overriding  
boy.beauty = False
boy.emotion = False
boy.size = "petite"
girl.skin_color = "light_skin"
girl.intelligence = True
girl.height = 80
girl.size = "petite"


print(boy.to_play())
print(boy.to_cry())
print(boy.to_cook())
print(boy.to_work())
print(girl.chores())
print(girl.to_pray())

print(boy.beauty)
print(boy.emotion)
print(boy.size)

print(girl.skin_color)
print(girl.intelligence)
print(girl.height)













