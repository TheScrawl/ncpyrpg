import curses
import math
from curses import wrapper

def drawArray(y, x, window, array):
	for i in array:
		window.addstr(y, x, i)
		y = y + 1
	
def mapControl(window):
	#Define map objects
	array = ['its a house',	
			'###############',
			'#             #',
			'#             #',
			'#             #',
			'#             #',
			'####### #######', ]


	#Set player spawn point	
	playerX = 4
	playerY = 4
		
	#Set Curses settings
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

	#Draw map objects
	drawArray(2, 2, window, array)		
	
	#player movement	
	while True:
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				if chr(window.inch(playerY - 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY - 1, playerX, u'o')
					playerY = playerY - 1
				else: 
					pass
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, u'o')
					playerY = playerY + 1 
				else:
					pass
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, u'o')
					playerX = playerX - 1     
				else:
					pass
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, u'o') 
					playerX = playerX + 1   
				else:
					pass
		except(curses.error, ValueError):
			pass

def menuControl(window):

	#Set Curses settings
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

	#TODO: base menu system to build upon

def main(masterWindow):
	#Setup screens
	stdscr = curses.initscr()
	maxHeight, maxWidth = stdscr.getmaxyx()
	mapWindow = curses.newwin(int(math.ceil(maxHeight / 2)) , int(math.ceil(maxWidth)), 0, 0)
	menuWindow = curses.newwin(int(math.ceil(maxHeight / 2)), int(math.ceil(maxWidth)), int(math.ceil(maxHeight / 2)), 0)	
	

	#Main while loop
	while True:
		mapWindow.box()
		menuWindow.box()
		menuWindow.refresh()
		mapWindow.refresh()
		mapControl(mapWindow)

wrapper(main)
