from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

class Gamadar:
	"""
	Classe qui contient toutes les variables et spécificités selectionnables des jeux =  Configuration du jeu
	"""
	def __init__(self, FAMANARU = True, CLASSIC_CARDS = True):
		self.FAMANARU = FAMANARU
		self.CLASSIC_CARDS = CLASSIC_CARDS

def add_type(draw, nb_str,font,font_color,BOLD = True): # Faire des types modulaires + basé sur les numéros c'est le top ?
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
	if BOLD :
		draw.text(((1000-w)/2, 20),txt,font_color,font=font,stroke_width=1,stroke_fill=font_color)
	else :
		draw.text(((1000-w)/2, 20),txt,font_color,font=font)

def add_classic_symbol( classic_value,font,img,classic_pos,symbol_size,font_color,color = "pic"):
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
		# x_pos = int(50 + symbol_size/2)
		img.alpha_composite(symbol_img, dest=(50, classic_pos + 25 - int(symbol_size/2) ) ) # Petit rectificatif pour que ça reste centré quelquesoit la taille du symbole
		draw = ImageDraw.Draw(img)	
		draw.text((20 , classic_pos),classic_value,font_color,font=font) # numéro carte classique

	return img

def classic_card_from_number(nb_str,color,print_flag = True): 
	valeur = None
	unit = int(nb_str[1])
	if color != "atout" :
	# 	valeur = None
	# else :
		if nb_str[0] == '0':
			valeur = str(2 + unit%2)
		if nb_str[0] == '1':
			valeur = str(4 + unit%2)
		if nb_str[0] == '2':
			valeur = str(6 + unit%2)
		if nb_str[0] == '3':
			valeur = str(8 + unit%2)
		if nb_str[0] == '4':
			if unit%2 == 0 :
				valeur = str(10)
		if nb_str[0] == '5':
			if unit%2 == 0 :
				valeur = 'V'
		if nb_str[0] == '6':
			if unit%2 == 0 :
				valeur = 'C'
		if nb_str[0] == '7':
			if unit%2 == 0 :
				valeur = 'D'
		if nb_str[0] == '8':
			if unit%2 == 0 :
				valeur = "R"
		if nb_str[0] == '9':
			if unit%2 == 0 :
				valeur = '1'

	if print_flag :
		print("Valeur " + str(valeur) + " associées au numéro " + nb_str)

	return valeur

def add_famanaru_symbol(nb_str,img,symbol_size,classic_pos,print_flag = False):
	no_symbol = False
	if nb_str[0] == '2': # des fonctions avec des suites de if c'est pas élégant = au moins factoriser en une fonction abstractable
		symbol_img = Image.open("./symbol/inversion.png")
	elif nb_str[0] == '0':
		symbol_img = Image.open("./symbol/trou_noir_0_voisins.png")
	elif nb_str[0] == '1':
		symbol_img = Image.open("./symbol/jumeaux_ligne.png")
	elif nb_str[0] == '4':
		symbol_img = Image.open("./symbol/loups_ligne.png")
	elif nb_str[0] == '4':
		symbol_img = Image.open("./symbol/loups_ligne.png")
	elif nb_str[0] == '7':
		symbol_img = Image.open("./symbol/troll_no_voisin.png")
	elif nb_str[0] == '6':
		symbol_img = Image.open("./symbol/dragon_superpos.png")
	else :
		no_symbol = True

	if no_symbol == False : 
		symbol_img = symbol_img.resize((symbol_size, symbol_size), Image.LANCZOS)
		symbol_img = symbol_img.convert("RGBA")
		img = img.convert("RGBA")
		img.alpha_composite(symbol_img, dest=(500, classic_pos + 25 - int(symbol_size/2) )) # en bas au milieu
		draw = ImageDraw.Draw(img)	

		if print_flag :
			print("Numero " + nb_str + " associé à l'image " + str(symbol_img) )

	return img

def font_from_number(nb_str,print_flag = False):  # TODO = couleur + modulaire (facile à choisir) (dictionnaire, ou variable de classe ? )
	
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

	if print_flag :
		print("Numero " + nb_str + " associé à la couleur " + color + " de valeur " + str(font_color))

	return font_color,color

def create_card(png_file,font_file,number,game_config,print_flag = False): # Créer un classe carte, avec ces caractéristiques (plus propre et moins d'arguments)

	card_size = 1000 # arbitraire, à mettre en argument ?
	FontSize = 90
	BigFontSize = 150

	symbol_size = 70 

	classic_nb = 5 # Avec 11 = valet, 12 = cavalier, 13 = dame, 14 = roi et 1 = AS
	classic_pos = 930 # nombre de pixel de décalage vers le bas, pour accéder la position de la ligne du bas, celle ou le symbole de carte classsique sera posé (nom de variable nul)

	classicFont = ImageFont.truetype(font_file, 60, encoding='utf-8') # Charge les polices aux bonnes tailles
	myFont = ImageFont.truetype(font_file, FontSize, encoding='utf-8') # Charge les polices aux bonnes tailles
	myBigFont = ImageFont.truetype(font_file, BigFontSize, encoding='utf-8')

	img = Image.open(png_file) # Charge l'image et la redimensionne
	img = img.resize((card_size, card_size), Image.LANCZOS)

	# nb_str = str(number) # Passage du nombre en liste de characteres
	# nb_str = list(nb_str)
	nb_str = number

	font_color,color = font_from_number(nb_str,print_flag = print_flag)
	
	draw = ImageDraw.Draw(img)	# Ajout du nombre
	draw.text((20, 20),nb_str[0],font_color,font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],font_color,font=myFont)

	add_type(draw, nb_str,myFont,font_color = font_color)

	if game_config.CLASSIC_CARDS :
		valeur = classic_card_from_number(nb_str,color)
		if valeur != None :
			img = add_classic_symbol(classic_value=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

	if game_config.FAMANARU :
		img = add_famanaru_symbol(nb_str = nb_str,img = img,symbol_size = symbol_size,classic_pos=classic_pos,print_flag=True)

	img = img.rotate(180) # rotation pour placer l'autre texte 
	draw = ImageDraw.Draw(img)	
	draw.text((20, 20),nb_str[0],font_color,font=myBigFont)
	draw.text((20 + BigFontSize/2 +5 , 20),nb_str[1],font_color,font=myFont)
	if game_config.CLASSIC_CARDS and valeur != None :
		img = add_classic_symbol(classic_value=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

	img = img.rotate(180)

	return img


if __name__ == '__main__':
	game_config = Gamadar()
	img = create_card(png_file = "purple_drag.png",font_file = 'Waredosk.otf',number = '62',game_config=game_config)
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