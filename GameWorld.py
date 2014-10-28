from tkinter import *
import WorldData
import BoxObject
import StaticBox
import LineObject
import PointObject
import math

point1 = PointObject.PointObject(100, 100)
point2 = PointObject.PointObject(200, 200)
point3 = PointObject.PointObject(300, 200)
point4 = PointObject.PointObject(400, 100)

line1 = LineObject.LineObject(point1.getX(), point1.getY(), point2.getX(), point2.getY())
line2 = LineObject.LineObject(point2.getX(), point2.getY(), point3.getX(), point3.getY())
line3 = LineObject.LineObject(point3.getX(), point3.getY(), point4.getX(), point4.getY())
line4 = LineObject.LineObject(100, 100, 300, 600)
line5 = LineObject.LineObject(200, 600, 500, 600)
line6 = LineObject.LineObject(10, 10, 30, 30)
pointDraw = PointObject.PointObject(100, 100)
complete = 0.0
dragging = -1

def __init__():
    pass

def loadObjects():
##    box1 = BoxObject.BoxObject()
##    box1_Image = PhotoImage(file = 'Bin/Images/img.gif')
##    WorldData.addToObjectList(box1, 100, 100, box1_Image)
##
##    box2 = StaticBox.StaticBox()
##    box2_Image = PhotoImage(file = 'Bin/Images/img2.gif')
##    WorldData.addToObjectList(box2, 400, 300, box2_Image)
    
    WorldData.addToLineList(line1)
    WorldData.addToLineList(line2)
    WorldData.addToLineList(line3)
    WorldData.addToLineList(line4)
    WorldData.addToLineList(line5)
    WorldData.addToLineList(line6)
    WorldData.addToLineList(pointDraw)

def updateWorld():
    global complete
    global dragging

    #print(WorldData.getMouseX())

    if ((WorldData.getMousePressed() == True) and( math.sqrt((WorldData.getMouseX() - point1.getX())**2 + (WorldData.getMouseY() - point1.getY())**2) <= 5 )):
        dragging = 1
        complete = 0
    if ((WorldData.getMousePressed() == True) and( math.sqrt((WorldData.getMouseX() - point2.getX())**2 + (WorldData.getMouseY() - point2.getY())**2) <= 5 )):
        dragging = 2
        complete = 0
    if ((WorldData.getMousePressed() == True) and( math.sqrt((WorldData.getMouseX() - point3.getX())**2 + (WorldData.getMouseY() - point3.getY())**2) <= 5 )):
        dragging = 3
        complete = 0
    if ((WorldData.getMousePressed() == True) and( math.sqrt((WorldData.getMouseX() - point4.getX())**2 + (WorldData.getMouseY() - point4.getY())**2) <= 5 )):
        dragging = 4
        complete = 0

    if(dragging == 1):
        point1.setPos(WorldData.getMouseX(), WorldData.getMouseY())
    elif(dragging == 2):
        point2.setPos(WorldData.getMouseX(), WorldData.getMouseY())
    elif(dragging == 3):
        point3.setPos(WorldData.getMouseX(), WorldData.getMouseY())
    elif(dragging == 4):
        point4.setPos(WorldData.getMouseX(), WorldData.getMouseY())
    elif(dragging == -1):
        pass

    line1.setP1((point1.getX(), point1.getY()))
    line1.setP2((point2.getX(), point2.getY()))
    line2.setP1((point2.getX(), point2.getY()))
    line2.setP2((point3.getX(), point3.getY()))
    line3.setP1((point3.getX(), point3.getY()))
    line3.setP2((point4.getX(), point4.getY()))
    
        
        
    if (WorldData.getMousePressed() == False):
        dragging = -1
        complete += 0.005
    if (complete > 1):
        complete = 0
        
    line4.setP1((line1.getP1()[0]+(complete * (line2.getP1()[0]-line1.getP1()[0])),line1.getP1()[1]+ (complete * (line2.getP1()[1]-line1.getP1()[1]))))
    line4.setP2((line1.getP2()[0]+(complete * (line2.getP2()[0]-line1.getP2()[0])),line1.getP2()[1]+ (complete * (line2.getP2()[1]-line1.getP2()[1]))))
    line5.setP1((line2.getP1()[0]+(complete * (line3.getP1()[0]-line2.getP1()[0])),line2.getP1()[1]+ (complete * (line3.getP1()[1]-line2.getP1()[1]))))
    line5.setP2((line2.getP2()[0]+(complete * (line3.getP2()[0]-line2.getP2()[0])),line2.getP2()[1]+ (complete * (line3.getP2()[1]-line2.getP2()[1]))))
    line6.setP2((line4.getP1()[0]+(complete * (line5.getP1()[0]-line4.getP1()[0])),line4.getP1()[1]+ (complete * (line5.getP1()[1]-line4.getP1()[1]))))
    line6.setP1((line4.getP2()[0]+(complete * (line5.getP2()[0]-line4.getP2()[0])),line4.getP2()[1]+ (complete * (line5.getP2()[1]-line4.getP2()[1]))))
    pointDraw.setPos(line6.getP2()[0]+(complete * (line6.getP1()[0]-line6.getP2()[0])),line6.getP2()[1]+ (complete * (line6.getP1()[1]-line6.getP2()[1])))

pass
