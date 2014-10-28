#====World Vars============================================
gameName = 'Test Game'
debugging = True
worldWidth = 1024
worldHeight = 768
isUpPressed = False
isDownPressed = False
isRightPressed = False
isLeftPressed = False
frameCounter = 0
mouseX = 1
mouseY = 1
mousePressed = False

ObjectList = []
LineList = []
PointList = []

def __init__():
	pass

def getFrameCounter():
	return frameCounter

def updateFrameCounter():
	global frameCounter
	frameCounter += 1

def getMouseX():
        global mouseX
        return mouseX

def getMouseY():
        global mouseY
        return mouseY

def setMousePos(nx, ny):
        global mouseX
        global mouseY
        mouseX = nx
        mouseY = ny
        
def setMousePressed(nstate):
        global mousePressed
        mousePressed = nstate

def getMousePressed():
        global mousePressed
        return mousePressed

def getWorldWidth():
	return worldWidth

def getWorldHeight():
	return worldHeight

def getObjectList():
	return ObjectList

def getLineList():
	return LineList

def addToObjectList(GameObjectToAdd, init_X, init_Y, init_Image):
	ObjectList.append(GameObjectToAdd)
	
	try:
		init_X = int(init_X)
		init_Y = int(init_Y)
	except Exception as e:
		print(e)
	else:
		GameObjectToAdd.setPos(init_X, init_Y)
		print("object added at " + str(init_X) + ", " + str(init_Y))

	GameObjectToAdd.setDraw(init_Image)
	
def addToLineList(LineObjectToAdd):
	ObjectList.append(LineObjectToAdd)
	
def addToLineList(PointObjectToAdd):
	ObjectList.append(PointObjectToAdd)
