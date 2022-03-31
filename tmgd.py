import zipfile, os
Gamefolder = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash"
files = os.listdir()
start = 0
for ls in files:
    if ls == "Officialtexture.zip":
        start = 1
if start == 1:
    print("Texture manager gd \"v0.2beta\"")
    print("/help for reference.")
if start == 0:
    print("No Archive: OfficialTexture.zip")
    input("")
while start == 1:
    COM = input("tmgd> ")
    if COM == "/help":
        print("/return_Set Officialtexture gd.")
        print("/install_Set your texture.")
        print("/exit_Turn off the program.")
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