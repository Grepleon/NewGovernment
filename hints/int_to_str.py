def int_to_str(number:int) -> str:
    return f"{number:,}".replace(",", " ")

if __name__ == "__main__":
    print(int_to_str(int(input())))