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

monnaie_initiale: float
message: str
nom_produit: str
prix: float
monnaie_rendue: float


###Initialisation des variables

monnaie_initiale = 0.0
message = ""
nom_produit = ""
prix = 0.0
monnaie_rendu = 0.0



### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")


# Saisie d'utilisateur
monnaie_initiale = float(input("Veuillez introduire votre monnaie : "))
produit = int(input("Veuillez sélectionner un produit : "))


# Prix et noms des produits

if produit == 1:
    prix = 4.90
    nom_produit = "Sandwich au poulet"
elif produit == 2:
    prix = 2.50
    nom_produit = "Chips Paprika"
elif produit == 3:
    prix = 2.00
    nom_produit = "Barre chocolatée"
elif produit == 4:
    prix = 3.30
    nom_produit = "Bonbons"
elif produit == 5:
    prix = 2.20
    nom_produit = "Ice Tea"
else:
    prix = 1.90
    nom_produit = "Limonade"


# Message décrivant la commande

if produit == 1:
    message = "servi ! Bon appétit !"
elif produit == 2:
    message = "servies ! Bon appétit !"
elif produit == 3:
    message = "servie ! Bon appétit !"
elif produit == 4:
    message = "servis ! Bon apépétit !"
elif produit == 5:
    message = "servi ! Santé !"
else:
    message = "servie ! Santé !"


# Calcul de la monnaie rendue

if monnaie_initiale > prix:
    monnaie_rendue = monnaie_initiale - prix
    print("Monnaie à rendre : ", round(monnaie_rendue, 2))
    print(nom_produit, message)
else:
    print(nom_produit, message)
