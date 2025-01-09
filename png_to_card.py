from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

class Gamadar:
	"""
	Classe qui contient toutes les variables et spécificités selectionnables des jeux =  Configuration du jeu
	"""
	def __init__(self, FAMANARU = True, GAMATRON = True, CLASSIC_CARDS = True):
		self.FAMANARU = FAMANARU
		self.GAMATRON = GAMATRON
		self.CLASSIC_CARDS = CLASSIC_CARDS

def add_sous_titre(draw, txt,font,font_color,BOLD = True): # Faire des types modulaires + basé sur les numéros c'est le top ?
	_, _, w, h = draw.textbbox((0, 0), txt, font=font)
	if BOLD :
		draw.text(((1000-w)/2, 850),txt,font_color,font=font,stroke_width=1,stroke_fill=font_color)
	else :
		draw.text(((1000-w)/2, 850),txt,font_color,font=font)


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

def add_icon( img, symbol_size,  file_img, pos_x, nb = 5, print_flag = False ):
	# symbol_img = Image.open("./symbol/fight.png")file_img
	symbol_img = Image.open(file_img)
	symbol_img = symbol_img.resize((symbol_size, symbol_size), Image.LANCZOS)
	symbol_img = symbol_img.convert("RGBA")
	img = img.convert("RGBA")
	for i in range(nb):
		img.alpha_composite(symbol_img, dest=(pos_x, 500 + int( i*(symbol_size+5) ) ) )
	if print_flag :
		print("Carte associée à l'image " + str(symbol_img) )

	return img

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

	if no_symbol == False and classic_value != '21' and classic_value != 'EX' : # Exceptions pour 21 et excuse, ou on ne met pas le symbole de trefle
		symbol_img = symbol_img.resize((symbol_size, symbol_size), Image.LANCZOS)
		symbol_img = symbol_img.convert("RGBA")
		img = img.convert("RGBA")
		# x_pos = int(50 + symbol_size/2)
		img.alpha_composite(symbol_img, dest=(50, classic_pos + 25 - int(symbol_size/2) ) ) # Petit rectificatif pour que ça reste centré quelquesoit la taille du symbole

	draw = ImageDraw.Draw(img)	
	draw.text((20 , classic_pos),classic_value,font_color,font=font,stroke_width=1,stroke_fill=font_color) # numéro carte classique

	return img

def classic_card_from_number(nb_str,color,print_flag = False): 
	"""
	Calcule la valeur de la carte, compatible avec taror (cavalier + atouts)
	"""
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
			elif unit == 7 :
				valeur = '21' # Carte 97 = 21
			elif unit == 3 :
				valeur = 'EX' # Carte 93 = Excuse
	else :
		if unit == 9:
			base = 10
		else :
			base = 0

		valeur = str(base + 1 + int(nb_str[0]))


	if print_flag :
		print("Valeur " + str(valeur) + " associées au numéro " + nb_str)

	return valeur

def add_famanaru_symbol(nb_str,img,symbol_size,classic_pos,print_flag = False):
	no_symbol = False
	if nb_str[0] == '2': # des fonctions avec des suites de if c'est pas élégant = au moins factoriser en une fonction abstractable
		symbol_img = Image.open("./symbol/inversion.png") # l'image est rechargée à chaque fois = pas opti !
		fact = 1
	elif nb_str[0] == '0':
		symbol_img = Image.open("./symbol/trou_noir_0_voisins.png")
		fact = 2
	elif nb_str[0] == '1':
		symbol_img = Image.open("./symbol/jumeaux_ligne.png")
		fact = 2
	elif nb_str[0] == '4':
		symbol_img = Image.open("./symbol/loups_ligne.png")
		fact = 2
	elif nb_str[0] == '7':
		symbol_img = Image.open("./symbol/troll_no_voisin.png")
		fact = 2
	elif nb_str[0] == '6':
		symbol_img = Image.open("./symbol/dragon_superpos.png")
		fact = 1
	else :
		no_symbol = True

	if no_symbol == False : 
		symbol_img = symbol_img.resize((symbol_size*fact, symbol_size*fact), Image.LANCZOS)
		symbol_img = symbol_img.convert("RGBA")
		img = img.convert("RGBA")
		img.alpha_composite(symbol_img, dest=(500, classic_pos + 25 - int(symbol_size*fact/2) )) # en bas au milieu
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

