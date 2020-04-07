class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "The apple's color is {} and it's flavor is {}.".format(self.color.upper(), self.flavor)


fruit = Apple("red", "sweet")
print(fruit)
