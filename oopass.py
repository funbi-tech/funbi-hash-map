
class Goat:

    def __init__(self,smell,bleet,sex,color):
        self.smell = True
        self.bleet = "loudly"
        self.sex = "she_goat"
        self.color = "black"

    def run(self):
        return "running"
    def shew(self):
        return "shewing"
    
my_goat = Goat(True,"loudly","she_goat","black")
my_goat.smell = False
goat1 = my_goat.smell
my_goat.bleet = "softly"
goat2 = my_goat.bleet
my_goat.sex = "he_goat"
goat3 = my_goat.sex
my_goat.color = "brown"
goat4 = my_goat.color
print(goat1,goat2,goat3,goat4)







