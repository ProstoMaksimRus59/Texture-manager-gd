#Shit code. :)
import zipfile, os
files = os.listdir()
start = 0
creat = 0
for ls in files:    #Check for the settings file.
    if ls == "settings.set":
        creat = 1
        set = open("settings.set", 'r')
        Gamefolder = set.read()
        set.close
if creat == 0:  #Creating a settings file.
    Way = input("Path to the game.\nFor example: C:\\yy\\xx\\Geometry Dash\n>")
    set = open("settings.set", 'w')
    set.write(Way)
    set.close()
    Gamefolder = Way
for ls in files:    #Check for archive.
    if ls == "Officialtexture.zip":
        start = 1
if start == 1:  #If there is an archive.
    print("Texture manager gd \"v0.3beta\"")
    print("/help for reference.")
if start == 0:  #If there is no archive.
    print("No Archive: OfficialTexture.zip")
    input("")
while start == 1:       #Command line.
    COM = input("tmgd> ")
    if COM == "/help":
        print("/return_Set Officialtexture gd.")
        print("/install_Set your texture.")
        print("/exit_Turn off the program.")
        print("/reset_Reset settings.")
    if COM == "/return":
        z = zipfile.ZipFile("Officialtexture.zip", 'r')
        z.extractall(Gamefolder)
        print("done.")
    if COM == "/install":
        TP = input("file> ")
        z = zipfile.ZipFile(TP, 'r')
        z.extractall(Gamefolder)
        print("done.")
    if COM == "/exit":
        exit()
    if COM == "/reset":
        os. remove("settings.set")
        input("Settings are dropped.\nThe program will be turned off.")
        exit()