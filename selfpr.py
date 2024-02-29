def convert_text(input_text):
    result = ""
    for char in input_text:
        if char.isalpha():
            if char.isupper():
                result += '@'
                num = ord(char) - ord('A') + 1
                if num <= 9:
                    result += str(num)
                else:
                    result += f':{num}'
            else:
                num = ord(char) - ord('a') + 1
                if num <= 9:
                    result += str(num)
                else:
                    result += f':{num}'
        elif char.isdigit():
            result += f'/{char}'
        elif char.isspace():
            result += '0'
        elif char == '@':
            result += '#'
        else:
            result += char
    return result


def main():
    user_input = input("Enter a text: ")
    output = convert_text(user_input)
    print("Converted:", output)


if __name__ == "__main__":
    main()



