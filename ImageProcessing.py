import sys,os,re
from PIL import Image as IM

class WriteToImage():
    def __init__(self,data):
        self.xaxis = 29 # pixels/volt
        self.yaxis = 116 # pixels/volt

class DetermineImage():
    def __init__(self,image):
        self.loc = None
        self.zero = []
        self.photo=image
        self.im = IM.open(self.photo)
        self.pix = self.im.load()
        self.find_edge()

    def find_edge(self):
        dim = self.im.size
        height = dim[0]
        width = dim[1]
        # Find vertical edge
        for x in range(0,width):
            for y in range(0,height):
                color = self.pix[y,x]
                self.loc = (y,x)
                if color is not 0:
                    check = self.confirm(axis='y')
                    if check:
                        self.zero[0] = [y,x]

    def confirm(self,axis):
        if axis == 'y':
            for z in range(self.loc[0],self.loc[0]+100):
                color = self.pix[z,x]
                if color == 0:
                    isaxis = False
                    break
            isaxis = True
        else:
            for z in range(self.loc[1],self.loc[1]+100):
                color = self.pix[y,z]
                if color == 0:
                    isaxis = False
                    break
            isaxis = True
        return isaxis



