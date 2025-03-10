# CardGenerator






# TODO :
- Toutes les cartes en automatiques = v1 basé sur le numéro des cartes
- Un truc qui récupère automatiquement les cartes après le scan d'une feuille = faire facilement sa version en dessinant
- Lien automatique à Latex pour update livret
- Lien avec IA generative pour génrer des trucs automatiquement*
- Improve 6 avec des points positifs = modifie l'utilisation du jeu (jouer sur les doubles lecture des symboles dans les différents jeux, si l'agressivité est bonne en competition, elle est défavorable en coopération, etc?)

## Librairies :
<!-- - pip3 install pypdf2 -->
- pip3 install pypdf2
- sudo apt-get install texlive-latex-base

# Pdf conversion pour le livret (Automatiser ces procédures depuis python ?)

## Pour mettre le livret en vesion imprimable :
- sudo apt-get install texlive-extra-utils
- pdfbook2 --inner-margin=20 Gamadaru_Portrait-1.pdf 

## Pour ajouter la couverture et remettre en place :
- sudo snap install pdftk
- pdftk file1.pdf file2.pdf cat output mergedfile.pdf # pour fusionner 2 pdf
- pdftk Gamadaru_Portrait-1-book.pdf  cat 2-end output outputfile.pdf  # pour selectionner certaines pages

# Règles à ajouter :
- Deck building
- Munchkin
- Undercover
- Radsland
- etc.

# Idée :
Créer une nouvelle ressource ?