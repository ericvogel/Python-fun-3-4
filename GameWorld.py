from tkinter import *
import WorldData
import BoxObject
import StaticBox

def __init__():
    pass

def loadObjects():
    box1 = BoxObject.BoxObject()
    box1_Image = PhotoImage(file = 'Bin/Images/img.gif')
    WorldData.addToObjectList(box1, 100, 100, box1_Image)

    box2 = StaticBox.StaticBox()
    box2_Image = PhotoImage(file = 'Bin/Images/img2.gif')
    WorldData.addToObjectList(box2, 400, 300, box2_Image)
