"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration des variables

prix: int
rabais_etu: int
rabais_mem: int
rabais_fam: int
carte_mens: str
carte_mem: str
carte_etu: str
forfait_fam: str

### Initialisation des variables

prix = 10
rabais_etu = 2
rabais_mem = 3
forfait_fam = 1
carte_mens = input("Possédez-vous la carte mensuelle ? (oui ou non) ")

### Séquence d'opération

# Cas : pour ceux qui ont la carte mensuelle
if carte_mens == "oui":
    prix = prix - prix
    print("Le prix à payer est : " + str(prix) + "CHF")

# Cas : pour ceux qui n'ont pas de carte mensuelle
else:
    carte_mem = input("Possédez-vous la carte membre ? (oui ou non) ")
    carte_etu = input("Possédez-vous la carte étudiante (oui ou non) ")
    forfait_fam = input("Bénéficiez-vous du forfait famille ? (oui ou non) ")


# Cas : rabais normaux
    if carte_mem == "oui" and carte_etu == "non" and forfait_fam == "non":
        prix = prix - rabais_mem
    elif carte_etu == "oui" and carte_mem == "non" and forfait_fam == "non":
        prix = prix - rabais_etu
    elif forfait_fam == "oui" and carte_mem == "non" and carte_etu == "non":
        prix = prix - rabais_fam

# Cas : tous les rabais
    if carte_mem == "oui" and carte_etu == "oui":
        prix = prix - rabais_mem - rabais_etu
    elif carte_etu == " oui" and forfait_fam == "oui":
        prix = prix - rabais_etu
    elif carte_mem == "oui" and forfait_fam == "oui":
        prix = prix - rabais_mem - rabais_fam
    elif carte_mem == "oui" and carte_etu == "oui" and forfait_fam == "oui":
        prix = prix - rabais_mem - rabais_etu
    else:
        prix = prix


# Message spécifiant le prix à payer
    print("Le prix à payer est : " + str(prix) + "CHF")
