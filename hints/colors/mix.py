def mix(color1:str, color2:str, val:float):
    red1 = int(color1[1:3], 16)
    green1 = int(color1[3:5], 16)
    blue1 = int(color1[5:7], 16)
    red2 = int(color2[1:3], 16)
    green2 = int(color2[3:5], 16)
    blue2 = int(color2[5:7], 16)

    red = int(red1 * (1 - val) + red2 * val)
    green = int(green1 * (1 - val) + green2 * val)
    blue = int(blue1 * (1 - val) + blue2 * val)

    new_color = f"#{red:02x}{green:02x}{blue:02x}"

    return new_color

if __name__ == "__main__":
    print(mix("#ffaa00", "#0033ff", 0.8))