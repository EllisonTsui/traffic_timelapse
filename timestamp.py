from PIL import Image, ImageDraw, ImageFont
import _imagingft # to load TrueTypeFont
import time
import os
# ---------------------------------------------------------------------------- #
def TimeStampImages(imgdir = "./screenshots/", savedir = "./timestamped/", fontFile = "./FreeSans.ttf"):
    """Creates a timestamped version of the images in the screenshots subfoler"""
    # *** parameters -- Modify according to your needs! ***
    fontSize = 30
    Width = 300
    Height = 50
    TextLeftPlacement = 20
    TextHeightPlacement = 12

    # *** real work ***
    fileList = os.listdir(imgdir)
    for fileName in fileList:
        if fileName.endswith(".png"):
            fileName2 = fileName.split('.')
            fileInfo = os.stat(imgdir + fileName)
            timeInfo = time.strftime(" %d.%m.%Y | %H:%M", time.localtime(fileInfo.st_mtime))
            print(fileName + ": " + timeInfo)

            im = Image.open(imgdir + fileName)
            myfont = ImageFont.truetype(fontFile, fontSize)
            draw = ImageDraw.Draw(im)
            draw.rectangle([TextLeftPlacement, TextHeightPlacement, Width, Height], fill="white")
            draw.text([TextLeftPlacement, TextHeightPlacement], timeInfo, fill="black", font=myfont)
            del draw

            #write image
            im.save(savedir + fileName2[0] + ".png", 'PNG')
    print("Done.")
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    TimeStampImages()
