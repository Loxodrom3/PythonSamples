import os

path = ("E:/E_Documents/E_Pix4D/Percy_LD_Images/BU")

for fname in os.listdir(path):
    print(fname)
    srcFile = os.path.join(path, fname)
    # newName = fname[-7:]
    newName = fname[:8]+".png"
    dstFile = os.path.join(path, newName)
 #   print (srcFile, newName, dstFile, sep=" ")
    os.rename(srcFile, dstFile)
