import curses
import math
from curses import wrapper

array = [	'its a house',	
					'###############',
					'#             #',
					'#             #',
					'#             #',
					'#             #',
					'####### #######', ]
def mapControl(window, array):
	x = 2
	y = 2
	for i in array:
		window.addstr(y, x, i)
		y = y + 1	
		
	
	playerX = 4
	playerY = 4
		
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)  
	curses.use_default_colors()
	window.keypad(True)

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
def main(masterWindow):
	stdscr = curses.initscr()
	maxHeight, maxWidth = stdscr.getmaxyx()
	mapWindow = curses.newwin(int(math.ceil(maxHeight / 2)) , int(math.ceil(maxWidth)), 0, 0)
	while True:
		mapWindow.box()  
		mapWindow.refresh()
		mapControl(mapWindow, array)
wrapper(main)
