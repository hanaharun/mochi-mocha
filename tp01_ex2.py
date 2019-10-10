"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables

SANDWICH: float = 4.90
CHIPS: float = 2.50
CHOCOLAT: float = 2.00
BONBONS: float = 3.30
TEA: float = 2.20
LIMONADE: float = 1.90
sandwich_poulet: int = 1
chips_paprika: int = 2
barre_choco: int = 3
bonbon: int = 4
ice_tea: int = 5
limonade: int = 6
monnaie: float = 0.0
produit: str
rendu: float = 0.0
prix = float = 0.0
nom_produit: str
phrase: str


###Initialisation des variables

nom_produit = ""
monnaie: float = float(input("Veuillez introduire votre monnaie : "))
produit: str = str(input("Veuillez sélectionner un produit : "))

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")


if produit == 1:
    prix = 4.90
    nom_prod = "Sandwich au poulet"
elif produit == 2:
    prix = 2.50
    nom_produit = "Chips Paprika"
elif produit == 3:
    prix = 2.00
    nom_prdotuit = "Barre chocolatée"
elif produit == 4:
    prix = 3.30
    nom_produit = "Bonbons"
elif produit == 5:
    prix = 2.20
    nom_produit = "Ice Tea"
elif produit == 6:
    prix = 1.90
    nom_produit = "Limonade"



if monnaie > prix:
    rendu = monnaie - prix
    print("Monnaie à rendre : ", round(rendu, 2))
    print(nom_produit, phrase)
else:
    print(nom_produit, phrase)








