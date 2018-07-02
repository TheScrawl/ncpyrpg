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
playerY, playerX, = 1, 1 #Spawn Point
gameWindowXSize = 40
gameWindowYSize = 20

## GAME MAP ARRAYS AND OBJECTS
# Arrays - These are objects you can draw


# Objects (char, y, x, function)

## USER MAP - put in all of the objects you want to draw and their locations
def drawmap(window):
	
#You need to put all of the variables you want in the game into this list
varList = ['mapObjList', 'gameWindowXSize', 'gameWindowYSize',  'playerY', 'playerX', ] 

#Probably dont mess with this either
varDict = dict([i, eval(i)] for i in varList)
drawmapvar = drawmap

#You probably shouldnt touch this either
if __name__ == '__main__':
	print('Dumping game variables to gamefile...')
	pickle.dump(varDict, open('gamefile', 'wb'))
	print('Dumping functions to functionfile...')
	pickle.dump(drawmapvar, open('functionfile', 'wb'))
