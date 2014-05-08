Meta Antics
===========

Meta Antics is a Python program for experimenting with music metadata.
At the moment it is very much still a work in progress.

So far it is only capable of logging in to your Google Play music
library and creating a music meta-database from this, however in the
future it would be nice to support libraries and playlists from all
other major music sources such as iTunes, last.fm, spotify, pandora,
grooveshark, etc (feel free to contribute).

The project started as an excuse to learn both Python and Vim, however
I expect it to remain one of my main sideprojects for quite a while.


Aims
----

- (current WIP) Create a 'related artist' Force Directed Map (from Google
Music data)
- Listening behaviour visualisations.
- Better music synchronisation between all supported libraries (i.e. only
uploading what is necessary to Google Music by performing better checks
than what Google Music seems to be capable of...)
- Compare music libraries with friends by visualising the differences in
your library contents with a focus on considering high amounts of plays
and related artists.
- Automatic notification for releases of new music by artists in your
library with a relatively high number of plays. Will have to watch major
music distro's for this.
- Super smart (and configurable) auto-playlist (and radio) generation.
This should also consider 'likes' and 'favourites' on social media and
other music sites.


Dependencies
------------

- The [Unofficial Google Music API by Simon Webber] (https://github.com/simon-weber/Unofficial-Google-Music-API)
- [pyprocessing] (https://code.google.com/p/pyprocessing/)
- [Python Box2D] (https://pypi.python.org/pypi/Box2D/2.3b0)


Note
----

This is a messy-WIP-side-project born of my disappointment in available
music management services and a chance to implement a bunch of ideas
that have been floating around between my friends and I for a while. I'm
definitely open to ideas and contributions, so feel free to add feature
requests to the issues section or even help out yourself!
