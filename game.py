from paint_addons import *
from paint_isk_ris import *
from paint_mass_gen import *
from paint_output import *
import time

def poligon(symbol,mass):
    paint_rectangle(25, 25, symbol, 1, 1, mass)
    paint_rectangle(7, 7, ' ', 2, 2, mass)
    paint_rectangle(7, 7, ' ', 10, 2, mass)
    paint_rectangle(7, 7, ' ', 18, 2, mass)
    paint_rectangle(7, 7, ' ', 2, 10, mass)
    paint_rectangle(7, 7, ' ', 10, 10, mass)
    paint_rectangle(7, 7, ' ', 18, 10, mass)
    paint_rectangle(7, 7, ' ', 2, 18, mass)
    paint_rectangle(7, 7, ' ', 10, 18, mass)
    paint_rectangle(7, 7, ' ', 18, 18, mass)

def game_x(symbol,x,y,mass):
    # paint_rectangle(7, 7, ' ', x-3, y-3, mass)
    coord_ris([symbol,x,y], mass)
    coord_ris([symbol,x+1,y+1], mass)
    coord_ris([symbol,x+2,y+2], mass)
    coord_ris([symbol,x+1,y-1], mass)
    coord_ris([symbol,x+2,y-2], mass)
    coord_ris([symbol,x-1,y-1], mass)
    coord_ris([symbol,x-2,y-2], mass)
    coord_ris([symbol,x-1,y+1], mass)
    coord_ris([symbol,x-2,y+2], mass)

def game_y(symbol,x,y,mass):
    # paint_rectangle(7, 7, ' ', x-3, y-3, mass)
    coord_ris([symbol,x,y], mass)
    # coord_ris([symbol,x+1,y+1], mass)
    # coord_ris([symbol,x+2,y+2], mass)
    coord_ris([symbol,x+1,y-1], mass)
    coord_ris([symbol,x+2,y-2], mass)
    coord_ris([symbol,x-1,y-1], mass)
    coord_ris([symbol,x-2,y-2], mass)
    coord_ris([symbol,x-1,y+1], mass)
    coord_ris([symbol,x-2,y+2], mass)    

def game_hode(symbol,command,hode_mass,x_or_y,mass):
    if any(color in command for color in hode_mass):
        pass
    else:
        # try:
        #     command = int(command)
        # except:
        #     command = 0
        command = 1
        command = str(command)
        nol1 = 0
        while nol1 == 0:
            
            if any(color in command for color in hode_mass):
                nol1 = 1
            else:
                command = int(command)
                command+=1
                command = str(command)


    if x_or_y == 1:
        if command == '1':
            game_x(symbol, 5, 5, mass)
        elif command == '2':
            game_x(symbol, 13, 5, mass)
        elif command == '3':
            game_x(symbol, 21, 5, mass)
        elif command == '4':
            game_x(symbol, 5, 13, mass)
        elif command == '5':
            game_x(symbol, 13, 13, mass)
        elif command == '6':
            game_x(symbol, 21, 13, mass)
        elif command == '7':
            game_x(symbol, 5, 21, mass)
        elif command == '8':
            game_x(symbol, 13, 21, mass)
        elif command == '9':
            game_x(symbol, 21, 21, mass)
    elif x_or_y == 2:
        if command == '1':
            game_y(symbol, 5, 5, mass)
        elif command == '2':
            game_y(symbol, 13, 5, mass)
        elif command == '3':
            game_y(symbol, 21, 5, mass)
        elif command == '4':
            game_y(symbol, 5, 13, mass)
        elif command == '5':
            game_y(symbol, 13, 13, mass)
        elif command == '6':
            game_y(symbol, 21, 13, mass)
        elif command == '7':
            game_y(symbol, 5, 21, mass)
        elif command == '8':
            game_y(symbol, 13, 21, mass)
        elif command == '9':
            game_y(symbol, 21, 21, mass)

    nol = 0
    kol = len(hode_mass)
    while nol < kol:
        if command == hode_mass[nol]:
            if x_or_y == 1:
                hode_mass[nol] = 'x'
            elif x_or_y == 2:
                hode_mass[nol] = 'y'
        nol+=1    
    return hode_mass
            

