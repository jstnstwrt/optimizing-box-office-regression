

class Movie(object):
	""" This class contains the movie objects and all the relevant attributes 
		being scraped from box office mojo"""

	def __init__(self, name, url= None):
        """Return a Movie object whose name is *name* and can be found
        at the box office mojo url given."""
        self.name = name
        self.url = url