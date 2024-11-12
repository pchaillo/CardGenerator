from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

def add_type(draw, nb_str,font,font_color):
	if nb_str[0] == '0':
		txt = "TROU NOIR"
	if nb_str[0] == '1':
		txt = "JUMEAUX"
	if nb_str[0] == '2':
		txt = "VOLEUR"
	if nb_str[0] == '3':
		txt = "LUNE"
	if nb_str[0] == '4':
		txt = "LOUP"
	if nb_str[0] == '5':
		txt = "SOLEIL"
	if nb_str[0] == '6':
		txt = "DRAGON"
	if nb_str[0] == '7':
		txt = "MONSTRE"
	if nb_str[0] == '8':
		txt = "CRYPTIDE"
	if nb_str[0] == '9':
		txt = "DIEU"
	_, _, w, h = draw.textbbox((0, 0), txt, font=font)
	draw.text(((1000-w)/2, 20),txt,font_color,font=font)

def add_classic_symbol( classic_nb,font,img,classic_pos,symbol_size,font_color,color = "pic"):
	no_symbol = False
	if color == "pic":
		symbol_img = Image.open("./symbol/pic.png")
	elif color == "carreau":
		symbol_img = Image.open("./symbol/carreau.png")
	elif color == "coeur":
		symbol_img = Image.open("./symbol/coeur.png")
	elif color == "trefle":
		symbol_img = Image.open("./symbol/trefle.png")
	elif color == "atout" :
		no_symbol = True

	if no_symbol == False : 
		symbol_img = symbol_img.resize((symbol_size, symbol_size), Image.LANCZOS)
		symbol_img = symbol_img.convert("RGBA")
		img = img.convert("RGBA")
		img.alpha_composite(symbol_img, dest=(60, classic_pos))

	draw = ImageDraw.Draw(img)	
	draw.text((20 , classic_pos),str(classic_nb),font_color,font=font) # numéro carte classique

	return img

def classic_card_from_number(nb_str,color): 
	valeur = None
	unit = int(nb_str[1])
	if color != "atout" :
	# 	valeur = None
	# else :
		if nb_str[0] == '0':
			valeur = 2 + unit%2
		if nb_str[0] == '1':
			valeur = 4 + unit%2
		if nb_str[0] == '2':
			valeur = 6 + unit%2
		if nb_str[0] == '3':
			valeur = 8 + unit%2
		if nb_str[0] == '4':
			if unit%2 == 0 :
				valeur = 10
		if nb_str[0] == '5':
			if unit%2 == 0 :
				valeur = 11
		if nb_str[0] == '6':
			if unit%2 == 0 :
				valeur = 12
		if nb_str[0] == '7':
			if unit%2 == 0 :
				valeur = 13
		if nb_str[0] == '8':
			if unit%2 == 0 :
				valeur = 14
		if nb_str[0] == '9':
			if unit%2 == 0 :
				valeur = 1

	return valeur

def font_from_number(nb_str):  # TODO = couleur + modulaire (facile à choisir) (dictionnaire, ou variable de classe ? )
	if nb_str[1] == '0' or nb_str[1] == '1' :
		font_color = (0,0,0) # NOIR
		color = "pic"
	elif nb_str[1] == '2' or nb_str[1] == '3' :
		font_color = (0,153,0) # VERT
		color = "trefle"
	elif nb_str[1] == '4' or nb_str[1] == '5' :
		font_color = (51,153,250) # BLUE
		color = "carreau"
	elif nb_str[1] == '6' or nb_str[1] == '7' :
		font_color = (204,0,0) # ROUGE
		color = "coeur"
	elif nb_str[1] == '8' or  nb_str[1] == '9' :
		font_color = (128,0,128) # VIOLET
		color = "atout"
	return font_color,color

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

	# nb_str = str(number) # Passage du nombre en liste de characteres
	# nb_str = list(nb_str)
	nb_str = number

	font_color,color = font_from_number(nb_str)
	valeur = classic_card_from_number(nb_str,color)

	draw = ImageDraw.Draw(img)	# Ajout du nombre
	draw.text((20, 20),nb_str[0],font_color,font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],font_color,font=myFont)

	add_type(draw, nb_str,myFont,font_color = font_color)
	img = add_classic_symbol(classic_nb=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

	img = img.rotate(180)
	draw = ImageDraw.Draw(img)	
	draw.text((20, 20),nb_str[0],font_color,font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],font_color,font=myFont)
	img = add_classic_symbol(classic_nb=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

	img = img.rotate(180)

	return img


if __name__ == '__main__':
	img = create_card(png_file = "purple_drag.png",font_file = 'Waredosk.otf',number = '68')
	img.save('carte_temoin.png')
	print("Card Created")


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