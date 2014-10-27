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
