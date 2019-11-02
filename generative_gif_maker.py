from PIL import Image
import imageio
import colorsys
import numpy
from string import Template


startFile = 'me.jpg'
destinationFile = 'me.gif'
imagePath = Template('./assets/$fileName')
gifPath = Template('./gifs/$fileName')
image = Image.open(imagePath.substitute(fileName=startFile))
numpyImage = numpy.asarray(image)

width, height = image.size
pixels = image.load()
images = []

for k in range(20):
    print(k)
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r + 13) % 256
            g = (g + 13) % 256
            b = (b + 13) % 256

            pixels[i, j] = (r, g, b)

    images.append(numpy.asarray(image))

imageio.mimsave(gifPath.substitute(fileName=destinationFile), images)
