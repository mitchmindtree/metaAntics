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
        self.relatives = []
        print("Screen =", width, height)
        print("Pos =", self.pos.x, self.pos.y)

    def setRelatedArtists(self, artistNodes):
        '''Find all related artist nodes'''
        self.relatives = []
        for artist in artistNodes:
            if artist.data.get('related_artists'):
                for rel in artist.data.get('related_artists'):
                    if self.data.get('name') == rel.get('name'):
                        self.relatives.append(artist)

    def drawLinesToRelatives(self):
        for rel in self.relatives:
            line(self.pos.x, self.pos.y, rel.pos.x, rel.pos.y)
            text(rel.data.get('name'), rel.pos.x, rel.pos.y)

    def drawNode(self):
        '''Draw function for artist node. Should be called in pyprocessing's 'draw'.'''
        if self.data:
            if (abs(mouse.x - self.pos.x)+abs(mouse.y - self.pos.y) < 20):
                if self.relatives:
                    self.drawLinesToRelatives()
                ellipse(self.pos.x, self.pos.y, 15, 15)
                text(self.data.get("name"), self.pos.x, self.pos.y)
            else:
                ellipse(self.pos.x, self.pos.y, 5, 5)
            
        #print("Screen =", width, height)
        #print("Pos =", self.pos.x, self.pos.y)
    
