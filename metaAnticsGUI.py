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


artistMeta = ArtistMeta()
stationMeta = StationMeta()
artists = []


def setup():
    size(WIDTH, HEIGHT)
    t = Thread(target=authGM())
    t.start()


def draw():
    background(250, 0, 0)
    text("A test string!", 200, 200)
    ellipse(mouse.x, mouse.y, 10, 10)
    #if artists:
        #fdg.draw()


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
 

#def mouseClicked(): 


#def mouseDragged():


#def mouseMoved():


#def mousePressed():


if __name__ == "__main__":
    run() 

