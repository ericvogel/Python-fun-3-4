from tkinter import *
import WorldData
import BoxObject
import StaticBox
import LineObject
import PointObject


line1 = LineObject.LineObject(100, 100, 200, 400)
line2 = LineObject.LineObject(200, 400, 500, 600)
line3 = LineObject.LineObject(500, 600, 800, 300)
line4 = LineObject.LineObject(100, 100, 300, 600)
line5 = LineObject.LineObject(200, 600, 500, 600)
line6 = LineObject.LineObject(10, 10, 30, 30)
point1 = PointObject.PointObject(100, 100)
complete = 0.0

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
    WorldData.addToLineList(point1)

def updateWorld():
    global complete
    complete += 0.002
    if (complete > 1):
        complete = 0
    line4.setP1((line1.getP1()[0]+(complete * (line2.getP1()[0]-line1.getP1()[0])),line1.getP1()[1]+ (complete * (line2.getP1()[1]-line1.getP1()[1]))))
    line4.setP2((line1.getP2()[0]+(complete * (line2.getP2()[0]-line1.getP2()[0])),line1.getP2()[1]+ (complete * (line2.getP2()[1]-line1.getP2()[1]))))
    line5.setP1((line2.getP1()[0]+(complete * (line3.getP1()[0]-line2.getP1()[0])),line2.getP1()[1]+ (complete * (line3.getP1()[1]-line2.getP1()[1]))))
    line5.setP2((line2.getP2()[0]+(complete * (line3.getP2()[0]-line2.getP2()[0])),line2.getP2()[1]+ (complete * (line3.getP2()[1]-line2.getP2()[1]))))
    line6.setP2((line4.getP1()[0]+(complete * (line5.getP1()[0]-line4.getP1()[0])),line4.getP1()[1]+ (complete * (line5.getP1()[1]-line4.getP1()[1]))))
    line6.setP1((line4.getP2()[0]+(complete * (line5.getP2()[0]-line4.getP2()[0])),line4.getP2()[1]+ (complete * (line5.getP2()[1]-line4.getP2()[1]))))
    point1.setPos(line6.getP2()[0]+(complete * (line6.getP1()[0]-line6.getP2()[0])),line6.getP2()[1]+ (complete * (line6.getP1()[1]-line6.getP2()[1])))

pass
