def space(text:str, max_char:int, extra_max:int):
    count_char=0
    new_text = ""
    for char in text:
        count_char += 1
        if char == "\n":
            count_char = 0

        if char != " ":
            if count_char < extra_max:
                new_text += char
            else:
                new_text += char + "-\n"
                count_char = 0
        elif count_char > max_char:
            new_text += "\n"
            count_char = 0
        else:
            new_text += " "

    if new_text[-1] == "\n":
        new_text = new_text[:-1]
    if new_text[-1] == "-":
        new_text = new_text[:-1]

    return new_text.replace("-\n ", "\n")