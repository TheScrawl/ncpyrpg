import curses
import math
from curses import wrapper

def drawArray(y, x, window, array):
	for i in array:
		window.addstr(y, x, i)
		y = y + 1
	
def mapControl(window):
	#Define map objects
	house = [
		'its a house',
		'###############',
		'#             #',
		'#             #',
		'#             #',
		'#             #',
		'####### #######', 
	]


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
	drawArray(2, 2, window, house)		
	
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
	mapWindow = curses.newwin(
		int(math.ceil(maxHeight / 2)), #Line count 
		int(math.ceil(maxWidth)), #Column Count
		0, #Start Y 
		0) #Start X
	menuWindow = curses.newwin(
		int(math.ceil(maxHeight / 2)), #Line Count
		int(math.ceil(maxWidth)), #Column Count
		int(math.ceil(maxHeight / 2)), #Start Y
		0) #Start X	

	#Main while loop
	while True:
		mapWindow.box()
		menuWindow.box()
		menuWindow.refresh()
		mapWindow.refresh()
		mapControl(mapWindow)

wrapper(main)
