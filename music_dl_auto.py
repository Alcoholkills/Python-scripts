
#use subprocess to initiate cmd commands
#use pandas to import excel files
#check 'https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279' to make it automatically
#C:\Users\pierr\Documents\C'est le bureau\Youtube Downloader\George Orwell
#C:\Users\pierr\Music\iTunes\iTunes Media\Music\Unknown Artist\Unknown Album

#it's gg ;)


import pandas
#import subprocess
#import pytube
import os
import re

excelFilePath = "/home/pierre/Documents/Coding/PythonScript/nameAndAge.ods"
#excelArray = pandas.read_excel(excelFilePath, header=None, names=["Nom", "Ages", "Adultes ?"]).values
#returns a dataframe
excelArray = pandas.read_excel(excelFilePath).values
print(excelArray)

print("--")
for y in excelArray:
    if y[2] != "Oui":
        #print(y[0])
        Youtube(y[0]).streams.get_audio_only().download()
        #FAIT - Enlever le print et faire la creation de l'objet YouTube
        y[2] = "Oui"
        #Mettre ici le write-excel pour valider le doc
        
listFiles = os.listdir("/home/pierre/Documents/Coding/PythonScript/")
print(listFiles)
for x in listFiles:
    found = re.findall("[.].+",x)
    print(found)
    if found == ".mp4":
        #mettre la commande ffmpeg pour convertir en 'mp3' est l'envoyer ici : 'C:\Users\pierr\Music\iTunes\iTunes Media\Music\Unknown Artist\Unknown Album'
        #cmd = ...
        #Mettre la commande ffmpeg ici, pour rm le file mp4
        #cmd = ...