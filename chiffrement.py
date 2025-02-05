import unicodedata


case_haute = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
case_basse = case_haute.lower()

def strip_accent(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def Premiers_Mots(texte, nombre_de_mots, longueur_min = 3):
    """
    Cette fonction sert à prendre une phrase en entrée et sort les premiers mots de cette phrase selon
    le nombre de mots que l'utilisateur voudrait avoir.
    """

    #On enlève les accents et on met tout en case basse

    texte_simplifie = strip_accent(texte)
    texte_simplifie = texte_simplifie.lower()

    #On génère des listes de lettres

    texte_liste = []
    texte_simplifie_liste = []
    texte_liste[:] = texte_simplifie

    #Si le charactère est une lettre ou une espace, on la conserve, sinon, on le transforme en espace

    for i in range(len(texte_liste)):

        if texte_liste[i] in case_basse or texte_liste[i] == ' ':

            texte_simplifie_liste.append(texte_liste[i])
        else:
            texte_simplifie_liste.append(' ')

    #on met tous les mots ensemble, puis on les sépare à l'aide des espaces

    mots = ''.join(texte_simplifie_liste)
    premiers_mots = []
    mots = mots.split(' ')

    #On enlève les mots qui sont trop court

    mots_a_enlever = []
    for mot in mots:
        if len(mot) < longueur_min: mots_a_enlever.append(mot)

    for mot in mots_a_enlever:
        mots.remove(mot)

    #On retourne les premiers mots et, s'il y en a moins que ce que l'utilisateur veux, on retourne le tout

    if len(mots) <= nombre_de_mots:
        premiers_mots = mots

    else:
        premiers_mots = mots[0:nombre_de_mots]

    return premiers_mots

def Chiffrage_Cesar(commande,message_base):


    """
    Cette fonction permet à l'utilisateur de prendre un message dans le fichier message_code.txt et de
    l'encrypter/décrypter par le chiffrement de César.
    """


    #initialisation de variables

    nombre_lettres_alphabet = 26
    message_base_liste = []
    case_haute_liste = []
    case_basse_liste = []

    message_base_liste[:] = strip_accent(message_base)
    case_haute_liste[:] = case_haute
    case_basse_liste[:] = case_basse

    message_code_liste = []

    #Si sa commande est un int ou 'd', on continue sinon c'est pas bien

    try:
        commande = int(commande)
    except ValueError:
        print("Commande invalide, essayez à nouveau.")

    #On vérifie l'entrée de l'utilisateur et si c'est un chiffre, on encrypte/décrypte

    if isinstance(commande, int):

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

        return message_code

def EstFrancais(texte):
    e_count = 0
    for i in range(len(texte)):
        if texte[i] == 'e':
            e_count += 1
    if e_count/len(texte) >= 0.1 :
        return 1
    return 0

def Decryptage(texte):
    for i in range(26):
        Message_Decrypter = Chiffrage_Cesar(i,texte)
        if(EstFrancais(Message_Decrypter)):
            return Message_Decrypter, 26-i
    return 0


def menu():
    """
        Un simple menu pour intéragir avec l'utilisateur,
        On demande s'il veut encrypter ou decrypter,
        par la suite, s'il veut écrire son propre texte ou utiliser un fichier texte
        Enfin, on appelle les fonctions du code qui réponde à la demande.
        """
    if input('Voulez-vous encrypter (1) ou decrypter (0) un texte ?') == 1:
        texte = input('Veuillez entrer un texte ou un fichier texte terminant par .txt\n')
        if texte.endswith(".txt"):
            file = open(texte, 'r', encoding = 'utf-8')
            texte = file.readlines()
            texte = ''.join(texte)
        commande = input('Entrez un nombre pour encrypter le message : ')
        message_code = Chiffrage_Cesar(commande,texte)
        print(message_code)
    else:
        texte = input('Veuillez entrer un texte ou un fichier texte terminant par .txt')
        if texte.endswith(".txt"):
            file = open(texte, 'r', encoding='utf-8')
            texte = file.readlines()
            texte = ''.join(texte)
    message, clef = Decryptage(texte)
    print(f"La clé de chiffrement est: {clef}\n")
    print(message)


menu()


