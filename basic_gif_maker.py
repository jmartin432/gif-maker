from PIL import Image
import imageio
import colorsys
import numpy
from string import Template

destinationFile = 'face_dream.gif'
gifPath = Template('./gifs/$fileName')

initial_image = Image.open('./assets/face_dream/face.jpg')
numpyImage = numpy.asarray(initial_image)

images = [numpy.asarray(initial_image)]

for i in range(12):
    print("Adding image: " + str(i))
    image_path = './assets/face_dream/face_dream_{}.jpg'.format(i)
    image = Image.open(image_path)

    images.append(numpy.asarray(image))

for i in range(11, -1, -1):
    print("Adding image: " + str(i))
    image_path = './assets/face_dream/face_dream_{}.jpg'.format(i)
    image = Image.open(image_path)

    images.append(numpy.asarray(image))

print(len(images))
imageio.mimsave(gifPath.substitute(fileName=destinationFile), images)
