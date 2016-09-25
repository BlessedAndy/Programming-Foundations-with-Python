'''
Created on Sep 5, 2016

@author: Andy Zhang
'''
import sys
import urllib.request

print(sys.version)

def read_text():
    quotes = open(r"C:\Users\I310003\Documents\SAP\Learn\Python\Udacity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()
    
def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    #urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
#     print(Output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no course words!")
    else:
        print("Could not scan the document properly.")
    
read_text()