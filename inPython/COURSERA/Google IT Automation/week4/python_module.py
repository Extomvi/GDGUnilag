import datetime
import random

number = random.randint(1, 10)
print(number)

now = datetime.datetime.now()
print("This random number was generated at {}.".format(now))

next_month = now + datetime.timedelta(days=30)
print("This time next month is {}.".format(next_month))
