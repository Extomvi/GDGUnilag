'''
SETTING METHODS WITHIN THE CLASS
'''

class Piglet:
    """Represents a Piglet that can say their name"""
    name = ""
    years = 0
    def speak(self):
        """Outputs a message including the name of the Piglet"""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to equivalent pig years"""
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
