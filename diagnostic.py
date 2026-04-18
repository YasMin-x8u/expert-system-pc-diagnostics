regles = [
    (["ventilateur_tourne", "ecran_noir"], "probleme_carte_graphique"),
    (["ordinateur_ne_sallume_pas", "odeur_brule"], "alimentation_defaillante"),
    (["bip_demarrage", "ecran_noir"], "probleme_memoire"),
    (["ordinateur_ne_sallume_pas", "ventilateur_tourne"], "probleme_bouton_power"),
    (["probleme_carte_graphique"], "panne_materielle"),
    (["alimentation_defaillante"], "panne_materielle"),
    (["probleme_memoire"], "panne_materielle"),
]

symptomes = {
    "1": "ordinateur_ne_sallume_pas",
    "2": "ecran_noir",
    "3": "bip_demarrage",
    "4": "ventilateur_tourne",
    "5": "odeur_brule"
}

print("Selectionnez les symptomes (separes par espace) :")
for numero, nom in symptomes.items():
    print(numero, "-", nom)

choix = input("Votre choix : ").split()

faits = []
for c in choix:
    if c in symptomes:
        faits.append(symptomes[c])

print("Faits initiaux :", faits)

nouveau = True
while nouveau:
    nouveau = False
    for conditions, conclusion in regles:
        if all(c in faits for c in conditions):
            if conclusion not in faits:
                faits.append(conclusion)
                print("Nouveau fait ajoute :", conclusion)
                nouveau = True

print("---------------------------")
print("Diagnostic final :")
if "panne_materielle" in faits:
    print("=> Panne materielle detectee")
else:
    print("=> Cause non determinee")
print("Base finale :", faits)
