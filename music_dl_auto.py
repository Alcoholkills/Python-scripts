from tkinter import *
from tkinter import filedialog
from os import system, getcwd
from convert_to_mp3 import cleanMusicFolder

root = Tk()
root.geometry("500x200")
root.title("YouTube Download")

textArea = Entry(root, width=50)
textArea.pack()

def wrapper():
    beginADownLoad(textArea.get())

def beginADownLoad(url):
    try:
        system(("pytube " + url + ' -a -t "C:\\Users\\pierr\\Music\\Music_DL"').replace("\n",""))
        textArea.delete(0,last=END)
    except FileNotFoundError:
        pass

def selectAFile():
    root.filename = filedialog.askopenfilename(initialdir=getcwd(),title="Select a file", filetypes=(("txt files","*.txt"),))
    with open(root.filename, 'r') as f:
        lines = f.readlines()
        linesMax = len(lines)
        i = 1
        for x in lines:
            beginADownLoad(x)
            print(str(i) + "/" + str(linesMax))
            i += 1

beginDL = Button(root, text="Validate", command=wrapper)
searchTxtFile = Button(root, text="Select a file", command=selectAFile)
cleanMusic = Button(root, text="ffmpeg convert", command=cleanMusicFolder)

beginDL.pack()
searchTxtFile.pack()
cleanMusic.pack()

mainloop()