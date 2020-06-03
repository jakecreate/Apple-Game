from graphics import *

x = 250

b_color = color_rgb(130, 255, 110)
r_color = color_rgb(123, 202, 123)

white = color_rgb(255, 250, 193)

def draw_borders(win):
    w_box = Rectangle(Point(244, 0), Point(751,600))
    w_box.setFill(white)
    w_box.setOutline(white)
    w_box.draw(win)
    bar = Rectangle(Point(244, 0), Point(249, 600))
    bar.setOutline("brown")
    bar.setFill("brown")
    bar.draw(win)

    bar2 = Rectangle(Point(746, 0), Point(751, 600))
    bar2.setOutline("brown")
    bar2.setFill("brown")
    bar2.draw(win)

    but1 = Rectangle(Point(x, 400), Point(x + 99, 499))
    but1.setFill(r_color)
    but1.setOutline('white')
    but1.draw(win)

    but2 = Rectangle(Point(x + 99, 400), Point(x + (99 * 2), 499))
    but2.setFill(r_color)
    but2.setOutline('white')
    but2.draw(win)

    but3 = Rectangle(Point(x + (99 * 2), 400), Point(x + (99 * 3), 499))
    but3.setFill(r_color)
    but3.setOutline('white')
    but3.draw(win)

    but4 = Rectangle(Point(x + (99 * 3), 400), Point(x + (99 * 4), 499))
    but4.setFill(r_color)
    but4.setOutline('white')
    but4.draw(win)

    but5 = Rectangle(Point(x + (99 * 4), 400), Point(x + (99 * 5), 499))
    but5.setFill(r_color)
    but5.setOutline('white')
    but5.draw(win)


def update_score(scr, win, l):
    sc = Text(Point(500, 50), f'{scr}')
    sc.setSize(20)
    l.append(sc)
    sbox = Rectangle(Point(475, 30), Point(525, 70))
    sbox.setFill("white")
    l.append(sbox)

    sbox.draw(win)
    sc.draw(win)


def rule_sheet(win):
    txbox = Rectangle(Point(758, 4), Point(997, 500))
    txbox.setFill('white')
    txbox.draw(win)
    rule = Text(Point(861, 260), """
            [Rules on how to play]  
        
        - There are 5 buttons. To score
         a point, click on the apple with
        the lowest altitude with the
        corresponding button according
        to column.
        
        - Every [25 points] will increase
        the the downfall speed of the
        apple.
        
        *It DOES NOT matter if the apple
        is on the button or not
        
        *IT DOES NOT matter if you click
        a button with an empty column
        
        - If the apple passes the buttons,
        you loose and the game ends.
        
        
        Good LUCK!
        
        (past 100 gets difficult)
        (Use a MOUSE)
          
    """)
    rule.setStyle('bold')
    rule.setSize(11)
    rule.draw(win)


def title_sheet(win):
    textbox = Rectangle(Point(5, 135), Point(240, 450))
    textbox.setFill('white')
    textbox.draw(win)
    rule1 = Text(Point(90, 150), """
           ~CATCH THAT APPLE!~
    """)
    rule1.setStyle('bold')
    rule1.setSize(15)
    rule1.draw(win)

    apple_title = Image(Point(120, 250), 'cartoonapple.png')
    apple_title.draw(win)

    rule1 = Text(Point(85, 340), """
               [Click ANYWHERE to START]
        """)
    rule1.setStyle('bold')
    rule1.setSize(13)
    rule1.draw(win)

    rule2 = Text(Point(85, 390), """
                made by - Jake Kim
                art credit - Eugene Lee
            """)
    rule2.setStyle('bold')
    rule2.setSize(11)
    rule2.draw(win)


rx = color_rgb(213, 70, 70)


def exit_button(win):
    yes_b = Rectangle(Point(754, 500), Point(1000, 600))
    yes_b.setFill(rx)
    yes_b.setOutline(rx)
    xy = yes_b.getCenter()
    yes_b.draw(win)

    exit_n = Text(Point(877, 550), 'EXIT')
    exit_n.setTextColor('white')
    exit_n.setStyle('bold italic')
    exit_n.setSize(36)
    exit_n.draw(win)
    return xy


def game_over(win, scr):
    clx = color_rgb(255, 241, 145)
    blox = Rectangle(Point(260, 250), Point(735, 350))
    blox.setFill(clx)
    blox.setOutline(clx)
    blox.draw(win)

    clr = color_rgb(188, 13, 30)

    gam2 = Text(Point(500, 330), f'Your Score: {scr}')
    gam2.setFace('courier')
    gam2.setStyle('bold')
    gam2.setTextColor('black')
    gam2.setSize(10)
    gam2.draw(win)

    gam = Text(Point(500, 300), 'GAME OVER')
    gam.setFace('courier')
    gam.setStyle('bold')
    gam.setTextColor(clr)
    gam.setSize(30)
    gam.draw(win)

# class Hit():
#     def __init__(self, centerx, centery, x1, y1, rangex, rangey):
#         self.centerx = centerx
#         self.centery = centery
#         self.x1 = x1
#         self.y1 = y1
#         self.rx = rangex
#         self.ry = rangey
#
#     def if_pressed(self):
#         xcond = abs(self.centerx - self.x1)
#         ycond = abs(self.centery - self.y1)
#
#         if xcond < self.rx and ycond < self.ry:
#             return True
#         else:
#             return False
