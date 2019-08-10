from PIL import Image
import PIL.ImageOps
from numpy import array
import numpy
im = Image.open("part3.1.png")
np_im = numpy.array(im)
print(np_im.shape)
np_im = np_im - 18
new_im = im.convert("L")
new_im.save("gray1.png")
new_im = PIL.ImageOps.invert(new_im)
new_im.save("invert.png")
new_im = im.resize((28,28))
new_im.save("resize.png")