import dill as pickle


#Important game function stuff, you probably shouldnt edit this
mapObjList = []

def drawArray(y, x, window, array):
	for i in array:
		window.addstr(y, x, i)
		y = y + 1

class mapObj(object):
	global mapObjList
	def __init__(self, char, posY, posX, function):
		self.char = char
		self.posY = posY
		self.posX = posX
		self.pos = (self.posY, self.posX)
		self.function = function
		mapObjList.append(self)	

## GAME VARIABLES - Feel free to edit and add things here
playerY, playerX, = 4, 4 #Spawn Point
gameWindowXSize = 40
gameWindowYSize = 28

## GAME MAP ARRAYS AND OBJECTS
# Arrays - These are objects you can draw


# Objects (char, y, x, function)

button = mapObj(
	['x'],
	5, 
	5, 
	[
	'menuOut("button pressed", menuWindow)',
	'window.addch(7, 6, " ")', 
	])

button2 = mapObj(
	['x'],
	5, 
	6, 
	[
	'menuOut("button2 pressed", menuWindow)'
	])

maze = ['#####################################', '#                                   #',
'# ################  ############### #', 
'# #    #     #   #  #   #    #    # #',
'# #    #     #   #  #   #    #    # #',
'# #    #     #   #  #   #    #    # #',
'# ############   #  #   #    #    # #', 
'# #    #     #   #  #   ########### #',
'# #    #     #####  #####    #    # #',
'# #    #     #          #    #    # #',
'# #    #     # ######## #    #    # #',
'# ############ #      # ########### #',
'#              #      #             #',
'# ############ #      # ########### #',
'# #    #  #  # #      # #    #    # #',
'# #    #  #  # ######## #    #    # #',
'# #    #  #  #          #    #    # #',
'# #    ###########  ######   #    # #',
'# ######    #    #  #    ########## #',
'# #    #    #    #  #    #   #    # #',
'# #    #    #    #  #    #   #    # #',
'# #    #    #    #  #    #   #    # #',
'# #    #    #    #  #    #   #    # #',
'# ################  ############### #',
'#                                   #',
'#####################################']


## USER MAP - put in all of the objects you want to draw and their locations
def drawmap(window):
	drawArray(1, 1, window, maze)
	drawArray(button.posY, button.posX, window, button.char)
	drawArray(button2.posY, button2.posX, window, button2.char)
	
#You need to put all of the variables you want in the game into this list
varList = ['mapObjList', 'gameWindowXSize', 'gameWindowYSize',  'playerY', 'playerX', 'maze', 'button', 'button2']

#Probably dont mess with this either
varDict = dict([i, eval(i)] for i in varList)
drawmapvar = drawmap

#You probably shouldnt touch this either
if __name__ == '__main__':
	print('Dumping game variables to gamefile...')
	pickle.dump(varDict, open('gamefile', 'wb'))
	print('Dumping functions to functionfile...')
	pickle.dump(drawmapvar, open('functionfile', 'wb'))
