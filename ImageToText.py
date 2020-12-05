import pytesseract as tess
from PIL import Image
PATH = '/Users/ezulq/Desktop/hqdefault.jpg'
img = Image.open(PATH)
text = tess.image_to_string(img)
print(text)

#this image processing sucks