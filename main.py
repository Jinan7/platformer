# Welcome to the twisted mind of j1nx
# Hope I inspire you😉

import pygame, sys, math
from pygame.locals import *

GAMEWORLD = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

WINDOWX = 600  # width of game window
WINDOWY = 600  # height of game window
FRAMEX = 10  # number of displayed cells in x-axis
FRAMEY = len(GAMEWORLD)  # number of displayed cells in y-axis
CELLX = math.ceil(WINDOWX / FRAMEX)  # width of a cell
CELLY = math.ceil(WINDOWY / FRAMEY)  # height of a cell
BALLRADIUS = CELLY / 2
MARKERPOS = BALLRADIUS - 5
MARKERRADIUS = 3
GLIDERWIDTH = CELLX
GLIDERHEIGHT = 5

FRAMERATE = 60

# collision Arrays
ALLRESTRICTEDX = []
ALLRESTRICTEDY = []
RESTRICTEDX = []
RESTRICTEDY = []
GLIDEDONX = []
GLIDEDONY = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 79, 57)
SKYBLUE = (135, 206, 235)
GRAY = (211, 211, 211)
BALLCOLOR = BLACK
MARKCOLOR = GRAY
BACKGROUND = SKYBLUE
CELLCOLOR = BROWN

# navigation
xVELOCITY = 3
FALLSPEED = 0.3
STATIC = WINDOWX / 2
MAXDISPLACEMENT = (len(GAMEWORLD[0]) - FRAMEX) * CELLX
GRAVITY = 1  # acceleration due to gravity
RIGHT = 'right'
LEFT = 'left'
BOTH = 'both'
HEIGHT = 100
STOPHEIGHT = 2

# glide constants
GLIDEAMPLITUDE = CELLX * 2
GLIDESPEED = 0.03


def main():
    pygame.init()
    # Display and timers
    global GAMEWINDOW, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    GAMEWINDOW = pygame.display.set_mode((WINDOWX, WINDOWY))
    pygame.display.set_caption('Bouncy')

    # Movement variables
    global ballx, bally, screenDisplacement, angularDisplacement, theta, markx, marky
    global isGliding
    ballx = BALLRADIUS
    bally = BALLRADIUS
    moveRight = False
    moveLeft = False
    isGliding = False
    screenDisplacement = 0
    angularDisplacement = [0, math.pi]
    theta = 0

    # Gravity and jump variables
    global time, landed, isJumping, height, fallHeight
    isJumping = False
    landed = False
    time = 0
    height = HEIGHT
    fallHeight = 0


    # Start Animation
    getRestricted()
    while not landed:
        gravity()
        drawWorld()
        drawBall(ballx, bally)
        FPSCLOCK.tick(FRAMERATE)
        pygame.display.update()

    # Game Loop
    while True:
        # event handlers
        for event in pygame.event.get():

            # Quit Event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #  Movement Event
            if event.type == KEYDOWN and event.key == K_RIGHT:
                moveRight = True
            if event.type == KEYUP and event.key == K_RIGHT:
                moveRight = False
            if event.type == KEYDOWN and event.key == K_LEFT:
                moveLeft = True
            if event.type == KEYUP and event.key == K_LEFT:
                moveLeft = False
            if event.type == KEYDOWN and event.key == K_UP:
                isJumping = True

        # movement
        gravity()
        if moveRight:
            move(RIGHT)
        if moveLeft:
            move(LEFT)
        if isJumping:
            jump()
        if isGliding:
            glide(glideType)
        adjustX(BOTH)

        # move glider
        for i in range(len(angularDisplacement)):
            angularDisplacement[i] = (angularDisplacement[i] + GLIDESPEED) % (2 * math.pi)

        # update Screen
        drawWorld()
        drawBall(ballx, bally)
        FPSCLOCK.tick(FRAMERATE)
        pygame.display.update()


def drawWorld():
    GLIDEDONX.clear()
    GAMEWINDOW.fill(BACKGROUND)
    # for x in range(screenDisplacement//CELLX, (FRAMEX+1) + screenDisplacement//CELLX):
    for x in range(len(GAMEWORLD[0])):
        for y in range(FRAMEY):
            if GAMEWORLD[y][x] == 1:
                drawCell(x, y)
            elif GAMEWORLD[y][x] == 2:
                drawGlider(x, y, angularDisplacement[0], 2)
            elif GAMEWORLD[y][x] == 3:
                drawGlider(x, y, angularDisplacement[1], 3)


def drawGlider(x, y, angle, glidetype):
    global isGliding, ballx, glideType
    left, top = getLeftTop(x, y)
    displacement = math.sin(angle) * GLIDEAMPLITUDE
    left = left + displacement

    for X in range(int(left), int(left) + GLIDERWIDTH + 1):
        section = []
        for Y in range(top, top + GLIDERHEIGHT + 1):
            section.append([X, Y, glidetype])
        GLIDEDONX.append(section)

    # for Y in range(top, top + GLIDERHEIGHT + 1):
    #     section = []
    #     for X in range(int(left), int(left) + GLIDERWIDTH + 1):
    #         section.append([X, Y, angle])
    #         GLIDEDONY.append(section)
    pygame.draw.rect(GAMEWINDOW, WHITE, (left, top, GLIDERWIDTH, GLIDERHEIGHT))


