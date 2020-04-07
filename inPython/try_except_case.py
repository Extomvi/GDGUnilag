'''
CLEAN VERSION
'''

largest = None
smallest = None

while True:
     number = input("When you are satisfied with your input, enter 'done'" + "\nEnter a number: ")

     if number == "done":
        break
     try:
         a = float(number)
     except:
         print("Invalid input")
         continue
     number = float(number)

     if smallest is None:
         smallest = number
     if number < smallest:
         smallest = number
     if largest is None:
         largest = number
     if number > largest:
         largest = number
        
print("Largest is ", int(largest))
print("Smallest is ", int(smallest))

