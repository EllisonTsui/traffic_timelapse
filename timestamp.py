from PIL import Image, ImageDraw, ImageFont
import _imagingft # to load TrueTypeFont
import time, os
from color_analysis import TrafficColorAnalysis
import numpy as np
# ---------------------------------------------------------------------------- #
def TrafficColorAnalysis(im, tol = 10):
    """Using the determined colors for google maps traffic, output their respective values"""
    # Told Traffic Colors
    # green: (0,180,32)
    # orange: (255,159,0)
    # red: (255,0,0)
    # blood: (192,0,0)
    # traffic_colors = [(0,180,32), (255,159,0), (255,0,0), (192,0,0)]

    # Found Traffic Colors
    # green: (132,202,80)
    # orange: (240,125,2)
    # red: (230,0,0)
    # blood: (159,20,20)
    traffic_colors = [(132,202,80),(240,125,2),(230,0,0),(159,20,20)]

    num_colors = [0,0,0,0]

    colors = im.convert('RGB').getcolors(maxcolors = 256 * 256 * 256)

    for color in colors:
        rgb = color[1]
        for i in range(len(traffic_colors)):
            t_rgb = traffic_colors[i]
            within_limits = True
            for j in range(3):
                if rgb[j] < max(t_rgb[j] - tol, 0) or rgb[j] > min(t_rgb[j] + tol, 255):
                    within_limits = False
                    break
            if within_limits == True:
                num_colors[i] += color[0]
                break # tolerance must ensure that color bands being searched don't overlap

    return traffic_colors, num_colors
# ---------------------------------------------------------------------------- #
def TimeStampImages(imgdir = "./screenshots/", savedir = "./timestamped/", fontFile = "./FreeSans.ttf"):
    """Creates a timestamped version of the images in the screenshots subfoler"""
    # *** parameters -- Modify according to your needs! ***
    fontSize = 30
    Width = 300
    Height = 48
    TextLeftPlacement = 40
    TextHeightPlacement = 8
    traffic_height = 5
    traffic_sidepadding = 32

    traffic_bar_left = TextLeftPlacement - traffic_sidepadding
    traffic_bar_size = Width - TextLeftPlacement + 2 * traffic_sidepadding

    # Enumerate files ending in .png in the image directory
    fileList = os.listdir(imgdir)
    for fileName in fileList:
        if fileName.endswith(".png"):
            fileName2 = fileName.split('.')
            fileInfo = os.stat(imgdir + fileName)
            timeInfo = time.strftime(" %d.%m.%Y | %H:%M", time.localtime(fileInfo.st_mtime))
            print(fileName + ": " + timeInfo)
            # Open image
            im = Image.open(imgdir + fileName)
            # Compute the number of pixels of traffic
            colors, num_colors = TrafficColorAnalysis(im)
            total_traffic = sum(num_colors)
            # Add Time and Traffic to the Image
            myfont = ImageFont.truetype(fontFile, fontSize)
            draw = ImageDraw.Draw(im)
            # Traffic Bar
            if total_traffic != 0:
                traffic_percent = [float(x) / total_traffic for x in num_colors]
                traffic_cumsum = np.cumsum(traffic_percent)
                for i in range(len(num_colors),0,-1):
                    draw.rectangle([traffic_bar_left, Height + 1, traffic_bar_left + traffic_bar_size * traffic_cumsum[i-1], Height + traffic_height], fill=colors[i-1])
            # Time
            draw.rectangle([TextLeftPlacement-traffic_sidepadding , TextHeightPlacement, Width, Height], fill="white")
            draw.text([TextLeftPlacement, TextHeightPlacement], timeInfo, fill="black", font=myfont)
            # Percentage of Traffic?
            # traffic = (1 - traffic_percent[0])*100
            # traffic_string = "%.0f%%" %(traffic)
            # draw.rectangle([traffic_bar_left + traffic_bar_size + 5 , TextHeightPlacement, traffic_bar_left + traffic_bar_size + 40, Height], fill="white")
            # draw.text([traffic_bar_left + traffic_bar_size + 10, TextHeightPlacement], traffic_string, fill="black", font=myfont)
            del draw
            #write image
            im.save(savedir + fileName2[0] + ".png", 'PNG')
    print("Done.")
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    TimeStampImages()
