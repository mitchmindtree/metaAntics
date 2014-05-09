#!usr/bin/env python2


'''

Meta Antics.

A python program for experimenting with large amounts of music metadata!

'''


import sys, os
from pprint import pprint
from pyprocessing import *
from threading import Thread
from GMMetaData import ArtistMeta, StationMeta, authGM
from forceDirectedGraph import *
from Box2D import *


artistMeta = ArtistMeta()
stationMeta = StationMeta()
artists = []
fdg = FDG()


def setup():
    '''Called once on startup by pyprocessing's setup.'''
    size(WIDTH, HEIGHT)
    frameRate(60)
    t = Thread(target=authGM())
    t.start()


def draw():
    '''Override of pyprocessing's draw. Called 'framerate' times a second'''
    background(12, 60, 50)
    ellipse(mouse.x, mouse.y, 10, 10)
    if fdg.artistNodes:
        fdg.drawNodes()


def keyPressed(): 
    if key.char == '0':
        print('Seeya Mayyyytte!')
        artistMeta.setStop()
        stationMeta.setStop()
        sys.exit(0)
    elif key.char == '1':
        stationMeta.start()
        artistMeta.start()
    elif key.char == '2':
        stationMeta.start()
    elif key.char == '3':
        artistMeta.start()
    elif key.char == '4':
        artists = artistMeta.loadData()
        pprint(artists)
        fdg.setArtists(artists)
        fdg.setRelatedArtists()
 

#def mouseClicked(): 


#def mouseDragged():


#def mouseMoved():


#def mousePressed():


if __name__ == "__main__":
    run() 

