#!usr/bin/env python2


'''

Artist node to be used with Box2D to generate Force Directed Graph

'''


from pyprocessing import *
from Box2D import *
import Box2D


def getArtistNodeBodyDef(x, y):
    bd = b2BodyDef()
    


class ArtistNode(b2Body):

    def __init__(self, artistData=None, x=None, y=None):
        self.data = artistData if artistData is not None else []
        self.pos = b2Vec2(x if x is not None else width/2, y if y is not None else height/2)
        print("Screen =", width, height)
        print("Pos =", self.pos.x, self.pos.y)

    def drawNode(self):
        '''Draw function for artist node. Should be called in pyprocessing's 'draw'.'''
        if self.data:
            ellipse(self.pos.x, self.pos.y, 5, 5)
            if (abs(mouse.x - self.pos.x)+abs(mouse.y - self.pos.y) < 10):
                text(self.data.get("name"), self.pos.x, self.pos.y)
        #print("Screen =", width, height)
        #print("Pos =", self.pos.x, self.pos.y)
    
