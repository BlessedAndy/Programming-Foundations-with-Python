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

#toy_story.show_trailer()
#print(toy_story.storyline)

rain_man = media.Movie("Rain Man",
                        "A Marin on an alien planet",
                        "https://en.wikipedia.org/wiki/Rain_Man#/media/File:Rain_Man_poster.jpg",
                        "http://v.youku.com/v_show/id_XODMwMjI2NTQ4.html")

kramer_vs_kramer = media.Movie("Kramer vs . Kramer",
                             "Story about American family",
                             "https://en.wikipedia.org/wiki/Kramer_vs._Kramer#/media/File:Oscar_posters_79.jpg",
                             "https://www.youtube.com/watch?v=jNLcfJ06y34"
                             )


movies = [toy_story, rain_man,kramer_vs_kramer]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.valid_ratings)

print (media.Movie.__doc__)

print (media.Movie.__name__)

print (media.Movie.__module__)