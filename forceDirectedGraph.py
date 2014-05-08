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


