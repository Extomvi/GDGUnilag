'''
SETTING METHODS WITHIN THE CLASS
'''

class Piglet:
    name = "tom"
    years = 0
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        return self.years * 18

jerry = Piglet()
jerry.name = "Jerry"
jerry.speak()

pam = Piglet()
pam.name = "Pam"
pam.speak()

piggy = Piglet()
piggy.years = 5
print(piggy.pig_years())
