from os import listdir, system, chdir, remove

def cleanMusicFolder():
    path = "C:\\Users\\pierr\\Music\\Music_DL"
    myLength = len(listdir(path))
    i = 1
    chdir(path)
    for file in listdir(path):
        if file[-3:] == "mp4":
            system("ffmpeg -i \"" + file + "\" \"" + file[:-4] +".mp3\"")
            remove(file)
        print(str(i) + "/" + str(myLength))
        i += 1
    
        