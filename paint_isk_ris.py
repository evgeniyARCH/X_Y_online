def coord_isk(coord, mass):
    x_coord = coord[0]
    y_coord = coord[1]
    x_massive = mass[y_coord - 1]
    symbol = x_massive[x_coord - 1]
    return symbol


def coord_ris(cords_and_symbol: list, mass: list):
    x_coord = cords_and_symbol[1]
    y_coord = cords_and_symbol[2]
    current_symbol = str(cords_and_symbol[0])
    x_massive = mass[y_coord - 1]
    x_massive[x_coord - 1] = current_symbol
    return mass







def chislo_prov(prov, text):  # Боюсь менять, ибо может сломаться, но почему именно так?
    nol = 1
    while nol == 1:
        prov = input(text)
        try:
            prov = int(prov)
            nol = 0
            return prov
        except ValueError:
            print("это не число")


# Мое предложение:
def check_num(string: str):
    integer = int
    try:
        integer = int(string)
    except ValueError:
        print("Not integer")
        return None
    return integer
