"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
### Déclaration des variables

fumeur: str
sport: str
age: int = 0
sexe: str
risque: int

### Initialisation des variables

# Saisie d'utilisateur

fumeur = input("Êtes-vous fumeur ? (oui ou non) ")
sport = input("Faîtes-vous du sport ? (oui ou non) ")
age = int(input("Quel est votre âge ? "))
sexe = input("Quel est votre sexe ? (h ou f) ")
risque = 0

### Séquence d'opération

# Calcul du niveau de risque

if fumeur == "oui":
    risque = risque + 2
if sport == "oui":
    risque = risque - 1
if sexe == "h" and age >= 50:
    risque += 1
if sexe == "f" and age >= 60:
    risque += 1


# Message spécifiant le niveau de risque obtenu

if risque <= 1:
    print("Le niveau de risque est faible (" + str(risque) + ")")
else:
    print("Le niveau de risque est élevé (" + str(risque) + ")")

