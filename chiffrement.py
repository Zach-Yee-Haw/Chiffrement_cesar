import unicodedata

def strip_accent(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def Chiffrage_Cesar():


    """
    Cette fonction permet à l'utilisateur de prendre un message dans le fichier message_code.txt et de l'encrypter/décrypter
    par le chiffrement de César.
    """


    #initialisation de variables

    nombre_lettres_alphabet = 26
    message_base = open("message_code.txt", "r", encoding='utf-8')
    message_base = message_base.read()
    case_haute = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    case_basse = case_haute.lower()

    message_base_liste = []
    case_haute_liste = []
    case_basse_liste = []

    message_base_liste[:] = strip_accent(message_base)
    case_haute_liste[:] = case_haute
    case_basse_liste[:] = case_basse

    while True:

        message_code_liste = []

        #Entrée par l'utilisateur

        commande = input("Entrez un chiffre afin de encrypter/décrypter le message, ou entrez \'d\' pour tenter de décoder le message : ")

        #Si sa commande est un int ou 'd', on continue sinon c'est pas bien

        try:
            commande = int(commande)
        except ValueError:
            if commande != 'd': print("Commande invalide, essayez à nouveau.")

        #On vérifie l'entrée de l'utilisateur, si c'est un 'd', on décode et si c'est un chiffre, on encrypte/décrypte

        if commande == "d":
            #
            print("test")
            #
        elif isinstance(commande, int):

            """
            On vérifie la position de la lettre dans l'alphabet, puis on lui ajoute la valeur de l'utilisateur.
            On divise ensuite ce nombre par 26 et on prend le restant afin que ce chiffre corresponde à une lettre
            dans l'alphabet. On ajoute cette lettre dans la liste du message codé. Si le charactère n'est pas une 
            lettre, on l'ajoute directement dans la liste.
            """

            i = 0

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

            #On unifie le message codé/décodé

            message_code = ''.join(message_code_liste)

            #On montre le message à l'utilisateur

            print("Voici le message : ", message_code)

        if input("Tapez \'r\' pour recommencer, ou autre chose pour terminer : ") != 'r': break

Chiffrage_Cesar()