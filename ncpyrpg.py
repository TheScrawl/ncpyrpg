import curses
import math
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
			
def mapControl(window, menuWindow):
	global playerX
	global playerY	
	#Set Curses settings
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

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
					window.addstr(playerY - 1, playerX, u'o')
					playerY = playerY - 1
				for i in mapObjList:
					if i.pos == (playerY - 1, playerX):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY - 1, playerX, 'o')
						playerY = playerY - 1
						for x in i.function:
							eval(x)	
				else: 
					pass
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, u'o')
					playerY = playerY + 1 
				for i in mapObjList:
					if i.pos == (playerY + 1, playerX):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY + 1, playerX, 'o')
						playerY = playerY + 1
						for x in i.function:
							eval(x)
				else:
					pass
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, u'o')
					playerX = playerX - 1     
				for i in mapObjList:
					if i.pos == (playerY, playerX - 1):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY, playerX - 1, 'o')
						playerX = playerX - 1
						for x in i.function:
							eval(x)	
				else:
					pass
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, u'o') 
					playerX = playerX + 1   
				for i in mapObjList:
					if i.pos == (playerY, playerX + 1):
						window.addch(playerY, playerX, ' ')
						window.addstr(playerY, playerX + 1, 'o')
						playerX = playerX + 1
						for x in i.function:
							eval(x)	
				else:
					pass
		except(curses.error, ValueError):
			pass

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

wrapper(main)