def game(symbol,who_one):
    
    mass = mass_gen_custom(25, 25, symbol)
    poligon(symbol, mass)
    hode_mass = ['1','2','3','4','5','6','7','8','9']
    output_mass(mass, 'text.txt')

    try:
        os.remove('close.txt')
    except:
        pass
    try:
        os.remove('win_x.txt')
    except:
        pass
    try:
        os.remove('win_y.txt')
    except:
        pass
    try:
        os.remove('hod.txt')
    except:
        pass
    try:
        os.remove('x.txt')
    except:
        pass
    try:
        os.remove('y.txt')
    except:
        pass
    if who_one == 'x':
        w = open('y.txt','w')
        w.close()
    elif who_one == 'y':
        w = open('x.txt','w')
        w.close()
    

    nol = 0
    while nol == 0:
        x_win = []
        y_win = []
        nol2 = 0
        while nol2 == 0:
            time.sleep(0.1)
            try:
                r = open('hod.txt','r')
                command = str(r.read())
                nol2 = 1
            except:
                pass

        d = open('x_or_y.txt','r')
        # command = r.read()
        r.close()
        # OPEN IF FILES
        x_or_y = int(d.read())
        d.close()
        # command = 'dsfghfsd'


        hode_mass = game_hode(symbol,command, hode_mass, x_or_y, mass)
        output_mass(mass, 'text.txt')
        nol1 = 0
        kol1 = len(hode_mass)
        while nol1 < kol1:
            if hode_mass[nol1] == 'x':
                x_win.append(str(nol1+1))
            elif hode_mass[nol1] == 'y':
                y_win.append(str(nol1+1))
            nol1+=1 

        #X
    
        if any(color in '1' for color in x_win) and any(color in '2' for color in x_win) and any(color in '3' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()
        elif any(color in '4' for color in x_win) and any(color in '5' for color in x_win) and any(color in '6' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()
        elif any(color in '7' for color in x_win) and any(color in '8' for color in x_win) and any(color in '9' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()

        elif any(color in '1' for color in x_win) and any(color in '4' for color in x_win) and any(color in '7' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()
        elif any(color in '2' for color in x_win) and any(color in '5' for color in x_win) and any(color in '8' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()
        elif any(color in '3' for color in x_win) and any(color in '6' for color in x_win) and any(color in '9' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()

        elif any(color in '1' for color in x_win) and any(color in '5' for color in x_win) and any(color in '9' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()
        elif any(color in '3' for color in x_win) and any(color in '5' for color in x_win) and any(color in '7' for color in x_win):
            nol = 1
            win_x = open('win_x.txt','w')
            win_x.close()

        #Y

        elif any(color in '1' for color in y_win) and any(color in '2' for color in y_win) and any(color in '3' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()
        elif any(color in '4' for color in y_win) and any(color in '5' for color in y_win) and any(color in '6' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()
        elif any(color in '7' for color in y_win) and any(color in '8' for color in y_win) and any(color in '9' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()

        elif any(color in '1' for color in y_win) and any(color in '4' for color in y_win) and any(color in '7' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()
        elif any(color in '2' for color in y_win) and any(color in '5' for color in y_win) and any(color in '8' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()
        elif any(color in '3' for color in y_win) and any(color in '6' for color in y_win) and any(color in '9' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()

        elif any(color in '1' for color in y_win) and any(color in '5' for color in y_win) and any(color in '9' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()
        elif any(color in '3' for color in y_win) and any(color in '5' for color in y_win) and any(color in '7' for color in y_win):
            nol = 1
            win_x = open('win_y.txt','w')
            win_x.close()   
        else:
            pass


        if any(color in '1' for color in hode_mass) or any(color in '2' for color in hode_mass) or any(color in '3' for color in hode_mass) or any(color in '4' for color in hode_mass) or any(color in '5' for color in hode_mass) or any(color in '6' for color in hode_mass) or any(color in '7' for color in hode_mass) or any(color in '8' for color in hode_mass) or any(color in '9' for color in hode_mass):
            pass
        else:
            nol = 1
            close = open('close.txt','w')
            close.close()




        
        os.remove('x_or_y.txt')
        os.remove('hod.txt')
        print(x_win)
        print(y_win)

        
        

# game('#')
