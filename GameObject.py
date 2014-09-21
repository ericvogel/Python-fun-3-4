import WorldData


def __init__():
	print('Loading GameObject class...Done')

class GameObject():
		
		
		def __init__(self):
			self.x = 0
			self.y = 0
			self.image = None

		def setPos(self, newX, newY):
			self.x = newX
			self.y = newY

		def getX(self):
			return (self.x)
		
		def getY(self):
			return (self.y)
		
		def getDraw(self):
			return self.image
		
		def setDraw(self, newImage):
			self.image = newImage
			#print self.image


		def move(self):
			if (WorldData.isDownPressed == True):
				self.setPos(self.getX(), self.getY()+self.movingSpeed)
			elif (WorldData.isUpPressed == True):
				self.setPos(self.getX(), self.getY()-self.movingSpeed)

			if (WorldData.isRightPressed == True):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
			elif (WorldData.isLeftPressed == True):
				self.setPos(self.getX()-self.movingSpeed, self.getY())

		def update(self):
			pass

		def getWidth(self):
			return self.image.width()

		def getHeight(self):
			return self.image.height()

		def getCollision(self, collidingClass = None):
			self.tempList = list(WorldData.ObjectList)
			
			self.tempList.remove(self)

			if (collidingClass != None):
				for item in self.tempList:
					if (item.__class__.__name__ != collidingClass):
						self.tempList.remove(item)
				pass

			self.boundingBoxes = []   # boundingBoxes are defined by a tuple of 4 ints, (left, upper, right, lower, object)
			for item in self.tempList:
				self.boundingBoxes.append( ((item.getX()-(item.getWidth()/2))-self.getWidth()/2, (item.getY()-(item.getHeight()/2))-self.getHeight()/2, (item.getX() + (item.getWidth()/2))+self.getWidth()/2, (item.getY()+(item.getHeight()/2))+self.getHeight()/2, item ))
			LEFTBOUND = 0
			UPPERBOUND = 1
			RIGHTBOUND = 2
			LOWERBOUND = 3
			ITEMOBJECT = 4
			for item in self.boundingBoxes:
				#===================================================================
				#print (self.ownBoundingBox[LOWERBOUND] , item[UPPERBOUND])
				if  (
						(self.getX()>item[LEFTBOUND])and
						(self.getY()>item[UPPERBOUND])and
						(self.getX()<item[RIGHTBOUND])and
						(self.getY()<item[LOWERBOUND])
					):
					return (True, item[4])
			#if=get=to=this=statment=there=are=no=collisions
			return (False, None)
