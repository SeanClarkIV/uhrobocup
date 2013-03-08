import time

from PIL import Image, ImageDraw
import numpy

import config

def redballdetection():
    origImage = getImage()                      # Get image from NAO Robot

    filteredImage = colorpick(origImage)        # Remove any pixels that are not red

    #TODO: Identify ball from filtered image

    #TODO: Calculate diameter

    #TODO: Calculate distance and angle

    return

def getImage():
  """
  First get an image from Nao, then show it on the screen with PIL.
  """

  camProxy = config.loadProxy("ALVideoDevice")
  resolution = 1    # 320x240
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = camProxy.getImageRemote(videoClient)

  t1 = time.time()

  # Time the image transfer.
  print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Create a PIL Image from our pixel array.
  origImage = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
  # im.save( str(colorSpace) + ".png", "PNG")

  return origImage

def colorpick(origIm):
    outfile = open('file.txt', 'w') # Open original image

    origWidth = origIm.size[0]      # Get original image's width.
    origHeight = origIm.size[1]     # Get original image's height.
    print "Dimensions - w:", imgWidth, "h:",

#    analysedIm = Image.new("RGB", (origWidth,origHeight), "white")  # Create blank image with same dimendions as original image

#    draw = ImageDraw.Draw(analysedIm)   # Set wich image to draw pixels to.

    matrix = numpy.zeros(shape=(origHeight,origWidth))
    for height in range(0, (origHeight), 1):    # Iterate up to down on image through each pixel.
        outfile.write("\n")
        for width in range (0, (origWidth), 1): # Iterate left to righ on image through each pixel.
            r, g, b = origIm.getpixel((width,height)) # Save each pixel color to variables r,g,b.

            if (r >= 85) and (g <= ((r/4)*3)):  # Find all pixels that have a red hue.
                matrix[height][width] = 1
                matrix = str(matrix)
                outfile.write("1")
            else:
                outfile.write("0")

#                draw.point((width,height), fill=(r,g,b))    # Export only red hue pixels to blank image.
#                del draw    # Stop draw process.

#     analysedIm.save("analysed.jpg", "JPEG")
#     analysedIm.show()
#     print "done"

    return matrix