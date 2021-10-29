
class budget:

    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
       

    def deposit (self):
        depo = int(input("amount to deposit \n"))
        self.balance += depo
        return f"your new balance for {self.name} is {self.balance}"
    
    def withdraw(self):
        withd = int(input("amount to withraw \n"))
        self.balance -= withd
        return f"your new balance for {self.name} is {self.balance}"
    
    def getBalance(self):
         return f"your balance for {self.name} is {self.balance}"

    def transfer(self, toCat):  #toCat is the other object to transfer to
        amount_to_transfer = int(input("amount to transfer  \n"))
        self.balance -= amount_to_transfer
        toCat.balance += amount_to_transfer
        return f"Transfer successful. Your new balance for {self.balance} is {self.balance} \n new balance for {toCat.name} is {toCat.balance}"

#food = budget("food", 0)
#clothing = budget("cloth", 0)
#food.transfer(clothing)
#print(clothing.name)
#print(food.name)

#the function below is to test the budget class
def main():
    category = []
    cat = []
    num_cat = int(input("How many categories do you want \n"))
    running = True
    for i in range(num_cat):
        n = input(f"{i+1}  Name of category \n")
        category.append(n)
        cat.append(str(n))
        category[i] = budget(cat[i], 0)
    while running:
        print("What operation do yoou want to perform? \n")
        print("1. Deposit to a category \n")
        print("2. Withdraw from a category \n")
        print("3. Transfer from a category \n")
        print("4. Get a category balance \n")
        print("5. Exit")
        option = int(input("choose an option"))

        if option == 1:
            print('select a category to deposit to')
            for i in range(num_cat):
                print(f"{i + 1}. {category[i].name}")
            select = int(input("choose the category by number \n"))
            print(category[select - 1].deposit())

        if option == 2:
            print('select a category to withdraw from')
            for i in range(num_cat):
                print(f"{i + 1}. {category[i].name}")
            select = int(input("choose the category by number \n"))
            print(category[select - 1].withdraw())

        if option == 3:
            print('select a category to transfer from \n')
            for i in range(num_cat):
                print(f"{i + 1}. {category[i].name}")
            select = int(input("choose the category by number \n"))

            print('select a category you want to  transfer to')
            for j in range(num_cat):
                print(f"{j + 1}. {category[j].name}")
            select2 = int(input("choose the category by number \n"))

            print(category[select - 1].transfer(category[j]))

        if option == 4:
            print('select a category to check the balance \n')
            for i in range(num_cat):
                print(f"{i + 1}. {category[i].name}")
            select = int(input("choose the category by number \n"))
            print(category[select - 1].getBalance())
    
        if option == 5:
            print("Thanks for using the app")
            running = False

        print("Do you wnnt to perfor another opration yes/no \n")
        oper = input("yes/no \n")
        if oper == "yes":
            pass
        elif oper == "no":
            print("Thanks for using the app")
            running = False

main()








    
