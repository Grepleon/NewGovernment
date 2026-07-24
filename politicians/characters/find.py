import politicians.politician as pol

def find_politicians(val:str, politicians: list[pol.Politician]) -> list[pol.Politician]:
    find_politicians:list[pol.Politician] = []
    for politician in politicians:
        if politician.find(val):
            find_politicians.append(politician)

    return find_politicians
