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