"""Palindromic Number"""

def palindromic_number(n):
    if n<0 or (n%10 == 0 and n != 0):
        return False

    reverted_number = 0
    while n > reverted_number:
        pop = n%10
        reverted_number = reverted_number*10 + pop
        n = n/10

    return n == reverted_number or n == reverted_number/10



if __name__ == "__main__":
    n = 121
    print(palindromic_number(n))