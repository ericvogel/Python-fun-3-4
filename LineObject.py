import WorldData


def __init__():
    pass

class LineObject():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def getP1(self):
        return(self.x1, self.y1)
    
    def setP1(self, newP1):
        (self.x1, self.y1) = (newP1[0], newP1[1])
    
    def getP2(self):
        return(self.x2, self.y2)
    
    def setP2(self, newP2):
        (self.x2, self.y2) = (newP2[0], newP2[1])

    def update(self):
        pass
    
    
    
