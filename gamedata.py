# Engine functions - do not touch
def drawArray(y, x, window, array): 
	for i in array: 
		window.addstr(y, x, i) 
		y = y + 1 

# Game Variables

playerY, playerX, = 4, 4 #Spawn Point

# Game Map Objects

house = [ 
	'##########',
	'#        #',
	'#        #',
	'#        #',
	'#        #',
	'#### #####',
	]

# User map
def drawmap(window):
	drawArray(2, 3, window, house)
	drawArray(2, 15, window, house)
