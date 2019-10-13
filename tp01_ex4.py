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

age: int
annee_permis: int
accident: int
assurance: int
tarif_situation: str

### Initialisation des variables

age = int(input("Entrez l'âge : "))
annee_permis = int(input("Entrez le nombre d'année de permis : "))
accident = int(input("Entrez le nombre d'accidents : "))
assurance = int(input("Entrez le nombre d'années d'assurances : "))
tarif_situation = ""

### Séquence d'opération

# Conducteur : - 25 ans , permis - 2 ans , 0 accident
if age < 25 and annee_permis < 2 and accident == 0 and assurance < 5:
    tarif_situation = "Rouge"
elif age < 25 and annee_permis < 2 and accident == 0 and assurance >= 5:
    tarif_situation = "Orange" # fidélité du client


# Conducteur : - 25 ans , permis + 2 ans OU + 25 ans , permis - 2 ans
elif age < 25 and annee_permis >= 2 and accident == 0 and assurance < 5 or age >= 25 and annee_permis < 2 and accident == 0 and assurance < 5:
    tarif_situation = "Orange"
elif age < 25 and annee_permis >= 2 and accident == 0 and assurance >= 5 or age >= 25 and annee_permis < 2 and accident == 0 and assurance >= 5:
    tarif_situation = "Vert" # fidélité du client
elif age < 25 and annee_permis >= 2 and accident == 1 and assurance < 5 or age >= 25 and annee_permis < 2 and accident == 1 and assurance < 5:
    tarif_situation = "Rouge"
elif age < 25 and annee_permis >= 2 and accident == 1 and assurance >= 5 or age >= 25 and annee_permis < 2 and accident == 1 and assurance >= 5:
    tarif_situation = "Orange" # fidélité du client


# Conducteur : + 25 ans , permis + 2 ans
elif age >= 25 and annee_permis >= 2 and accident == 0 and assurance < 5:
    tarif_situation = "Vert"
elif age >= 25 and annee_permis >= 2 and accident == 0 and assurance >= 5:
    tarif_situation = "Bleu" # fidélité du client
elif age >= 25 and annee_permis >= 2 and accident == 1 and assurance < 5:
    tarif_situation = "Orange"
elif age >= 25 and annee_permis >= 2 and accident == 1 and assurance >= 5:
    tarif_situation == "Vert" # fidélité du client
elif age >= 25 and annee_permis >= 2 and accident == 2 and assurance < 5:
    tarif_situation = "Rouge"
elif age >= 25 and annee_permis >= 2 and accident == 2 and assurance >= 5:
    tarif_situation = "Orange" # fidélité du client
else:
    tarif_situation = "Refusé"


# Message spécifiant la situation du client
print("Votre situation : ", tarif_situation)


