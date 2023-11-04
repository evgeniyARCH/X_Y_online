import subprocess


def mass_gen_linux_auto():
    b = subprocess.check_output('tput lines', shell=True)
    a = subprocess.check_output('tput cols', shell=True)
    a = int(a)
    a = a / 2
    b = int(b)
    b = b - 1
    c = '.'
    massy = []
    nol = 0
    while nol < b:
        massy.append([])
        nol1 = 0
        while nol1 < a:
            massy[nol].append(c)
            nol1 += 1
        nol += 1
    mass = massy
    return mass



def mass_gen_custom(a,b,character):
    # a = 20
    # b = 20
    massy = []
    nol = 0
    while nol < b:
        massy.append([])
        nol1 = 0
        while nol1 < a:
            massy[nol].append(character)
            nol1 += 1
        nol += 1
    mass = massy
    return mass