def glide(glidetype):
    global ballx
    if glidetype == 2:
        deltaX = (math.sin(angularDisplacement[0]) - math.sin(angularDisplacement[0] - GLIDESPEED)) * GLIDEAMPLITUDE
    elif glidetype == 3:
        deltaX = (math.sin(angularDisplacement[1]) - math.sin(angularDisplacement[1] - GLIDESPEED)) * GLIDEAMPLITUDE
    ballx = ballx + deltaX
    # isGliding = False


def drawCell(x, y):
    left, top = getLeftTop(x, y)
    pygame.draw.rect(GAMEWINDOW, CELLCOLOR, (left, top, CELLX, CELLY))


def getRestricted():
    global RESTRICTEDX
    global RESTRICTEDY
    tempRESTRICTEDX = []
    tempRESTRICTEDY = []

    # Get the left, top coordinate of every restricted cell
    for x in range(len(GAMEWORLD[0])):
        for y in range(len(GAMEWORLD)):
            if GAMEWORLD[y][x] == 1:
                left, top = getLeftTop(x, y)

                # Get all coordinate pairs occupied by every cell and add them to a temporary list
                for X in range(left, left + CELLX + 1):
                    section = []
                    for Y in range(top, top + CELLY + 1):
                        section.append([X, Y])
                    tempRESTRICTEDX.append(section)

                for Y in range(top, top + CELLY + 1):
                    section = []
                    for X in range(left, left + CELLX + 1):
                        section.append([X, Y])
                    tempRESTRICTEDY.append(section)

    # Group all coordinate pairs with similar x  values
    groupRestricted(len(GAMEWORLD[0]) * CELLX, 0, tempRESTRICTEDX)

    # Group all coordinate pairs with similar y  values
    groupRestricted(WINDOWY, 1, tempRESTRICTEDY)

    splitGroups(RESTRICTEDX, 1)
    splitGroups(RESTRICTEDY, 0)


def groupRestricted(numOfGroups, pos, tempRESTRICTED):
    global RESTRICTEDX
    global RESTRICTEDY
    for i in range(numOfGroups + 1):
        section = []
        for X in tempRESTRICTED:
            if X[0][pos] == i:
                section += X
        if len(section) == 0:
            continue
        if pos == 0:
            RESTRICTEDX.append(section)
        elif pos == 1:
            RESTRICTEDY.append(section)


def splitGroups(RESTRICTED, pos):
    global ALLRESTRICTEDX, ALLRESTRICTEDY
    temp = []
    for X in RESTRICTED:
        altered = False
        start = 0
        initial = X[0][pos]
        for Y in X:
            if Y[pos] - initial > 1:
                altered = True
                column = X[start:X.index(Y)]
                temp.append(column)
                start = X.index(Y)
            initial = Y[pos]
        if altered:
            column = X[start:]
            temp.insert(0, column)
        else:
            temp.append(X)
    for X in temp:
        if len(X) == 0:
            temp.remove(X)
    if pos == 0:
        ALLRESTRICTEDY = temp.copy()
    elif pos == 1:
        ALLRESTRICTEDX = temp.copy()


def drawBall(x, y):
    global markx, marky, theta

    markx = MARKERPOS * math.sin(theta)
    marky = MARKERPOS * math.cos(theta)
    pygame.draw.circle(GAMEWINDOW, BALLCOLOR, (x, y), BALLRADIUS)
    pygame.draw.circle(GAMEWINDOW, MARKCOLOR, (x + markx, y - marky), MARKERRADIUS)


def getLeftTop(x, y):
    left = x * CELLX - screenDisplacement
    top = y * CELLY
    return left, top


def gravity():
    global bally, ballx
    global time
    global landed
    global isJumping
    global glideType, isGliding
    global fallHeight, height

    if not isJumping:

        initial = -GRAVITY * (
                time ** 2)  # ydisplacement equals minus acceleration due to gravity multiplied time squared
        time += FALLSPEED
        final = -GRAVITY * (
                time ** 2)  # ydisplacement equals minus acceleration due to gravity multiplied time squared
        deltaY = final - initial
        fallHeight += math.fabs(deltaY)

        initialBottom = bally + BALLRADIUS
        bally = bally - deltaY
        bottom = bally + BALLRADIUS

        for X in ALLRESTRICTEDX:  # check if bottom coordinate of ball is in a restricted area
            if int(ballx) == X[0][0] - screenDisplacement and initialBottom <= X[0][1] <= bottom:
                landed = True  # only needed for starting animation of game
                time = 0  # reset time to 0
                bottom = X[0][
                    1]  # adjust bottom coordinate to surface of restricted zone
                bally = bottom - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate
                height = math.sqrt(fallHeight)
                if height < STOPHEIGHT:
                    isJumping = False
                    height = HEIGHT
                else:
                    isJumping = True
                fallHeight = 0
                break
            else:
                landed = False
        for X in GLIDEDONX:  # check if bottom coordinate of ball is in a restricted area
            if int(ballx) == X[0][0] and initialBottom <= X[0][1] <= bottom:
                landed = True
                isGliding = True
                glideType = X[0][2]
                time = 0  # reset time to 0
                bottom = X[0][
                    1]  # adjust bottom coordinates to surface of restricted zone
                bally = bottom - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate
                break
            else:
                isGliding = False


