from PIL import Image, ImageDraw, ImageFont
import _imagingft # to load TrueTypeFont
import time
import os
# ---------------------------------------------------------------------------- #
def TimeStampImages():
    """Creates a timestamped version of the images in the screenshots subfoler"""
    # *** parameters -- Modify according to your needs! ***
    mydir = "./screenshots/"
    savedir = "./timestamped/"
    fontFile = "./FreeSans.ttf"
    fontSize = 20
    topLeftWidthDivider = 8.5 # increase to make the textbox shorter in width
    topLeftHeightDivider = 23 # increase to make the textbox shorter in height
    textPadding = 2 #

    # *** real work ***
    fileList = os.listdir(mydir)
    for fileName in fileList:
        if fileName.endswith(".png"):
            fileName2 = fileName.split('.')
            fileInfo = os.stat(mydir + fileName)
            timeInfo = time.strftime("%d.%m.%Y %H:%M", time.localtime(fileInfo.st_mtime))
            print(fileName + ": " + timeInfo)

            im = Image.open(mydir + fileName)
            myfont = ImageFont.truetype(fontFile, fontSize)
            topLeftWidth = int(im.size[0] - (im.size[0] / topLeftWidthDivider))
            topLeftHeight = int(im.size[1] - (im.size[1] / topLeftHeightDivider))
            draw = ImageDraw.Draw(im)
            draw.rectangle([topLeftWidth, topLeftHeight, im.size[0], im.size[1]], fill="black")
            draw.text([topLeftWidth + textPadding, topLeftHeight + textPadding], timeInfo, fill="white", font=myfont)
            del draw

            #write image
            im.save(savedir + fileName2[0] + ".png", 'PNG')
    print("Done.")
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    TimeStampImages()
