import png_to_card as PTC
import os

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

source_folder = 'source'
destination_folder = "cartes"
liste = os.listdir('./' + source_folder)
back_card = './symbol/back.png'

# GENERATE_CARDS = True

c = canvas.Canvas('page.pdf')

ind_ligne = 0
ind_colonne = 0


def fill_page(page,back_card): # mauvaise factorisation du code = faire un truc + propre
	ind_ligne = 0
	ind_colonne = 0
	for i in range(20):
		if ind_ligne > 3 :
			ind_colonne += 1
			ind_ligne = 0
		page.drawImage(back_card, ind_ligne*5*cm, ind_colonne*5*cm, 5*cm, 5*cm)
		ind_ligne += 1
	return page


for i in liste : # ici, tout dépend du numéro = bonne chose ?
	number = i[0:2]
	img = PTC.create_card(png_file = './' + source_folder + '/' + i ,font_file = 'Waredosk.otf',number = number)
	card_name = './' + destination_folder + '/' +  number + '.png'
	img.save(card_name)
	print("Carte n° " + str(number) + " générée")
	# img.show()

	
	if ind_ligne > 3 :
		ind_colonne += 1
		ind_ligne = 0

	if ind_colonne > 4 :
		c.showPage()
		fill_page(page = c ,back_card=back_card)
		c.showPage()
		ind_colonne = 0

	c.drawImage(card_name, ind_ligne*5*cm, ind_colonne*5*cm, 5*cm, 5*cm)
	# c.showPage()
	ind_ligne += 1

c.showPage() # On ajoute la dernière page de dos
fill_page(page = c ,back_card=back_card)
c.showPage()	
c.save()
print("PDF saved")
