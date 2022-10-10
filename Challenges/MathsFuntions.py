"""Write a Python Program that assigns the Principal amount
of 10000 to variable P, assign to n the value 12, and assign to r the interest rate
of 8% (0.08). Then  have the program prompt the user for the number of years t
that the money will be compounded for. calculate and print
the final amount after t years."""

principal_amount = input("Please enter Principal Amount")
r = 0.08
n =  12
number_of_years = input("Please input number of years")

P = int(principal_amount)

t = int(number_of_years)

A = P * (( 1 + (r/n))**(n*t))

print("The final amount after " , t, "years is", A)