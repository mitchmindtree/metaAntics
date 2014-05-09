#!usr/bin/env python2


'''

A tool for visualising Meta Antics' data as a "Force Directed
Graph" using Box2D.

'''


import Box2D
from ArtistNode import ArtistNode


# Constants
PPM = 20.0
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
WIDTH, HEIGHT = 1280, 720


class FDG():

    def __init__(self):
        self.artistNodes = []

    def getNodeX(self, i):
        return (i * 17) % width

    def getNodeY(self, i, total):
        totalPerc = total - ((total*5) % width)
        perc = i - ((i*5) % width)
        return (i * 17) % height

    def setArtists(self, artists):
        self.artists = []
        self.artistNodes = []
        for a in artists:
            if a.get('related_artists'):
                self.artists.append(a)
        for i in range(len(self.artists)):
            self.artistNodes.append(ArtistNode(self.artists[i], self.getNodeX(i), self.getNodeY(i, len(self.artists))))

    def setRelatedArtists(self):
        for an in self.artistNodes:
            an.setRelatedArtists(self.artistNodes)

    def drawNodes(self):
        for an in self.artistNodes:
            an.drawNode()

