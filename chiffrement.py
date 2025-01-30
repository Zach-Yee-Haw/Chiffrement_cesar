
nombre_lettres_alphabet = 26
message_base = open("message_code.txt", "r", encoding='utf-8')
message_base = message_base.read()
case_haute = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
case_basse = case_haute.lower()

message_base_liste = []
case_haute_liste = []
case_basse_liste = []

message_base_liste[:] = message_base
case_haute_liste[:] = case_haute
case_basse_liste[:] = case_basse

while True:

    message_code_liste = []

    commande = input("Entrez un chiffre afin de coder/décoder le message, ou entrez \'d\' pour tenter de décoder le message : ")

    try:
        commande = int(commande)
    except ValueError:
        if commande != 'd': print("Commande invalide, essayez à nouveau.")


    if commande == "d":
        #
        print("test")
        #
    elif isinstance(commande, int):
        #
        i = 0
        #
        for lettre in message_base_liste:

            if lettre in case_haute_liste:

                position_lettre = case_haute.find(lettre)
                position_lettre += commande
                position_lettre %= nombre_lettres_alphabet
                message_code_liste.append(case_haute_liste[position_lettre])

            elif lettre in case_basse_liste:

                position_lettre = case_basse.find(lettre)
                position_lettre += commande
                position_lettre %= nombre_lettres_alphabet
                message_code_liste.append(case_basse_liste[position_lettre])

            else:
                message_code_liste.append(lettre)

            i += 1

        message_code = ''.join(message_code_liste)

        print("Voici le message : ", message_code)

    if input("Tapez \'r\' pour recommencer, ou autre chose pour terminer : ") != 'r': break