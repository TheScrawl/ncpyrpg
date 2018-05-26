import curses
import math
import gamedata
from curses import wrapper

def mapControl(window):
	
	#Set Curses settings
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

	playerY = gamedata.playerY
	playerX = gamedata.playerX

	#Draw map objects
	gamedata.drawmap(window)	

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
