import string
import random
import re
import os
import platform

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
                
    saut_de_ligne()
    
    new = str(input("Generer un nouveau MDP [A] : "))

    if new == "A":
        genMDP()
    else :
        close()

genMDP()