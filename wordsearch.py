#  
#  
#  

__author__ = "blalyasar"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "blalyasar@gmail.com"
__status__ = ""


# bash e ekleme  
# alias wordsearch='python  path/dosyaismi.py'


import os
from argparse import ArgumentParser


p = ArgumentParser(description=' *filetype search word ')
p.add_argument('--f',
                #"filetype",
                required=True,
                help='file type -> tr:dosya uzantısı' ,
                type=str)

p.add_argument('--w',
                #"--word",
                required=True,
                help='search word-> tr: aranılacak kelime' ,
                type=str)
p.print_help() # helpi cagırmak :)
args = p.parse_args()

#  
# 
# 

CURRENT_DIR = os.getcwd()
print( CURRENT_DIR  )

CURRENT_DIR_FILE =  os.listdir( CURRENT_DIR )
#print(CURRENT_DIR_FILE)
CURRENT_DIR_FILE  = [img for img in CURRENT_DIR_FILE if img.endswith(f"{args.f}")]
#print(CURRENT_DIR_FILE)


for iread in CURRENT_DIR_FILE:
    with open( iread , "r", encoding="utf-8") as fileread:
        lines = fileread.readlines() # liste doner
        
        for index in range(len(lines)): # tum metnın ıcınde gez
            word = lines[index]
            #print(word)
            for word2 in word.split(): #
                #print(word2)
            
                # kucuk harfe cevirme olayı
                if word2.lower() == args.w.lower() :
                        print("Kelime su dosyada bulundu --->",iread)
                        print("Kelime su satırda bulundu --->",index)
                        print(word)

                for point in word2.split("."):
                    # kucuk harfe cevirme olayı
                    if point.lower() == args.w.lower() :
                        print("Kelime su dosyada bulundu --->",iread)
                        print("Kelime su satırda bulundu --->",index)
                        print(word.strip()) # tab olayına karşı
                        print("")
