#====World Vars============================================
gameName = 'Test Game'
debugging = True
worldWidth = 800
worldHeight = 600
isUpPressed = False
isDownPressed = False
isRightPressed = False
isLeftPressed = False

ObjectList = []

def __init__():
	pass


def getWorldWidth():
	return worldWidth

def getWorldHeight():
	return worldHeight

def getObjectList():
	return ObjectList

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
