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
WIDTH, HEIGHT = 640, 480


class FDG():

    def __init__(self):
        self.artistNodes = []

    def getNodeX(self, i):
        return (i * 5) % width

    def getNodeY(self, i, total):
        totalPerc = total - ((total*5) % width)
        perc = i - ((i*5) % width)
        return (i * 20) % height

    def setArtists(self, artists):
        self.artistNodes = []
        for i in range(len(artists)):
                self.artistNodes.append(ArtistNode(artists[i], self.getNodeX(i), self.getNodeY(i, len(artists))))

    def drawNodes(self):
        for an in self.artistNodes:
            an.drawNode()

