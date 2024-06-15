from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw


FontSize = 24
# font = ImageFont.truetype("times-ro.ttf", 24)
myFont = ImageFont.truetype('./WAFERO Personal Use.otf', FontSize, encoding='utf-8')


img = Image.new('RGB', (600, 400), color = 'red')

draw = ImageDraw.Draw(img)
draw.text((300, 200),"Hello World !",(0,0,0),font=myFont)

img.save('pil_red.png')