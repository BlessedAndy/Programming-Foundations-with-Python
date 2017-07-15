'''
Created on Sep 29, 2016

@author: Andy Zhang
'''
import webbrowser


class Movie():
    
    """THIS IS FOR TESTING PYTHON DOC"""
    
    valid_ratings = ["G","PG","PG-13","R"]
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        webbrowser.open("http://music.163.com/#/outchain/2/409872465/")
