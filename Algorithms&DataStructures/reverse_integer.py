"""Reverse an Integer"""

def reverse_integer(n):
    reversed_num = 0

    while n>0:
        remainder = n%10
        reversed_num = reversed_num*10 + remainder
        n = n//10

    return reversed_num


if __name__ == "__main__":
    n = 54321
    print(reverse_integer(n))