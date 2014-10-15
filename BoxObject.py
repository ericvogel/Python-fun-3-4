import WorldData
import GameObject


class BoxObject(GameObject.GameObject):

    def __init__(self):
        self.movingSpeed = 5
        pass

    def move(self):
        if (WorldData.isDownPressed == True):
                self.setPos(self.getX(), self.getY()+self.movingSpeed)
                while(self.getCollision()[0]):
                        self.setPos(self.getX(), self.getY()-1)
        elif (WorldData.isUpPressed == True):
                self.setPos(self.getX(), self.getY()-self.movingSpeed)
                while(self.getCollision()[0]):
                        self.setPos(self.getX(), self.getY()+1)

        if (WorldData.isRightPressed == True):
                self.setPos(self.getX()+self.movingSpeed, self.getY())
                while(self.getCollision()[0]):
                        self.setPos(self.getX()-1, self.getY())
        elif (WorldData.isLeftPressed == True):
                self.setPos(self.getX()-self.movingSpeed, self.getY())
                while(self.getCollision()[0]):
                        self.setPos(self.getX()+1, self.getY())

    def update(self):
        self.move()
