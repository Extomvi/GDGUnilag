'''
UNDERSTANDING CLASSES, THEIR METHODS AND INSTANCES
'''

class Apple:
    color = ""
    flavor = ""

fruit = Apple()
fruit.color = "red"
fruit.flavor = "sweet"

veg = Apple()
veg.color = "green"
veg.flavor = "bleh"

print(fruit.color)
print(veg.flavor)