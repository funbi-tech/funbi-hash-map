class Food:
    def __init__(self,vegis,fruits,meat,fish):
        self.vegis = vegis
        self.fruits = fruits
        self.meat = meat
        self.fish = fish

    def eat(self):
        return "eating"
    def snack(self):
        return "snacking"
    
foodie = Food("carot","orange","beef","titus")

class Exercise(Food):
    def __init__(self,jugging,running,skipping):
        super(). __init__("carot","orange","beef","titus")
        self.jugging = jugging
        self.running = running
        self.skipping = skipping

    def at_gym(self):
        return "gymming"
    def drink_water(self):
        return "drinking"
    
health = Exercise(40,90,30)
health.vegis = "cabbage"
print(health.vegis)
print(health.eat())




