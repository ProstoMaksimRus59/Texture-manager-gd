import zipfile
print("Texture manager gd \"v0.1beta\"")
print("/help for reference.")
while 1 == 1:
    COM = input("tmgd> ")
    if COM == "/help":
        print("/return_Officialtexture gd.")
        print("/install_Set your texture.")
        print("/exit_Turn off the program.")
    if COM == "/return":
        z = zipfile.ZipFile("Officialtexture.zip", 'r')
        z.extractall("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash")
        print("done.")
    if COM == "/install":
        TP = input("file> ")
        z = zipfile.ZipFile(TP, 'r')
        z.extractall("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash")
        print("done.")
    if COM == "/exit":
        exit()