'''
Created on Aug 9, 2017

@author: I310003
'''

import io
BLOCKSIZE = 1048576 # or some other, desired size in bytes
# with io.open('201501.DAT', 'r', encoding='ansi') as sourceFile:
#     with io.open("201501.txt", 'w', encoding='utf8') as targetFile:
#         while True:
#             contents = sourceFile.read(BLOCKSIZE)
#             if not contents:
#                 break
#             targetFile.write(contents)
            
with io.open('MV_ORGANISATIONALUNITS.txt', 'r', encoding='utf8') as sourceFile:
    with io.open("201501.txt", 'w', encoding='ansi') as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)
