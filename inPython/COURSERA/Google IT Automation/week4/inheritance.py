class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

class Piglet(Animal):
    sound = "Oink!"
class Cow(Animal):
    sound = "Moooooo!"

weld = Apple("red", "tart")
yeld = Grape("green", "sweet")
tom = Piglet("Tom")
milky = Cow("Milky White")

print(weld.color)
print(yeld.flavor)
tom.speak()
milky.speak()