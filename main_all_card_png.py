import png_to_card as PTC
import os
import pandas as pd

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

source_folder = 'source'
destination_folder = "cartes"
liste = os.listdir('./' + source_folder)
back_card = './symbol/back.png'

BASE = False
NUMBER = True # True = number from card name // False = Random number and card name from png name
EXTENSION = True

# GENERATE_CARDS = True

c = canvas.Canvas('All_Cards.pdf')

ind_ligne = 0
ind_colonne = 0

game_config = PTC.Gamadar()

taille_carte = 5 
shift = 0.3
used_shift = taille_carte + shift # pour mettre de petite marges entre les cartes
vertical_shift = taille_carte + shift*2

def print_card_on_page(ind_ligne,ind_colonne,card_name,c,back_card,taille_carte,used_shift): # appelle aussi la fonction fill_page, pour réaliser les dossiers de manière automatique
	if ind_ligne > 3 :
		ind_colonne += 1
		ind_ligne = 0

	if ind_colonne > 4 :
		c.showPage()
		fill_page(page = c ,back_card=back_card,used_shift=used_shift,taille_carte=taille_carte)
		c.showPage()
		ind_colonne = 0

	c.drawImage(card_name, ind_ligne*used_shift*cm, ind_colonne*used_shift*cm, taille_carte*cm, taille_carte*cm)
	# c.showPage()
	ind_ligne += 1

	return ind_ligne, ind_colonne

def fill_page(page,back_card,used_shift,taille_carte): # mauvaise factorisation du code = faire un truc + propre + Faire quelquechose qui remplit les pages automatiquement en fonction de la taille de la page
	ind_ligne = 0
	ind_colonne = 0
	for i in range(20):
		if ind_ligne > 3 :
			ind_colonne += 1
			ind_ligne = 0
		page.drawImage(back_card, ind_ligne*used_shift*cm, ind_colonne*used_shift*cm, taille_carte*cm, taille_carte*cm)
		ind_ligne += 1
	return page

card_ind = 0

if BASE :
	for i in liste : # ici, tout dépend du numéro = bonne chose ?

		if NUMBER :
			number = i[0:2]
			img = PTC.create_card(png_file = './' + source_folder + '/' + i ,font_file = 'Waredosk.otf',number = number,game_config=game_config)
		else :
			if card_ind < 10 :
				number = '0' + str(card_ind)
			else :
				number = str(card_ind)
			card_ind += 1
			img = PTC.create_card(png_file = './' + source_folder + '/' + i ,font_file = 'Waredosk.otf',number = number,game_config=game_config,card_name =i[:-4])

		card_name = './' + destination_folder + '/' +  number + '.png'
		img.save(card_name)
		print("Carte n° " + str(number) + " générée")
		# img.show()

		ind_ligne, ind_colonne = print_card_on_page(ind_ligne,ind_colonne,card_name,c,back_card,taille_carte,used_shift)

if EXTENSION :
	liste_ext = os.listdir('./extension/description')
	for j in liste_ext :
		df = pd.read_csv('./extension/description/' + j)
		print(df)
		info=df.loc[0,"Name"]
		print(str(info))
		img = PTC.create_card('./extension/img/'  + img_file ,font_file = 'Waredosk.otf',number = number,game_config=game_config,description = df)
	

c.showPage() # On ajoute la dernière page de dos
fill_page(page = c ,back_card=back_card,used_shift=used_shift,taille_carte=taille_carte)
c.showPage()	
c.save()
print("PDF saved")
