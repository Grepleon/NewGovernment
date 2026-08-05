def int_to_str(number:int) -> str:
    num = str(number)[::-1]
    len_num = len(num)
    i = 0
    str_num = ""

    while i < len_num:
        str_num += num[i]
        if i % 3 == 2: str_num += " "
        i += 1
    if str_num[-1] == " ":
        return str_num[:-1][::-1]
    return str_num[::-1]

if __name__ == "__main__":
    print(int_to_str(int(input())))