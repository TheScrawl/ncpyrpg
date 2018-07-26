import dill as pickle


#Important game function stuff, you probably shouldnt edit this
mapObjList = []
mapEntityList = []

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

class mapEntity(object):
    def __init__(self, movepath, body, speed, posY, posX, contactFunctions):
        self.movepath = movepath
        self.body = body
        self.speed = speed
        self.posY = posY
        self.posX = posX
        self.contactFunctions = contactFunctions

    def spawn(self, window, loops):
            window.addstr(self.posY, self.posX, self.body)
            for l in range(loops):
                for i in self.movepath:
                    for x in range(i[1]):
                        window.addstr(self.posY, self.posX, ' ')
                        if i[0] == 'up':
                            self.posY = self.posY + 1
                            window.addstr(self.posY, self.posX, self.body)
                        if i[0] == 'down':
                            self.posY = self.posY - 1
                            window.addstr(self.posY, self.posX, self.body)
                        if i[0] == 'left':
                            self.posX = self.posX - 1
                            window.addstr(self.posY, self.posX, self.body)
                        if i[0] == 'right':
                            self.posX = self.posX + 1
                            window.addstr(self.posY, self.posX, self.body)
                        time.sleep(0.1)
                        window.refresh()
                    #menuOut('entity moved ' + str(i[0]), window





## GAME VARIABLES - Feel free to edit and add things here
playerY, playerX, = 4, 4 #Spawn Point
gameWindowXSize = 40
gameWindowYSize = 28

## GAME MAP ARRAYS AND OBJECTS
# Entities 

badguy = mapEntity(
        [('up', 3), ('left', 3), ('down', 3), ('right', 3)],
        '#',
        1,
        10,
        10,
        ['exit(0)']
        )


# Arrays - These are objects you can draw

maze = ['##########',
        '#        #', 
        '#        #', 
        '#        #', 
        '#        #', 
        '##########',]

# Objects (char, y, x, function)

button = mapObj(
	['x'],
	5, 
	5, 
	[
	'menuOut("button pressed", menuWindow)',
	'window.addch(7, 6, "F")', 
	'menuOut("Door opened", menuWindow)',
	])

button2 = mapObj(
	['x'],
	5, 
	6, 
	[
	'(threading.Thread(target=badguy.spawn, args=(window, 100))).start()',
	'menuOut("button2 pressed", menuWindow)'
	])

## USER MAP - put in all of the objects you want to draw and their locations
def drawmap(window):
	#drawArray(1, 1, window, maze)
	drawArray(button.posY, button.posX, window, button.char)
	drawArray(button2.posY, button2.posX, window, button2.char)
	
#You need to put all of the variables you want in the game into this list
varList = [
        #System vars
        'mapObjList', 
        'mapEntityList', 
        'gameWindowXSize', 
        'gameWindowYSize',  
        'playerY', 
        'playerX', 
        #Player vars
        'maze', 
        'button', 
        'button2', 
        'badguy']

#Probably dont mess with this either
varDict = dict([i, eval(i)] for i in varList)
drawmapvar = drawmap

#You probably shouldnt touch this either
if __name__ == '__main__':
	print('Dumping game variables to gamefile...')
	pickle.dump(varDict, open('gamefile', 'wb'))
	print('Dumping functions to functionfile...')
	pickle.dump(drawmapvar, open('functionfile', 'wb'))
