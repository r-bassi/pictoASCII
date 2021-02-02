from sys import argv
from PIL import Image, ImageOps
from math import floor

# Best representation with simplest characters
# Thanks to http://paulbourke.net/dataformats/asciiart/
# Reverse character order to invert image shading for dark mode: " .:-=+*#%@"
characters = "@%#*+=-:. "

if len(argv) < 3:
    print("Input sequence: python pictoASCII.py -scale pixelNumber imageFile.jpg outputFile.txt")
    print("For more information see README.md")
    input()
    exit()

# argument handling using argv array
cmdArg = 0
for i in range(len(argv)):
    if argv[i] == "-scale":
        cmdArg += 2
        maxScaling = int(argv[i + 1])

srcPic = argv[1 + cmdArg]
outFile = argv[2 + cmdArg]

# open source image
inputImage = Image.open(srcPic)

# scale and antialias input image if specified
if "maxScaling" in globals():
    inputImage.thumbnail((maxScaling, maxScaling), Image.ANTIALIAS)

# clear output file, truncate file to zero length or create text file for writing
with open(outFile, "w") as temp:
    temp.write("")

# function to prevent array out of bounds error
scale = lambda num, max: num if num < max else max - 1

# turn image to grayscale using Pillow, grayscale value range: 0-255
grayedImage = ImageOps.grayscale(inputImage)

# pixels are loaded as a 2d array, pixel[x,y]
pixel = grayedImage.load()

with open(outFile, "a") as output:
    grayScaled = len(characters) / 255
    for y in range(grayedImage.size[1]):
        outStr = ""
        for x in range(grayedImage.size[0]):
            charIndex = scale(floor(int(pixel[x, y]) * grayScaled), len(characters))
            outStr += characters[charIndex]
        output.write(outStr + "\n")
