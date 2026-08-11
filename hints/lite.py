def lite(color:str, val:int):
    red = int(color[1:3], 16)
    red = max(0, min(red + val, 255))
    green = int(color[3:5], 16)
    green = max(0, min(green + val, 255))
    blue = int(color[5:7], 16)
    blue = max(0, min(blue + val, 255))

    new_color = f"#{red:02x}{green:02x}{blue:02x}"

    return new_color

if __name__ == "__main__":
    print(lite("#00aa00", 33))