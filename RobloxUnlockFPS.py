import os
def placeFile(folder):
    folderContents = os.listdir(folder)
    for i in folderContents:
        try:
            if 'RobloxPlayerBeta.exe' in os.listdir(folder + "/" + i):
                gameFolder = i
                break
        except:
            pass
    if "ClientSettings" not in os.listdir(folder + "/" + gameFolder):
        print("Writing new file...")
        target = folder + "/" + gameFolder + "/ClientSettings"
        os.mkdir(target)
        f = open(target + "/" + "ClientAppSettings.json", "w")
        f.write("{\"DFIntTaskSchedulerTargetFps\": 240}")
        f.close()
placeFile(f"C:/Users/{os.environ.get('USERNAME')}/AppData/Local/Roblox/Versions")
placeFile("C:/Program Files (x86)/Roblox/Versions")