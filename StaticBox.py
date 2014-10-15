import WorldData
import GameObject


class StaticBox(GameObject.GameObject):

        def __init__(self):
                self.movingSpeed = 10
                super().__init__()

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
                ##DON'T self.move()
