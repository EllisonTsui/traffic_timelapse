import imageio
import os
# ---------------------------------------------------------------------------- #
def CreateGif(imagedir, moviename = "movie_out", duration = 0.5):
    """Creates a gif movie for the given image folder with a set duration
    between frames"""

    filenames = os.listdir(imagedir)

    with imageio.get_writer('./' + moviename + '.gif', mode='I', duration = duration) as writer:
        for filename in filenames:
            image = imageio.imread(imagedir + filename)
            writer.append_data(image)
# ---------------------------------------------------------------------------- #
if __name__ == "__init__":
    CreateGif("./timestamped/")
