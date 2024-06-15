import numpy as np
from PIL import Image, ImageDraw, ImageFont
from string import ascii_lowercase, ascii_uppercase

img = Image.open("marylin.png")
imgArray = np.array(img)

tmp = Image.new('RGB', ( imgArray.shape[1] , imgArray.shape[0] ) , 'white' )
image_result = ImageDraw.Draw(tmp)

FontSize = 3

# myFont = ImageFont.truetype('arial.ttf', 12) # n'arrive pas à importer la ressource !
# myFont = ImageFont.load_default()
myFont = ImageFont.truetype('./WAFERO Personal Use.otf', FontSize, encoding='utf-8')

lorem = open("bullshit.txt", "r" , encoding='utf8').read()
c = 0 # compteur de position de la lettre dans lorem

print("Value :")
print(imgArray)
print(imgArray.shape)
print(imgArray[0,0])

for y in range( 0 , imgArray.shape[0] , FontSize):
    for x in range( 0 , imgArray.shape[1] , FontSize ):
        # b,w = imgArray[y, x] # r, v, b, t       
        # if (b,w) == (255,255):
        b = imgArray[y, x] # r, v, b, t   
        # print(b)    
        if b > 10:
            image_result.text((x, y), lorem[c].upper(), font=myFont, fill=(110, 110, 101))
        else:
            image_result.text((x, y), lorem[c].upper(), font=myFont, fill=(250, 250, 250)) 
        c += 1

tmp.save('result2.jpg')


imagePlage = Image.open("./symbol/pic.png")

# imageChat = Image.open("chat.jpg")
imagePlage = imagePlage.convert("RGBA")
img = img.convert("RGBA")

img.alpha_composite(imagePlage, dest=(0, 0))

img.save("result.png")
img.show()