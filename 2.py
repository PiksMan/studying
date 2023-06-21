def palindrome_searching(str):
    if len(str) % 2 != 0:
        centre = len(str)//2
        first_part = str[0:centre]
        second_part = str[centre+1:len(str)]
        if first_part == second_part[::-1]:
            return True

    else:
        centre = len(str)//2
        first_part = str[0:centre]
        second_part = str[centre:len(str)]
        if first_part == second_part[::-1]:
            return True
    return False


print(palindrome_searching('123321'))
print(palindrome_searching('12321'))
