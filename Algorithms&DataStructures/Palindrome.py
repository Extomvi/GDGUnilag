"""Palindrome Checker"""

def is_palindrome(str): #One liner code
    return str==''.join(str[::-1])

def isPalindrome(str):
    reversed_string = str[::-1]
    if str == reversed_string:
        return True
    return False


if __name__ == "__main__":

    str = "madam"
    print(isPalindrome(str))