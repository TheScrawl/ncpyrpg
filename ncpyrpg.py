import curses
import math
import time
import dill as pickle
from curses import wrapper

class mapObj(object):
  global mapObjList
  def __init__(self, char, posY, posX, function):
    self.char = char
    self.posY = posY
    self.posX = posX
    self.pos = (self.posY, self.posX)
    self.function = function
    mapObjList.append(self)

class mapEntity(object):
    def __init__(self, movepath, body, speed, contactFunctions):
        self.movepath = movepath
        self.body = body
        self.speed = speed
        self.contactFunctions = contactFunctions
    
def spawn(entity, window, xPos, yPos):
        window.addstr(yPos, xPos, entity.body)
        for i in entity.movepath:
            for x in range(i[1]):
                window.addstr(yPos, xPos, ' ')
                if i[0] == 'up': 
                    yPos = yPos + 1
                if i[0] == 'down': 
                    yPos = yPos - 1
                if i[0] == 'left': 
                    xPos = xPos - 1
                if i[0] == 'right': 
                    xPos = xPos + 1
                window.addstr(yPos, xPos, entity.body)

badguy = mapEntity(
        [('up', 3), ('left', 3), ('down', 3)],
        u'卍',
        0.1,
        ['exit(0)']
        )

def drawArray(y, x, window, array): 
  for i in array: 
   window.addstr(y, x, i) 
   y = y + 1 

drawmap = None
playerX = None
playerY = None

def loadGame():
	global drawmap
	global playerX
	global playerY
	with open('gamefile', 'rb') as f:
		varDict = pickle.load(f)
		globals().update(varDict)
	with open('functionfile', 'rb') as f:
		drawmap = pickle.load(f)	
		
menuPos = 1
menuHistory = [' ']

def menuOut(string, window):
	global menuPos
	global menuHistory
	window.addstr(1, 1, ' '*len(menuHistory[-1]))
	window.addstr(1, 1, string)
	menuPos = menuPos + 1
	for i in menuHistory:
		window.addstr(menuPos,1, i)
	menuHistory.append(string)
	
def mapControl(window, menuWindow):
	global playerX
	global playerY	
	#Set Curses settings
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

<<<<<<< Updated upstream
	#Draw map objects
	drawmap(window)	
	#player movement	
	while True:
		menuWindow.refresh()
		window.refresh()
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				if chr(window.inch(playerY - 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY - 1, playerX, 'o')
					playerY = playerY - 1
				for i in mapObjList:
					if i.pos == (playerY - 1, playerX):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY - 1, playerX, 'o')
						playerY = playerY - 1
						for x in i.function:
							eval(x)	
						break
				else: 
					pass
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, 'o')
					playerY = playerY + 1 
				for i in mapObjList:
					if i.pos == (playerY + 1, playerX):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY + 1, playerX, 'o')
						playerY = playerY + 1
						for x in i.function:
							eval(x)
						break
				else:
					pass
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, 'o')
					playerX = playerX - 1     
				for i in mapObjList:
					if i.pos == (playerY, playerX - 1):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY, playerX - 1, 'o')
						playerX = playerX - 1
						for x in i.function:
							eval(x)
						break	
				else:
					pass
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, 'o') 
					playerX = playerX + 1   
				for i in mapObjList:
					if i.pos == (playerY, playerX + 1):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY, playerX + 1, 'o')
						playerX = playerX + 1
						for x in i.function:
							eval(x)	
						break
				else:
					pass
		except(curses.error, ValueError):
			pass
=======
    #Draw map objects
    drawmap(window)	
    #player movement	
    while True:
        menuWindow.refresh()
        window.refresh()
        keypress = window.getch()
        try:
            if keypress == ord('w'):
                if chr(window.inch(playerY - 1, playerX)) == ' ':
                    window.addch(playerY, playerX, ' ')
                    window.addstr(playerY - 1, playerX, 'o')
                    playerY = playerY - 1
                elif chr(window.inch(playerY - 1, playerX)) != ' ':
                     for i in mapObjList:
                        if i.pos == (playerY - 1, playerX):
                            window.addch(playerY, playerX, ' ')
                            window.addstr(playerY - 1, playerX, 'o')
                            playerY = playerY - 1
                            for x in i.function:
                                eval(x)	
                                mapObjList.remove(i)
                            break
                else: 
                    pass
            if keypress == ord('s'):
                if chr(window.inch(playerY + 1, playerX)) == ' ':
                    window.addch(playerY, playerX, ' ')
                    window.addstr(playerY + 1, playerX, 'o')
                    playerY = playerY + 1 

                elif chr(window.inch(playerY + 1, playerX)) != ' ':
                    for i in mapObjList:
                        if i.pos == (playerY + 1, playerX):
                            window.addch(playerY, playerX, ' ')
                            window.addstr(playerY + 1, playerX, 'o')
                            playerY = playerY + 1
                            for x in i.function:
                                eval(x)
                                mapObjList.remove(i)
                            break
                else:
                    pass
            if keypress == ord('a'):
                if chr(window.inch(playerY, playerX - 1)) == ' ':
                    window.addch(playerY, playerX, ' ')
                    window.addstr(playerY, playerX - 1, 'o')
                    playerX = playerX - 1     
                elif chr(window.inch(playerY, playerX - 1)) != ' ':
                    for i in mapObjList:
                        if i.pos == (playerY, playerX - 1):
                            window.addch(playerY, playerX, ' ')
                            window.addstr(playerY, playerX - 1, 'o')
                            playerX = playerX - 1
                            for x in i.function:
                                eval(x)
                                mapObjList.remove(i)
                            break	
                else:
                    pass
            if keypress == ord('d'):
                if chr(window.inch(playerY, playerX + 1)) == ' ':
                    window.addch(playerY, playerX, ' ')
                    window.addstr(playerY, playerX + 1, 'o') 
                    playerX = playerX + 1   
                elif chr(window.inch(playerY, playerX + 1)) != ' ':
                    for i in mapObjList:
                        if i.pos == (playerY, playerX + 1):
                            window.addch(playerY, playerX, ' ')
                            window.addstr(playerY, playerX + 1, 'o')
                            playerX = playerX + 1
                            for x in i.function:
                                eval(x)	
                                mapObjList.remove(i)
                            break
                else:
                    pass
        except(curses.error, ValueError):
            pass
>>>>>>> Stashed changes

def main(masterWindow):
	#Setup screens
	loadGame()
	stdscr = curses.initscr()
	maxHeight, maxWidth = stdscr.getmaxyx()

	mapWindow = curses.newwin(
		gameWindowYSize,
		gameWindowXSize,
		0,
		0)	

<<<<<<< Updated upstream
	menuWindow = curses.newwin(
		int(math.ceil(maxHeight - gameWindowYSize)), #Line Count
		int(math.ceil(maxWidth)), #Column Count
		int(math.ceil(gameWindowYSize)), #Start Y
		0) #Start X	

	#Main while loop
	while True:
		mapWindow.box()
		menuWindow.box()
		mapControl(mapWindow, menuWindow)

=======


    menuWindow = curses.newwin(
        int(math.ceil(maxHeight - gameWindowYSize)), #Line Count
        int(math.ceil(maxWidth)), #Column Count
        int(math.ceil(gameWindowYSize)), #Start Y
        0) #Start X	

    #Main while loop
    while True:
        mapWindow.box()
        menuWindow.box()
        mapControl(mapWindow, menuWindow)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
wrapper(main)
