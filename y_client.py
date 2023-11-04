from paint_output import *
import time

nol = 0
while nol == 0:
    nol1 = 0
    while nol1 == 0:
        try:
            prov_y = open('x.txt', 'r')
            nol1 = 1
            prov_y.close()
        except:
            clear_screen()
            print('вы - y')
            print_mass('text.txt')
            print('сейчас ход противника')
        time.sleep(1)
    
    clear_screen()
    print('вы - y')
    print_mass('text.txt')
    print('сейчас ваш ход')
    command = str(input('введите клетку поля '))
    hod = open('hod.txt', 'w')
    hod.write(command)
    hod.close()
    x_or_y = open('x_or_y.txt','w')
    x_or_y.write('2')
    x_or_y.close()
    prov_x = open('y.txt', 'w')
    prov_x.close()
    # os.remove('x_or_y.txt')
    # os.remove('hod.txt')
    os.remove('x.txt')
    # try:
    #     os.remove('text.txt')
    # except:
    #     pass

    try:
        win = open('win_y.txt','r')
        print('YOU WIN!!!')
        nol = 1
        win.close()
    except:
        pass

    try:
        win = open('win_x.txt','r')
        print('You lose #')
        nol = 1
        win.close()
    except:
        pass
    
    try:
        win = open('close.txt','r')
        print('Close')
        nol = 1
        win.close()
    except:
        pass
    