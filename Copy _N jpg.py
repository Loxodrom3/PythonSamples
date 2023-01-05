# copy files that end with _N.jpg to a destination directory
import os
import shutil

sPath = ("Z:/Temp/Jon/03_Final_Pictures") # start Path.  Note: must use '/' for directory delination
dPath = ("Z:/Temp/Jon/North")             # destination Path     

# ld = os.listdir(path)
# print (ld)

for fName in os.listdir(sPath):
    if fName.endswith("_N.jpg"): # str opperator to select North jpegs.
        srcFile = os.path.join(sPath, fName)
        dstFile = os.path.join(dPath, fName)
        print(fName)
        shutil.copyfile(srcFile, dstFile)
