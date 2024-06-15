import png_to_card as PTC
import os

source_folder = 'source'
destination_folder = "card"
liste = os.listdir('./' + source_folder)

for i in liste : # ici, tout dépend du numéro = bonne chose ?
	number = i[0:2]
	img = PTC.create_card(png_file = './' + source_folder + '/' + i ,font_file = 'Waredosk.otf',number = number)
	img.save('./' + destination_folder + '/' +  number + '.png')
	# img.show()

