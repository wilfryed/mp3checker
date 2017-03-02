#!C:\Python27\python.exe
# -*-coding:utf-8 -*

import os, sys, re, mutagen
from mutagen.mp3 import MP3

for root, directories, filenames in os.walk(u"E:\Musique"): 
    for filename in filenames: 
        extensions = os.path.splitext(filename)
        for extension in extensions:
            # on check si le fichier est un mp3
            if extension == ".mp3":  
                try:
                    f = MP3(os.path.join(root,filename) )
                    bitrate = f.info.bitrate / 1000
                    # on check si le bitrate est en dessous 96kbps
                    if bitrate <= 96:
                        file = open("report.txt","a")
                        file.write(os.path.join(root,filename).encode('utf8', 'ignore') + "\r")
                        file.write(str(bitrate) + "kbps" + "\r" + "\r")
                        file.close()  
                except mutagen.mp3.HeaderNotFoundError:
                    # le fichier est soit corrompu soit un fichier créé par OSX pour itunes
                    file = open("report.txt","a")
                    file.write("MP3 Header Error on file: " + os.path.join(root,filename).encode('utf8', 'ignore') + "\r \r")
                    file.close()
                    
print "Done!"             