"""String Compression"""
#input_str = aababbc
def string_compression(input_str):
    compres_string = ""
    if len(input_str) <= 1:
        return input_str
    count = 1
    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            compres_string += input_str[i] + str(count)
            count = 1
    compres_string += input_str[i] + str(count)

    if len(compres_string) >= len(input_str):
        return input_str
    else:
        return compres_string




if __name__ == "__main__":
    input_str = "abbbbbbbbbbbbbbbb"
    print(string_compression(input_str))