'''
Created on Aug 11, 2016

@author: Andy Zhang
'''
import os


def rename_files():
    #1. get file names from a folder
    file_list = os.listdir(r"C:\Users\I310003\Documents\SAP\Learn\Python\Udacity\scripts\prank\prank")
    dir = os.getcwd()
    print(dir)
    print(file_list)        
    
    #2. for each file, rename filename
    os.chdir(r"C:\Users\I310003\Documents\SAP\Learn\Python\Udacity\scripts\prank\prank")
    for file_name in file_list:
        print('The Original file name : '+file_name)
        print('The New file name : '+file_name.translate(str.maketrans('','','0123456789')))
        os.rename(file_name,file_name.translate(str.maketrans('','','0123456789')))

rename_files()