def move(direction):
    global ballx, screenDisplacement
    global markx, marky, theta
    left = ballx - BALLRADIUS
    right = ballx + BALLRADIUS

    if direction == 'right':
        if ballx > STATIC and screenDisplacement != MAXDISPLACEMENT:
            screenDisplacement += xVELOCITY
        elif right < WINDOWX:
            ballx += xVELOCITY
        adjustX(RIGHT)
        if not isJumping and landed:
            theta += (xVELOCITY / (BALLRADIUS)) % (2 * math.pi)
        elif height == 100:
            theta -= 0.03 % 360
    elif direction == 'left':
        if ballx < STATIC and screenDisplacement != 0:
            screenDisplacement -= xVELOCITY
        elif left > 0:
            ballx -= xVELOCITY
        adjustX(LEFT)
        if not isJumping and landed:
            theta -= (xVELOCITY / (BALLRADIUS)) % (2 * math.pi)
        elif height == 100:
            theta += 0.03 % 360


def adjustX(direction):
    global ballx, isJumping, time, screenDisplacement, isGliding
    left = ballx - BALLRADIUS
    right = ballx + BALLRADIUS

    # if not isGliding:
    if ballx > STATIC and screenDisplacement != MAXDISPLACEMENT:
        screenDisplacement += xVELOCITY
        ballx -= xVELOCITY
    if ballx < STATIC and screenDisplacement != 0:
        screenDisplacement -= xVELOCITY
        ballx += xVELOCITY
    if direction == 'right' or direction == 'both':
        for X in ALLRESTRICTEDY:
            if [math.ceil(right) + screenDisplacement, int(bally)] in X:
                right = X[0][0] - screenDisplacement - 1  # minus 1 ensures ball is not always in block
                ballx = right - BALLRADIUS
                isJumping = False
                time = 0
                break
        if right > WINDOWX:
            ballx = WINDOWX - BALLRADIUS
            isJumping = False
            time = 0

    if direction == 'left' or direction == 'both':
        for X in ALLRESTRICTEDY:
            if [math.floor(left) + screenDisplacement, int(bally)] in X:
                left = X[len(X) - 1][0] - screenDisplacement + 1
                ballx = left + BALLRADIUS
                isJumping = False
                time = 0
                break
        if left < 0:
            ballx = 0 + BALLRADIUS
            isJumping = False
            time = 0


def jump():
    global time, bally, isJumping, isGliding, glideType, height, fallHeight
    initial = -GRAVITY * ((time - math.sqrt(height)) ** 2) + height
    time += FALLSPEED
    final = -GRAVITY * ((time - math.sqrt(height)) ** 2) + height
   # final = -GRAVITY * (time ** 2) + 20 * time
    deltaY = final - initial
    isAscending = deltaY >= 0
    isDescending = deltaY <= 0

    initialTop = bally - BALLRADIUS
    initialBottom = bally + BALLRADIUS

    bally = bally - deltaY

    top = bally - BALLRADIUS
    bottom = bally + BALLRADIUS

    if isAscending:  # if ball is moving upwards
        for X in ALLRESTRICTEDX:
            if int(ballx) == X[0][0] - screenDisplacement and initialTop >= X[len(X) - 1][1] >= top:
                time = 0  # reset time
                top = X[len(X) - 1][1]
                bally = top + BALLRADIUS
                isJumping = False
                break
        for X in GLIDEDONX:  # check if bottom coordinate of ball is in a restricted area
            if int(ballx) == X[0][0] and initialTop >= X[len(X) - 1][1] >= top:
                isJumping = False
                time = 0  # reset time to 0
                top = X[len(X) - 1][1]
                bally = top + BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate
                break

    if isDescending:  # if ball is moving downwards
        fallHeight += math.fabs(deltaY)
        for X in ALLRESTRICTEDX:
            if int(ballx) == X[0][0] - screenDisplacement and initialBottom <= X[0][1] <= bottom:
                height = math.sqrt(fallHeight)
                if height < STOPHEIGHT:
                    isJumping = False
                    height = HEIGHT
                time = 0  # reset time
                bottom = X[0][1]
                bally = bottom - BALLRADIUS
                fallHeight = 0
                break
        for X in GLIDEDONX:  # check if bottom coordinate of ball is in a restricted area
            if int(ballx) == X[0][0] and initialBottom <= X[0][1] <= bottom:
                isJumping = False
                height = HEIGHT
                isGliding = True
                glideType = X[0][2]
                time = 0  # reset time to 0
                bottom = X[0][
                    1]  # adjust bottom coordinates to surface of restricted zone
                bally = bottom - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate
                break
            else:
                isGliding = False


if __name__ == '__main__':
    main()
