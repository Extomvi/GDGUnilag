"""Decode String"""

def decodeString(str):
    stack = []

    for i in range(len(str)):
        if str[i] != "]":
            stack.append(str[i])
        else:
            substring = ""
            while stack[-1] != "[":
                substring = stack.pop() + substring
            stack.pop()
            print(substring)

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            print(k)

            stack.append(int(k) * substring)

        print(stack)
    return "".join(stack)



if __name__ == "__main__":
    str = "3[a]2[bc]"
    print(decodeString(str))