'''
Created on Sep 29, 2016

@author: Andy Zhang
'''

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A boy and his toy come into life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "http://www.iqiyi.com/w_19rrxtosn9.html")

toy_story.show_trailer()
print(toy_story.storyline)

movies = [toy_story, ]