def add_99_number(img,nb_str,font_color,myBigFont,myFont,BigFontSize, BOLD = True):

	draw = ImageDraw.Draw(img)	# Ajout du nombre
	if BOLD :
		draw.text((20, 20),nb_str[0],font_color,font=myBigFont,stroke_width=1,stroke_fill=font_color)
		draw.text((20 + BigFontSize/2 + 7 , 20),nb_str[1],font_color,font=myFont,stroke_width=1,stroke_fill=font_color)
	else :
		draw.text((20, 20),nb_str[0],font_color,font=myBigFont)
		draw.text((20 + BigFontSize/2 + 7 , 20),nb_str[1],font_color,font=myFont)
	return draw

def create_card(png_file,font_file,number,game_config,print_flag = True,card_name = None, description = None): # Créer un classe carte, avec ces caractéristiques (plus propre et moins d'arguments)

	if print_flag :
		print("Begin generation of card number : " + number )

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

	if description != None : # carte en dehors de l'extension
		draw = add_99_number(img,nb_str,font_color,myBigFont,myFont,BigFontSize)

		# txt = "test" # Pour ajouter un sous-titre à la carte
		# add_sous_titre(draw, txt,font=classicFont,font_color=font_color)

		if card_name == None :
			add_type(draw, nb_str,myFont,font_color = font_color)
		else :
			_, _, w, h = draw.textbbox((0, 0), card_name, font=myFont)
			draw.text(((1000-w)/2, 20),card_name,font_color,font=myFont,stroke_width=1,stroke_fill=font_color)

		if game_config.CLASSIC_CARDS :
			valeur = classic_card_from_number(nb_str,color)
			if valeur != None :
				img = add_classic_symbol(classic_value=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

		if game_config.FAMANARU :
			img = add_famanaru_symbol(nb_str = nb_str,img = img,symbol_size = symbol_size,classic_pos=classic_pos,print_flag=print_flag)

		if game_config.GAMATRON :
			if color == 'atout':
				if nb_str[0] == '7' or nb_str[0] == '6' :
					img = add_icon( img, symbol_size,pos_x = 900, file_img = "./symbol/planete.png", nb = 2)
				if nb_str[0] == '8' or nb_str[0] == '5' :
					img = add_icon( img, symbol_size,pos_x = 900, file_img = "./symbol/planete.png", nb = 3)
				else :
					img = add_icon( img, symbol_size,pos_x = 900, file_img = "./symbol/planete.png", nb = 1)
			if nb_str[0] == '7':
				img = add_icon( img, symbol_size,pos_x = 10, file_img = "./symbol/fight.png", nb = 2)
			elif nb_str[0] == '8':
				img = add_icon( img, symbol_size,pos_x = 10, file_img = "./symbol/fight.png", nb = 3)
			elif nb_str[0] == '9':
				img = add_icon( img, symbol_size,pos_x = 10, file_img = "./symbol/fight.png", nb = 5)


		img = img.rotate(180) # rotation pour placer l'autre texte 
		add_99_number(img,nb_str,font_color,myBigFont,myFont,BigFontSize)
		if game_config.CLASSIC_CARDS and valeur != None :
			img = add_classic_symbol(classic_value=valeur,img=img,classic_pos=classic_pos,color = color,font = classicFont,symbol_size=symbol_size,font_color = font_color)

		img = img.rotate(180)

	# else : # cartes de l'extension


	return img


if __name__ == '__main__':
	game_config = Gamadar()
	img = create_card(png_file = "purple_drag.png",font_file = 'Waredosk.otf',number = '22',game_config=game_config)
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