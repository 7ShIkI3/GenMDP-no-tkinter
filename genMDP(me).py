import string
import random
import re
import os
import platform
import getpass

def get_os():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "Mac"
    elif system == "Linux":
        return "Linux"
    else:
        return "Système d'exploitation inconnu"

# Utilisation de la fonction pour obtenir le système d'exploitation
device = get_os()

#fermer la fenetre
def close():
    exit(0)

#affcichage
def saut_de_ligne():
    print()

def bar():
    print("_"*80)

def affichage():
    saut_de_ligne()
    bar()
    saut_de_ligne()

def CheckMdp(mdp: str):
    password = mdp
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "C'est un mot de passe très faible. Changez-le dès que possible."
    elif strength == 2:
        remarks = "C'est un mot de passe faible. Vous devriez envisager d'utiliser un mot de passe plus fort."
    elif strength == 3:
        remarks = "Votre mot de passe est correct, mais il peut être amélioré."
    elif strength == 4:
        remarks = "Votre mot de passe est difficile à deviner, mais vous pourriez le rendre encore plus sécurisé."
    elif strength == 5:
        remarks = "C'est un mot de passe extrêmement fort ! Les hackers n'ont aucune chance de deviner ce mot de passe !"

    print("Votre mot de passe contient : ")
    print(f"{lower_count} lettres minuscules")
    print(f"{upper_count} lettres majuscules")
    print(f"{num_count} chiffres")
    print(f"{wspace_count} espaces")
    print(f"{special_count} caractères spéciaux")
    print(f"Indice de force du mot de passe : {strength / 5}")
    print(f"Remarques : {remarks}")

affichage()
print("Your OS : ",device)

# Fonction pour générer le mot de passe
# Regex qui a pour condition 2 lettres minuscules, 2 lettres majuscules, 2 chiffres et 2 caractères spéciaux
def genMDP():
    regex = r"^(?=.*[a-z]{2})(?=.*[A-Z]{2})(?=.*\d{2})(?=.*[!@#$%^&*()_+\-={}\[\]|\\:;\"'<>,.?/]).{8,}$"

    mot_de_passe_valide = False

    while not mot_de_passe_valide:
        # Générer un mot de passe aléatoire
        longueur = 15  # Longueur du mot de passe
        lettres = string.ascii_letters
        chiffres = string.digits
        caracteres_speciaux = string.punctuation
        code = lettres + chiffres + caracteres_speciaux
        mot_de_passe = ''.join(random.choice(code) for _ in range(longueur))

        if re.match(regex, mot_de_passe):
            affichage()
            print("Mot de passe généré : ", mot_de_passe)
            mot_de_passe_valide = True
            
            site = str(input("Entrez le nom du site : "))
            
            if device == "Windows":
                try:
                    with open("Mdp_Historique\mdp.txt", "a") as f:
                        f.write(f"{site}: {mot_de_passe}\n")
                except:
                    os.mkdir('Mdp_Historique')
                    with open("Mdp_Historique\mdp.txt", "a") as f:
                        f.write(f"{site}: {mot_de_passe}\n")
            elif device == "Linux" or device == "Mac":
                try:
                    with open("Mdp_Historique/mdp.txt", "a") as f:
                        f.write(f"{site}: {mot_de_passe}\n")
                except:
                    os.mkdir('Mdp_Historique')
                    with open("Mdp_Historique/mdp.txt", "a") as f:
                        f.write(f"{site}: {mot_de_passe}\n")
            else:
                print("your device is not compatible")
                break
                
    affichage()
    CheckMdp(mot_de_passe)
    affichage()
    
    new = str(input("Generer un nouveau MDP [A] : "))

    if new == "A":
        genMDP()
    else :
        close()

genMDP()