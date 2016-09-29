'''
Created on Sep 29, 2016

@author: Andy Zhang
'''

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer