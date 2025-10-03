class Dog:

    def __init__(self,name,height,skin_color,has_ear,speed):
        self.name = name
        self.height = height
        self.skin_color = skin_color
        self.has_ear = has_ear
        self.speed = speed



    def bark(self):
        return "barking!"
    
    def run(self):
        return "running!"
    
    def eat(self):
        return "eating!"
    
    def spit(self):
        return "spitting!"
    
my_dog = Dog("bruno",30,"dark",True,"fast")
dog1 = my_dog.spit()
dog2 = my_dog.eat()

result = f"my dog is {my_dog.height} {dog1} it stops {dog2}"

print(result)









