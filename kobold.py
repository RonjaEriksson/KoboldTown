import random
class Kobold:

    def __init__(self, age):
        self.age = age
        self.generate_name()
        self.generate_stats()
        self.generate_colour()

    def __str__(self):
        return f"{self.name} is {self.age} years old. {self.name} is a {self.colour} kobold."

    def generate_stats(self):
        self.con = random.randint(5,15)
        self.str = random.randint(5,15)
        self.dex = random.randint(5,15)
        self.int = random.randint(5,15)
        self.wis = random.randint(5,15)
        self.cha = random.randint(5,15)

    def generate_colour(self):
        colour = "Blue"

    def generate_name(self):
        names = ["Flub", "Flick", "Glob"]
        self.name = random.choice(names)


    def kobold_manual_setup(self):
        self.generate_name()
        self.generate_stats()
        self.generate_colour()

    age = 0;
    colour = "white"
    pattern = "solid"
    traits = []
    name = "Flub"
    con = 0
    str = 0
    dex = 0
    int = 0
    wis = 0
    cha = 0

'''test_kobold = Kobold(3)
print(test_kobold)
print(test_kobold.int)
print(test_kobold.cha)'''
