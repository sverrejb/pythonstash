from PIL import Image
im = Image.open("Santa.png")
print (sorted(im.getcolors(im.size[0]*im.size[1]), key=lambda tup: tup[0], reverse=True))[9]