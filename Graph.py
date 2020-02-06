from State import *
import turtle
import time
from main import board, final_state
import pygame, sys, random
from pygame.locals import *
from main import board
from turtle import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)


pygame.init()
Screen().screensize(1000, 500)
Screen().setup(width=1.0, height=1.0)
t = turtle.Turtle()
turtle.bgcolor("#033649")
t.speed('fastest')
turtle.speed('fastest')
t.penup()




BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3 # number of rows in the board
TILESIZE = 80
WINDOWWIDTH = 260
WINDOWHEIGHT = 260
FPS = 30

BGCOLOR = (3, 54, 73)
TILECOLOR = (  0, 204,   0)
TEXTCOLOR = (255, 255, 255)
BORDERCOLOR = (  0,  50, 255)
BASICFONTSIZE = 20


XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


def initialize():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, blankx, blanky

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                blankx = row
                blanky = col
   

def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back




def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return (x, y)


def makeMove(board, move):
    blankx, blanky = getBlankPosition(board)
    if move == UP:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]


def getLeftTopOfTile(row, col):
    left = XMARGIN + (col * TILESIZE) + (col - 1)
    top = YMARGIN + (row * TILESIZE) + (row - 1)
    return (left, top)


def drawTile(row, col, number, adjx=0, adjy=0):
    left, top = getLeftTopOfTile(row, col)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjy, top + adjx, TILESIZE, TILESIZE))
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjy, top + int(TILESIZE / 2) + adjx
    DISPLAYSURF.blit(textSurf, textRect)




def drawBoard(board):
    DISPLAYSURF.fill(BGCOLOR)
   
    for row in range(3):
        for col in range(3):
            if board[row][col]:
                drawTile(row, col, board[row][col])

    left, top = getLeftTopOfTile(0, 0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)


def slideAnimation(board, direction, animationSpeed):
    # Note: This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx - 1
        movey = blanky 
    elif direction == DOWN:
        movex = blankx + 1
        movey = blanky 
    elif direction == LEFT:
        movex = blankx
        movey = blanky - 1
    elif direction == RIGHT:
        movex = blankx
        movey = blanky + 1

    # prepare the base surface
    drawBoard(board)
    baseSurf = DISPLAYSURF.copy()
    # draw a blank space over the moving tile on the baseSurf Surface.
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        # animate the tile sliding over
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], i, 0)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], 0, -i)

        pygame.display.update()
        FPSCLOCK.tick(FPS)



def findParentReturn(move):
    if move == 'U':
        return 'D'
    elif move == 'D':
        return 'U'
    elif move == 'L':
        return 'R'
    elif move == 'R':
        return 'L'

def draw_rectangle(point, text, parent_point, fill_color, direction, md):
    color('black', fill_color)
    t.penup()
    if parent_point is not None:
        t.setposition(parent_point)
        t.pendown()
        t.setposition(point)
        t.penup()
    penup()
    setposition(point)
    begin_fill()
    pendown()
    forward(45) 
    right(90) 
    forward(90) 
    right(90) 
    forward(90) 
    right(90) 
    forward(90) 
    right(90) 
    forward(90)
    end_fill()
    t.penup()
    t.setposition(point)
    
    t.pendown()
    t.forward(45)
    t.right(90) 
    t.forward(90)
    t.right(90) 
    t.forward(90) 
    t.right(90) 
    t.forward(90) 
    t.right(90) 
    t.forward(60)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(45 )
    penup()
    setposition(point[0] - 40, point[1] - 115)
    write(text, font=("Arial", 19, "normal"))
    # t.penup()
    if md == float('inf'):
        setposition(point[0] - 70, point[1] - 45)
        write('{}\n'.format(direction), font=("Arial", 16, "normal"))
    
    elif parent_point is not None:
        setposition(point[0] - 70, point[1] - 45)
        write('{}\n{}'.format(direction, md), font=("Arial", 16, "normal"))
    else:
        setposition(point[0] - 65, point[1] - 25)
        write(md, font=("Arial", 16, "normal"))


class Graph:    

    def AstarTree(self, start):
        parent_position = (0, 260)
        left_end = -270
        current_depth = 230
        currentNode = start
        drawBoard(board)
        pygame.display.update()
        if currentNode.isGoalState():
            draw_rectangle([0, 350], currentNode.stateValue(), None, '#ffd700', '', currentNode.manhattanDistance())
        else:
            draw_rectangle([0, 350], currentNode.stateValue(), None, 'green', '', currentNode.manhattanDistance())
        direction = ['L', 'R', 'U', 'D']
        start = time.time()
        depth = 1
        visited = []
        returnParent = None
        while not currentNode.isGoalState():
            
            checkForQuit()
            pygame.display.update()
            visited.append(currentNode)
            mdistance = float('inf')
            level_nodes = 0
            drawn_green = []
            dist = 180
            goal = 0
            for u in currentNode.successors():
                goal += 1
                if u.isGoalState():
                    left_end += 315 - (45 + 90 * (goal - 1))
            for u in currentNode.successors():
                newMdistance = u.manhattanDistance()
                draw_rectangle([left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, 'white', direction[level_nodes], newMdistance + depth)                
                if u.isGoalState():
                    draw_rectangle([left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, '#ffd700', direction[level_nodes], newMdistance + depth)
                    currentNode = u
                    for i in drawn_green:
                        draw_rectangle(i[0], i[1], i[2], i[3], i[4], i[5])
                        drawn_green = drawn_green[1:]
                    
                    slideAnimation(board, direction[level_nodes], 8)
                    makeMove(board, direction[level_nodes])
                    drawBoard(board)
                    pygame.display.update()
                    break
                elif u in visited:
                    draw_rectangle([left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, 'red', direction[level_nodes], newMdistance + depth)    
                elif mdistance > newMdistance:
                    draw_rectangle([left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, 'green', direction[level_nodes], newMdistance + depth)
                    for i in drawn_green:
                        draw_rectangle(i[0], i[1], i[2], i[3], i[4], i[5])
                        drawn_green = drawn_green[1:]
                        slideAnimation(board, returnParent, 8)
                        makeMove(board, returnParent)
                        drawBoard(board)
                        pygame.display.update()
                        

                    drawn_green.append([[left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, 'red', direction[level_nodes], newMdistance + depth])
                    
                        
                    slideAnimation(board, direction[level_nodes], 8) 
                    makeMove(board, direction[level_nodes])
                    drawBoard(board)
                    pygame.display.update()
                    
                    returnParent = findParentReturn(direction[level_nodes])
                    new_node = u
                    mdistance = newMdistance
                    new_parent_position = (left_end + level_nodes * dist, current_depth - 90)
                    new_left_end = left_end + level_nodes * dist - 270
                else:
                    draw_rectangle([left_end + level_nodes * dist, current_depth], u.stateValue(), parent_position, 'red', direction[level_nodes], newMdistance + depth)             
               

                level_nodes += 1
            else:
                left_end = new_left_end
                parent_position = new_parent_position
                current_depth -= 120
                currentNode = new_node
                depth += 1
            
        end = time.time()
        t.penup()
        penup()
        setposition(-300, 250)
        pendown()
        write("Expanded Node: {0} \nTime Taken: {1:.2f}".format(depth, (end - start)), font=("Arial", 19, "normal"))
        penup()
        setposition(1000, 1000)
        t.setposition(1000, 1000)

        while True:
            drawBoard(board)
            checkForQuit()
            pygame.display.update()
   
