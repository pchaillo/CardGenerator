from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

def add_type(draw, nb_str,font):
	if nb_str[0] == '6':
		print("dragon")
		txt = "DRAGON"
		_, _, w, h = draw.textbbox((0, 0), txt, font=font)
	draw.text(((1000-w)/2, 20),txt,(0,0,0),font=font)

def add_classic_symbol( classic_nb,font,img,classic_pos,symbol_size,color = "pic"):
	if color == "pic":
		symbol_img = Image.open("./symbol/pic.png")
	elif color == "carreau":
		symbol_img = Image.open("./symbol/carreau.png")
	elif color == "coeur":
		symbol_img = Image.open("./symbol/coeur.png")
	elif color == "trefle":
		symbol_img = Image.open("./symbol/trefle.png")
	symbol_img = symbol_img.resize((symbol_size, symbol_size), Image.LANCZOS)
	symbol_img = symbol_img.convert("RGBA")
	img = img.convert("RGBA")
	img.alpha_composite(symbol_img, dest=(60, classic_pos))
	draw = ImageDraw.Draw(img)	
	draw.text((20 , classic_pos),str(classic_nb),(0,0,0),font=font) # numéro carte classique

	return img

def create_card(png_file,font_file,number): # Créer un classe carte

	card_size = 1000 # arbitraire, à mettre en argument ?
	FontSize = 90
	BigFontSize = 150

	symbol_size = 50 

	classic_nb = 5 # Avec 11 = valet, 12 = cavalier, 13 = dame, 14 = roi et 1 = AS
	classic_pos = 930 # nombre de pixel de décalage vers le bas

	classicFont = ImageFont.truetype(font_file, 60, encoding='utf-8') # Charge les polices aux bonnes tailles
	myFont = ImageFont.truetype(font_file, FontSize, encoding='utf-8') # Charge les polices aux bonnes tailles
	myBigFont = ImageFont.truetype(font_file, BigFontSize, encoding='utf-8')

	img = Image.open(png_file) # Charge l'image et la redimensionne
	img = img.resize((card_size, card_size), Image.LANCZOS)

	nb_str = str(number) # Passage du nombre en liste de characteres
	nb_str = list(nb_str)

	draw = ImageDraw.Draw(img)	# Ajout du nombre
	draw.text((20, 20),nb_str[0],(0,0,0),font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],(0,0,0),font=myFont)

	add_type(draw, nb_str,myFont)
	img = add_classic_symbol(classic_nb=classic_nb,img=img,classic_pos=classic_pos,color = "pic",font = classicFont,symbol_size=symbol_size)

	img = img.rotate(180)
	draw = ImageDraw.Draw(img)	
	draw.text((20, 20),nb_str[0],(0,0,0),font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],(0,0,0),font=myFont)
	img = add_classic_symbol(classic_nb=classic_nb,img=img,classic_pos=classic_pos,color = "trefle",font = classicFont,symbol_size=symbol_size)

	img = img.rotate(180)

	img.save('carte_test2.png')
	print("Card Created")

create_card(png_file = "purple_drag.png",font_file = 'Waredosk.otf',number = 68)


## ## Back up : ## ##
# # Dimension unique des cartes (complètement arbitraire pour l'instant : 1000*1000pixels)
# card_size = 1000
# FontSize = 50
# # font = ImageFont.truetype("times-ro.ttf", 24)
# myFont = ImageFont.truetype('./WAFERO Personal Use.otf', FontSize, encoding='utf-8')
# img = Image.open("purple_drag.png")
# # imgArray = np.array(img)
# img = img.resize((card_size, card_size), Image.LANCZOS)
# draw = ImageDraw.Draw(img)
# draw.text((20, 20),"Hello World !",(0,0,0),font=myFont)
# img.save('crad_test2.png')
# print("Card Created")