from PIL import Image
# Créer l'image en mémoire
image1 = Image.new("RGB",(8,8), (150, 150, 150)) # (8,8) : taille de l'image
# (250, 250, 250) : gris clair, définition de la couleur par défaut
# Ce dernier paramètre est facultatif
# Colorier les pixels
# img.putpixel((0,0), (r, v, b))
image1.putpixel((0,0), (255, 0, 0))
image1.putpixel((4,0), (0, 255, 0))
image1.putpixel((0,6), (0, 0, 255))
image1.putpixel((7,7), (0, 255, 255))
# Afficher l'image
image1.show()
# Sauvegarder l'image - facultatif sur Basthon
#img.save("image1.png")