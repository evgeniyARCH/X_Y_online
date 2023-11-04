from paint_isk_ris import *


def paint_text(text, x, y, mass):
    text = list(text)
    text_kol = len(text)
    nol = 0
    while nol < text_kol:
        coord_ris([text[nol], x, y], mass)
        x += 1
        nol += 1


def paint_rectangle(a, b, smb, x, y, mass):
    nol1 = 0
    while nol1 < b:

        nol = 0
        while nol < a:
            coord_ris([smb, x + nol, y], mass)
            nol += 1
        y += 1
        nol1 += 1


def paint_rectangle_nofill(a, b, smb, x, y, mass):
    nol = 0
    while nol < a:
        coord_ris([smb, x + nol, y], mass)
        nol += 1

    nol1 = 0
    while nol1 < b - 1:
        coord_ris([smb, x, y], mass)
        coord_ris([smb, x + a - 1, y], mass)
        y += 1
        nol1 += 1

    nol = 0
    while nol < a:
        coord_ris([smb, x + nol, y], mass)
        nol += 1


def paint_square(a, smb, x, y, mass):
    x = int(x)
    y = int(y)
    # a = int(input('введите сторону квадрата '))
    # smb = input('введите символ ')

    xsleft = int(x - (a - 1) / 2)
    xsright = int(x + (a - 1) / 2)
    xsup = int(x - (a - 1) / 2)
    xsdown = int(x - (a - 1) / 2)

    ysleft = int(y - (a - 1) / 2)
    ysright = int(y - (a - 1) / 2)
    ysup = int(y - (a - 1) / 2)
    ysdown = int(y + (a - 1) / 2)
    nol = 0
    while nol < a:
        coord_ris([smb, xsleft, ysleft], mass)
        coord_ris([smb, xsright, ysright], mass)
        ysright += 1
        ysleft += 1
        coord_ris([smb, xsup, ysup], mass)
        coord_ris([smb, xsdown, ysdown], mass)
        xsdown += 1
        xsup += 1
        nol += 1


def paint_sqare_ft(a, smb, x, y, mass):
    # a = int(input('введите диагональ '))
    # smb = input('введите символ ')
    xsup = int(x)
    xsdown = int(x)
    xsleft = int(x - (a - 1) / 2)
    xsright = int(x + (a - 1) / 2)

    ysup = int(y - (a - 1) / 2)
    ysdown = int(y + (a - 1) / 2)
    ysleft = int(y)
    ysright = int(y)

    nol = 0
    while nol < ((a - 1) / 2):
        coord_ris([smb, xsup, ysup], mass)
        xsup -= 1
        ysup += 1

        coord_ris([smb, xsdown, ysdown], mass)
        xsdown += 1
        ysdown -= 1

        coord_ris([smb, xsleft, ysleft], mass)
        xsleft += 1
        ysleft += 1

        coord_ris([smb, xsright, ysright], mass)
        xsright -= 1
        ysright -= 1
        nol += 1

