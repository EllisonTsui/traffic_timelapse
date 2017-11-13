# Traffic Time-lapse

## Demo

Created from a cropped section of an outputted video file:

![Demo](https://user-images.githubusercontent.com/18148370/32717620-506a460e-c880-11e7-9f26-eebed5a88748.gif)

## Dependencies

1. selenium (for loading a web-browser in Python)
2. phantomJS (for having an independent web-browser driver)
3. _imagingft (for adding a timestamp to the images)
4. ffmpeg (for making a movie with the images)

### Optional

5. numpy (for using cumsum, can be replaced by a self written function)
6. PROHIBITIVE WITH LARGE DATA SETS: imageio (for making the gif at the end)
