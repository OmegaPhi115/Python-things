# Fonctions pour traduction des characteres ( /!\ Très technique /!\ )
# Resumé:
NombreLettre = {
    "Nombre": "Lettre" 
}

LettreNombre = {
    "Lettre": "Nombre en int"
}

def Dictionaire_de_traduction(base):
    """
    Crée un dictionaire de traduction
    :param base: base maximum
    :return: LettreNombre, NombreLettre
    """
    # On crée une liste contenant [nombre en int, charactere correspondant]
    liste_characteres = []

    # On y ajoute les chiffres de 0 a 9
    li = [
        [0, "0"],
        [1, "1"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5"],
        [6, "6"],
        [7, "7"],
        [8, "8"],
        [9, "9"]
    ]
    liste_characteres.extend(li)

    if base > 10:  # Si il faut plus de characteres
    # On ajoute les lettre
        index_ascii = 65 # correspond a "A"
        i = 10
        while index_ascii < (65 + (base - 10)):
            liste_characteres.append([i, chr(index_ascii)])
            i += 1
            index_ascii += 1

    # Finalement on crée les dictionaires
    LN = {"Lettre": "Nombre en int"}
    NL = {"Nombre": "Lettre"}

    for element in liste_characteres:
        NL[element[0]] = element[1]
        LN[element[1]] = int(element[0])

    return LN, NL

# Fonction de convertion (Exercice)

def XtoDEC(nombre, base):
    """
    Convertis un nombre en base X en base 10
    :param nombre: Nombre a convertir
    :param base: base du nombre
    :return: nombre en base 10
    """
    if base != 10:  # Verification que le nombre n'est pas deja convertis
        nombre_convertis = 0
        rang = len(nombre)
        for chararctere in nombre:  # Pour chaque charactere du nombre:
            # traduction du charactere en base 10
            chararctere_traduit = LettreNombre[chararctere]

            # Calcul du de sa valeur:
            valeur_character = chararctere_traduit * (base ** (rang - 1))  # valeur * (base ** rang a partir de 0)

            # On ajoute au total
            nombre_convertis = nombre_convertis + valeur_character

            rang -= 1
        return nombre_convertis
    else:
        return int(nombre)

def DECtoX(nombre, base):
    """
    Convertis Un nombre en base 10 en base X
    :param nombre: Nombre a convertir
    :param base: Base a convertir
    :return: Nombre comvertis
    """
    liste_restes = []
    resultat = nombre
    while resultat > 0:
        # on calcule le reste puis le resultat de la division euvlidienne du resultat par la base
        liste_restes.append(resultat % base)
        resultat = resultat // base

    # On inverse les resultats
    liste_restes.reverse()

    # On traduit les nombre en characters de la base
    nombre_convertis = ""
    for element in liste_restes:
        nombre_convertis += NombreLettre[element]

    return nombre_convertis

# Programe executé
nombre_depart = input("Nombre: ")
base_depart = int(input("Base du nombre: "))
base_finale = int(input("Convertir en base: "))

LettreNombre, NombreLettre = Dictionaire_de_traduction(max([base_depart, base_finale]))

nombre_en_DEC = XtoDEC(nombre_depart, base_depart)

if base_finale == 10:
    resu = nombre_en_DEC
else: # non, alors on convertis
    resu = DECtoX(nombre_en_DEC, base_finale)
    
print(nombre_depart, "en base", base_depart, "donne", resu, "en base", base_finale)

