from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time, datetime
from timestamp import TimeStampImages
from gif import CreateGif

# ---------------------------------------------------------------------------- #
def SaveScreenshot(url, img_name, driver = webdriver.PhantomJS(), load_delay = 15):
    """Takes a screenshot of the given url using the given driver waiting for
    a maximum of load_delay seconds for the page to load saving it as img_name"""

    driver.maximize_window()
    driver.get(url)
    # Wait for the page to load for a maximum of load_delay seconds
    try:
        myElem = WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print "Webpage ready!"
    except TimeoutException:
        print "Webpage imcompletely loaded"

    driver.save_screenshot( "./screenshots/" + img_name)
    print "Screenshot Saved as %s" %(img_name)
# ---------------------------------------------------------------------------- #
def ScreenShotEveryXMins(url, N, M):
    """Saves N screenshots every Xth minute of the hour"""
    i = 10

    for n in range(N):
        print "Screenshot number: %i" %(n+1)
        print "Browser started at second #%i" %(datetime.datetime.now().second)
        starttime = time.time()
        img_name = "screenshot" + str(i) + ".png"
        SaveScreenshot(url, img_name)
        endtime = time.time()
        timetaken = endtime - starttime
        print "Time taken till screenshot: %fs" %(timetaken)
        if timetaken < M * 60:
            time.sleep( M * 60 - timetaken)
        i += 1
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    url = "https://www.google.com/maps/@28.5479169,77.2012027,13.12z/data=!5m1!1e1"

    # PhantomJS
    # driver = webdriver.PhantomJS()
    # Safari
    # driver = webdriver.Safari()

    num_screenshots = 100
    M = 1

    ScreenShotEveryXMins(url, num_screenshots, M)

    TimeStampImages()

    CreateGif("./timestamped/", duration = 0.25)
