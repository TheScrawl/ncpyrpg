import curses
from curses import wrapper

def mapControl(screen, mapArray):
	#Draw Map
	for i in array:
		screen.addstr(y, x, i)
		y = y + 1

	playerX = 1
	playerY = 1
	
	

def main(masterWindow):
	masterWindow = curses.initscr()
	maxHeight = masterWindow.getmaxyx()[0]
	maxWidth = masterWindow.getmaxyx()[1]
	mapWindow = masterWindow.derwin(int(maxHeight / 2), maxWidth, 5, 5)
	while True:
		mapWindow.box()  
wrapper(main)
