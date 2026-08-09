hex16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def lite(color:str, val:int):
    red = int(color[1:3], 16)
    red = max(0, min(red + val, 255))
    green = int(color[3:5], 16) + val
    green = max(0, min(green + val, 255))
    blue = int(color[5:7], 16) + val
    blue = max(0, min(blue + val, 255))

    new_color = "#"
    for color_val in [red, green, blue]:
        new_color += f"{hex16[color_val // 16 % 16]}{hex16[color_val % 16]}"

    return new_color

if __name__ == "__main__":
    print(lite("#ff4402", -12))