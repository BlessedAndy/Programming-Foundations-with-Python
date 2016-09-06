'''
Created on Sep 5, 2016

@author: Andy Zhang
'''
def read_text():
    quotes = open(r"C:\Users\I310003\Documents\SAP\Learn\Python\Udacity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()