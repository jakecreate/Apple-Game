from graphics import *
from random import randint
from time import sleep
import pad
# ------------------ made by @jake_kim 2/29/2020.
# ------------------ Apple Drawing credit: @Eugene_Lee 2/29/2020.

# constructs a window
window = GraphWin("Catch That Apple", 1000, 600, autoflush=False)
window.setBackground('black')
# defined
slot = [300, 400, 500, 600, 700]
xcord = randint(0, 9)
ycord = -30
basket = []
scoreboard = []

# per
a = 0
spd = 0.06

# hit box on buttons
ybox = 450

# life not used.. yet
life = 3
scr = 0

# draw preset
pad.draw_borders(window)
score = pad.update_score(scr, window, scoreboard)
pad.rule_sheet(window)
pad.title_sheet(window)

# start game
window.getMouse()
# ----------
while True:
    # new slot
    if a % 10 == 0:
        xcord = randint(0, 4)
        if a < 1000:
            apple = Image(Point(slot[xcord], ycord), 'eugene.png')
        elif a > 990:
            apple = Image(Point(slot[xcord], ycord), 'neatapple.png')
        apple.draw(window)
        basket.append(apple)
    a += 1

    # movement

    for x in range(len(basket)):
        for b in range(10):
            basket[x].move(0, 1)

    # coord for apple
    if len(basket) > 0:
        last_apple = basket[0].getAnchor()
        lx = last_apple.getX()
        ly = last_apple.getY()

    # coord for mouse
    mouse = window.checkMouse()
    if mouse is None:
        pass
    else:
        mx = mouse.getX()
        my = mouse.getY()

        xcondition = abs(mx - lx)
        ycondition = abs(my - ly)

        if xcondition < 49 and len(basket) > 0 and 399 < my < 500:
            basket[0].undraw()
            basket.pop(0)
            scr += 1
            pad.update_score(scr, window, scoreboard)
            # remove previous 14 scorebox for less lagg
            if scr % 15 == 0:
                for x in range(len(scoreboard) - 2):
                    scoreboard[x].undraw()
                for x in range(len(scoreboard) - 2):
                    scoreboard.pop()

    # if it hits the mouse or floor



    if ly > 500:
        basket[0].undraw()
        basket.pop(0)
        break

    # fps
    sleep(spd)
    if a > 1000:
        spd = 0.025
    elif a > 2000:
        spd = 0.02
    elif a % 250 == 0:
        spd -= 0.01

    # refresh frame
    update()
# Game over msg
pad.game_over(window, scr)

# get hit-box of button
ex = pad.exit_button(window)
exX = ex.getX()
exY = ex.getY()


# waits for user to click
while True:
    mouse1 = window.getMouse()
    if mouse1 is None:
        pass
    else:
        mx1 = mouse1.getX()
        my1 = mouse1.getY()

    xcond = abs(mx1 - exX)
    ycond = abs(my1 - exY)

    if xcond < 123 and ycond < 50:
        break
    else:
        pass

window.close()
