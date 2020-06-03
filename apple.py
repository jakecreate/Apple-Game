from graphics import *
# -----------------------------------------------------
# this code was screenshoted and created into an image
# made by @Eugene_Lee 2/29/2020

def get_apple(x, y):
    pic = []

    apx = x
    apy = y

    # STEM
    rectstem = Rectangle(Point(apx, apy), Point(apx + 5, apy + 20))
    rectstem.setOutline("BROWN")
    rectstem.setFill("BROWN")

    pic.append(rectstem)

    # stemerase = Oval(Point(apx - 9, apy - 5), Point(apx + 1, apy + 28))
    # stemerase.setOutline("WHITE")
    # stemerase.setFill("WHITE")

    # pic.append(stemerase)

    leaf = Polygon(Point(apx - 7, apy + 10), Point(apx + 3, apy + 24), Point(apx + 3, apy + 10), Point(apx - 3, apy))
    leaf.setFill("GREEN")
    leaf.setOutline("GREEN")

    pic.append(leaf)

    # CIRCLES OF APPLE
    appleleftcircle = Circle(Point(apx - 5, apy + 30), 15)
    appleleftcircle.setOutline("RED")
    appleleftcircle.setFill("RED")

    pic.append(appleleftcircle)

    applerightcircle = Circle(Point(apx + 10, apy + 30), 15)
    applerightcircle.setOutline("RED")
    applerightcircle.setFill("RED")

    pic.append(applerightcircle)

    # OVALS OF APPLE
    appleleftoval = Oval(Point(apx - 8, apy + 30), Point(apx + 8, apy + 55))
    appleleftoval.setOutline("RED")
    appleleftoval.setFill("RED")

    pic.append(appleleftoval)

    applerightoval = Oval(Point(apx - 3, apy + 30), Point(apx + 17, apy + 55))
    applerightoval.setOutline("RED")
    applerightoval.setFill("RED")

    pic.append(applerightoval)
    # OUTLINE LINES OF APPLE
    line = Polygon(Point(apx - 21, apy + 31), Point(apx - 7, apy + 54), Point(apx + 12, apy + 40),
                   Point(apx + 15, apy + 52), Point(apx + 25, apy + 31))
    line.setOutline("Red")
    line.setFill("RED")

    pic.append(line)


    return pic
