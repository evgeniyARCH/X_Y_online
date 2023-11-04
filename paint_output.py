import subprocess
import os

def clear_screen():
    os.system('clear')

def output_old(mass):
    clear_screen()
    nol = 0
    b = len(mass)
    while nol < b:
        ssb = []
        ssb = mass[nol]
        print(' '.join(ssb))
        nol += 1


def output(mass):
    b = subprocess.check_output('tput lines', shell=True)
    a = subprocess.check_output('tput cols', shell=True)
    a = int(a)
    a = a / 2
    b = int(b)
    b = b - 2
    mass_y = len(mass)
    mass_x = len(mass[0])
    mass_print_y = []
    if mass_x < a or mass_y < b:
        pass
    else:
        nol = 0
        while nol < b:
            mass_print_x = []
            nol1 = 0
            while nol1 < a:
                mass_print_x.append(mass[nol][nol1])
                nol1 += 1
            mass_print_y.append(mass_print_x)

            nol += 1

        nol = 0
        while nol < b:
            ssb = []
            ssb = mass_print_y[nol]
            print(' '.join(ssb))
            nol += 1


def output_paint(mass, a, b, filel):
    if a > 1000 or b > 2000:
        pass
    else:  
        r = open(filel, 'w')
        nol = 0
        while nol < b:
            nol1 = 0
            while nol1 < a:
                smb = mass[nol][nol1]
                r.write(smb)
                r.write(' ')
                nol1 += 1
            r.write('\n')
            nol += 1
        r.close()

def output_mass(mass, filel):
    r = open(filel, 'w')
    nol = 0
    while nol < len(mass):
        nol1 = 0
        while nol1 < len(mass[0]):
            smb = mass[nol][nol1]
            r.write(smb)
            r.write(' ')
            nol1 += 1
        r.write('\n')
        nol += 1
    r.close()


# def print_mass(filel):
#     r = open(filel,'r')
#     ms = r.readlines()
#     output_old(ms)
#     clear_screen()
#     nol = 0
#     b = len(ms)
#     while nol < b:
#         ssb = []
#         ssb = ms[nol]
#         print(' '.join(ssb))
#         nol += 1
#     r.close()

def print_mass(filel):
    r = open(filel,'r')
    print(r.read())
    r.close()



