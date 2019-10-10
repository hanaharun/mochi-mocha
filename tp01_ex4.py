"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

### Déclaration des variables

age: int = 0
annee_permis: int = 0
accident: int = 0
annee_assurance: int = 0
tarif_situation: str

### Initialisation des variables

age = int(input("Entrez l'âge : "))
annee_permis = int(input("Entrez le nombre d'année de permis : "))
accident = int(input("Entrez le nombre d'accidents : "))
situation = " "

### Séquence d'opération

# -25 ans et permis -2 ans
if age <= 25 and annee_permis <= 2 and accident == 0:
    tarif_situation = "Rouge"
else:
    tarif_situation = "Refusé"

# - 25 ans et permis
if age <= 25 and annee_permis >= 2 and accident == 0 or age >= 25 and annee_permis <= 2 and accident == 0:
    tarif_situation = "Vert"
elif accident == 1:
    tarif_situation = "Orange"
elif accident == 2:
    tarif_situation = "Rouge"
else:
    tarif_situation = "Refusé"

# Fidélité des clients
annee_assurance = int(input("Entrez le nombre d'années d'assurance : "))
if annee_assurance >= 5:
    tarif_situation = ""

# Message spécifiant la situation du client
print("Votre situation : ", tarif_situation)
