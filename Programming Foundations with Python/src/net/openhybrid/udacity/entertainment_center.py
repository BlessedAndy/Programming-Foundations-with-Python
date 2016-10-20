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

avator = media.Movie("Avator",
                        "A Marin on an alien planet",
                        "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%98%BF%E5%87%A1%E8%BE%BE&step_word=&hs=0&pn=6&spn=0&di=107945989580&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2552744632%2C398485560&os=2632718767%2C1078212019&simid=3158977015%2C3795444350&adpicid=0&ln=1969&fr=&fmq=1476872127698_R&fm=index&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.designft.cn%2Fmanage%2FeWebEditor%2FUploadFile%2F201031015461129.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B1jft2gup_z%26e3BvgAzdH3Fp6w1j_z%26e3Bwfr%3Ft1%3D89a&gsm=0&rpstart=0&rpnum=0",
                        "http://v.youku.com/v_show/id_XODMwMjI2NTQ4.html")

movies = [toy_story, avator]

fresh_tomatoes.open_movies_page(movies)