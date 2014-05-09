#!usr/bin/env python2


'''
A module for managing Google Music Metadata. getGoogleMusicMeta returns
a dictionary with requested data (args.gmStations = Stations Data,
arts.gmArtists = Artists Data).
'''


import sys, json, os
from getpass import getpass
from pprint import pprint
from gmusicapi import Mobileclient
from operator import attrgetter, itemgetter
from threading import Thread


mobile = Mobileclient()


def gmMetaFP(which):
    '''Returns filepath for "which"'s meta data .json file'''
    return os.getcwd()+"/"+which+"MetaData.json"


def authGM(): 
    '''Authorises the instance of Google Music mobile client'''
    while True:
        user = raw_input("Enter your Google Music e-mail: ")
        pw = getpass() 
        if mobile.login(user, pw):
            print("Logged in successfully.")
            break
        elif count < 3:
            print("Login failed, try again fool!")
            count = count+1
        else:
            raise Exception("Failed to log in, you absolute nugget! Gonna have to quit now...")
            sys.exit(0)
   

def matchIgnoringCase(a, b):
    '''Utility function to check for string match ignoring case. Is mainly used
    for checking artist names.'''
    try:
        return a.upper() == b.upper()
    except AttributeError:
        return a == b



class GMMeta(Thread):
    '''The base class for retrieving, updating and loading Google Music metadata.'''
    
    def __init__(self):
        Thread.__init__(self)
        self.stop = False
 
    def setStop(self):
        self.stop = True
    
    def updateWhichGMJSON(self, which, data):
        print('Creating / Overwriting', gmMetaFP(which))
        f = open(gmMetaFP(which), 'w')
        json.dump(data, f, sort_keys=True)
        f.close()
        print("Finished wrting to", gmMetaFP(which))

    def loadJSONData(self, which):
        '''Loads Google Music  metadata for "which" frhm JSON'''
        print('Loading Stations from json.')
        f = open(gmMetaFP(which), 'r')
        data = json.load(f)
        f.close()
        return data



class ArtistMeta(GMMeta):
    '''Class for retrieving, updating and loading Google Music Artist metadata.'''

    def extendInfoInAlbums(self, artists, mobile):
        '''Extends information in "albums" key of artist using mobile.'''
        print("Extending Info for Albums in each Artist...")
        for artist in artists:
            print(artist.get('name'))
            try:
                for album in artist.get('albums'):
                    if self.stop:
                        return
                    print("\tRetrieving", album.get('name'))
                    try:
                        album = mobile.get_album_info(album.get('albumId'))
                    except KeyError:
                        print("Failed to extend album data due to KeyError in 'album'.")
            except TypeError:
                print("Failed to extend album data due to TypeError in 'artist'.")

    def addArtistInfo(self, artists, checked, song, mobile):
        '''Takes artist info from song and appends it to "artists".
        Also adds the associated "artistId" to the "checked" list.'''
        print('Retrieving', song.get('artist'))
        try:
            info = mobile.get_artist_info(song.get('artistId')[0], True, 5, 100)
            artists.append(info)
            checked.append(song.get('artistId')[0])
        except KeyboardInterrupt or SystemExit or GeneratorExit or EnvironmentError:
            print('Exiting Program...')
            sys.exit(0)
        except:
            print('Failed to retrieve...')

    def getArtists(self, songs, mobile):
        '''Returns a list of artist dictionaries from list of song dictionaries.'''
        new = sorted(songs, key=itemgetter('artist', 'album'))
        artists = []
        checked = []
        for i in range(len(new)):
            if self.stop:
                return []
            if new[i].get('artistId'):
                if not artists or (not matchIgnoringCase(new[i].get('artist'), artists[-1].get('name')) and
                                   not new[i].get('artistId')[0] in checked):
                    self.addArtistInfo(artists, checked, new[i], mobile)
        self.extendInfoInAlbums(artists, mobile)
        if self.stop:
            return []
        return artists

    def updateGMJSON(self):
        '''Fetch latest Google Music Data and update "artists" JSON file'''
        print("Updating 'artists' meta.")
        print("Retrieving songs from Google...")
        songs = mobile.get_all_songs()
        artists = self.getArtists(songs, mobile)
        if not self.stop:
            self.updateWhichGMJSON('artists', artists)
        if self.stop:
            print("Google Music MetaData update was cancelled.")
    
    def run(self):
        self.stop = False
        self.updateGMJSON()
    
    def loadData(self):
        return self.loadJSONData('artists')



class StationMeta(GMMeta):
    '''Class for retrieving, updating and loading Google Music Station metadata.'''
    
    def updateGMJSON(self):
        '''Fetch latest Google Music Data and update "stations" JSON file'''
        print("Updating 'stations' meta.")
        print("Retrieving stations from Google...")
        stations = mobile.get_all_stations()
        self.updateWhichGMJSON('stations', stations)
    
    def run(self):
        self.updateGMJSON()
    
    def loadData(self):
        return self.loadJSONData('stations')



