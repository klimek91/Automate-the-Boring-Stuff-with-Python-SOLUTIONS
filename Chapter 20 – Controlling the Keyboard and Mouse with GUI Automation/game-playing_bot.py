# https://www.miniclip.com/games/sushi-go-round/pl/focus/
# opera size 1920x1080 size 125%

import pyautogui as pyg
import time, os
from PIL import ImageGrab, ImageOps
from numpy import *

os.makedirs('snap', exist_ok=True)
#pyg.mouseInfo()

x_pad = 450
y_pad = 226

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1001, y_pad + 747)
    im = ImageGrab.grab()
    im.save(os.path.join('snap', 'snap'+str(int(time.time())) + '.png'), 'PNG')
    return im

def startGame():
    pyg.click(939,547, duration=0.1)
    pyg.click(918,836, duration=0.1)
    pyg.click(1367,933, duration=0.1)
    pyg.click(940,814, duration=0.1)

class Cord:
    f_shrimp = 514, 751
    f_rice = 594, 745
    f_nori = 505, 831
    f_roe = 595, 821
    f_salmon = 507, 910
    f_unagi = 599, 902

    phone = 1371, 785

    menu_toppings = 1265, 656

    t_shrimp = 1222, 575
    t_nori = 1213, 659
    t_roe = 1360, 658
    t_salmon = 1222, 749
    t_unagi = 1349, 573
    t_exit = 1358, 760

    menu_rice = 1253, 686
    buy_rice = 1299, 668

    delivery_norm = 1221, 681

    fold_mat = 694,745

def makeFood(food):
    if food == 'onigiri':
        foodOnHand['rice'] -=2
        foodOnHand['nori'] -=1
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

    elif food == 'caliroll':
        foodOnHand['rice'] -=1
        foodOnHand['nori'] -=1
        foodOnHand['roe'] -=1
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

    elif food == 'caliroll':
        foodOnHand['rice'] -=1
        foodOnHand['nori'] -=1
        foodOnHand['roe'] -=2
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

def buyFood(food):
    if food == 'rice':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_rice)
        time.sleep(0.1)
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            time.sleep(0.1)
            print("Rice is available")
            time.sleep(0.1)
            pyg.click(Cord.buy_rice)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['rice']+=10
            time.sleep(2.5)
        else:
            print("No cash for rice")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        time.sleep(0.1)
        if s.getpixel(Cord.t_nori) != (53, 53, 39):
            time.sleep(0.1)
            print('Nori is available')
            time.sleep(0.1)
            pyg.click(Cord.t_nori)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(1)
        else:
            print("No cash for nori")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)
    if food == 'roe':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        time.sleep(0.1)
        if s.getpixel(Cord.t_roe) != (101, 13, 13):
            time.sleep(0.1)
            print('Roe is available')
            time.sleep(0.1)
            pyg.click(Cord.t_roe)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(1)
        else:
            print("No cash for roe")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)

def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1001, y_pad + 747)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolor())
    a = a.sum()
    return im

x1 = 508
x2 = 666
x3 = 824
x4 = 981
x5 = 1139
x6 = 1297
y1 = 307
y2 = 357

def get_seat_one():
    box = (x1, y1, x1+61, y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_one_'+str(int(time.time())) + '.png'), 'PNG')
    return a


def get_seat_two():
    box = (x2,y1, x2+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_two_' + str(int(time.time())) + '.png'), 'PNG')
    return a


def get_seat_three():
    box = (x3,y1,x3+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_three_' + str(int(time.time())) + '.png'), 'PNG')
    return a


def get_seat_four():
    box = (x4,y1,x4+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_four_' + str(int(time.time())) + '.png'), 'PNG')
    return a


def get_seat_five():
    box = (x5,y1,x5+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_five_' + str(int(time.time())) + '.png'), 'PNG')
    return a


def get_seat_six():
    box = (x6,y1,x6+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.path.join('snap', 'seat_six_' + str(int(time.time())) + '.png'), 'PNG')
    return a


def get_all_seats():
    print(get_seat_one() , ' seat one')
    print(get_seat_two(), ' seat two')
    print(get_seat_three(), ' seat three')
    print(get_seat_four(), ' seat foure')
    print(get_seat_five(), ' seat five ')
    print(get_seat_six(), ' seat six')

onigiri = []
caliroll = []
gunkan = []

for i in range(3850,4110):
    onigiri.append(i)

for i in range(4450,5100):
    caliroll.append(i)

for i in range(4120,4400):
    gunkan.append(i)

def sushiType(number):
    if number in onigiri:
        return 'onigiri'
    if number in caliroll:
        return 'caliroll'
    if number in gunkan:
        return 'gunkan'

def checkFood():
    for i,j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print("{} is low and need to restock".format(i))
                buyFood(i)

def clear_tables():
    pyg.click(591,556)
    pyg.click(759,550)
    pyg.click(912,553)
    pyg.click(1069,554)
    pyg.click(1226,557)
    pyg.click(1386,555)
    time.sleep(0.1)

class Blank:
    seat_1 = 10495
    seat_2 = 12478
    seat_3 = 12999
    seat_4 = 12713
    seat_5 = 13223
    seat_6 = 12206

def check_bubs():

    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        sushiType(s1)
        print('table 1 is occupied and needs %s' % sushiType(s1))
        makeFood(sushiType(s1))
    else:
        print('Table 1 unoccupied')
    clear_tables()
    checkFood()

    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        sushiType(s2)
        print('table 2 is occupied and needs %s' % sushiType(s2))
        makeFood(sushiType(s2))
    else:
        print('Table 2 unoccupied')
    clear_tables()
    checkFood()

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        sushiType(s3)
        print('table 3 is occupied and needs %s' % sushiType(s3))
        makeFood(sushiType(s3))
    else:
        print('Table 3 unoccupied')
    clear_tables()
    checkFood()

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        sushiType(s4)
        print('table 4 is occupied and needs %s' % sushiType(s4))
        makeFood(sushiType(s4))
    else:
        print('Table 4 unoccupied')
    clear_tables()
    checkFood()

    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        sushiType(s5)
        print('table 5 is occupied and needs %s' % sushiType(s5))
        makeFood(sushiType(s5))
    else:
        print('Table 5 unoccupied')
    clear_tables()
    checkFood()

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        sushiType(s6)
        print('table 6 is occupied and needs %s' % sushiType(s6))
        makeFood(sushiType(s6))
    else:
        print('Table 6 unoccupied')
    clear_tables()


def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()