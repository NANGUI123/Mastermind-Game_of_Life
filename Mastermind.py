from random import randint
from Param_of_game import LEN_COMBINAISON
from Param_of_game import MAX_ATTEMPTS


def secret_combinaison():
    secret_combinaison = [randint(1, 10) for _ in range(LEN_COMBINAISON)]
    return secret_combinaison


def player_combinaison():
    """Demander à l'utilisateur de saisir une combinaison de 4 chiffres."""
    while True:
        input_player = input("Entrez votre combinaison (4 chiffres séparés par des espaces) : ")
        try:
            combinaison = [int(num) for num in input_player.split()]
            if len(combinaison) == 4 and all(1 <= num <= 10 for num in combinaison):
                if len(combinaison) == len(set(combinaison)):
                    return combinaison
                else:
                    print("Erreur : Il y a des doublons dans la combinaison. Veuillez entrer une combinaison unique.")
            else:
                print("Ce chiffre est déjà dans la combinaison. Veuillez en entrer un autre.")
                print("Erreur : Veuillez entrer une combinaison de 4 chiffres compris entre 1 et 10.")
        except ValueError:
            print("Erreur : Votre saisie ne comporte pas que des nombres. Veuillez entrer exactement 4 nombres compris entre 1 et 10.")


def compare_combinaison(secret_combinaison, attemps_of_player):
    right_place = 0
    wrong_place = 0
    try:
        for index, num in enumerate(attemps_of_player):
            if num == secret_combinaison[index]:
                right_place += 1
            elif num in secret_combinaison:
                wrong_place += 1
            print(f"Indice : {right_place} bien placé(s), {wrong_place} mal placé(s).")
            return right_place, wrong_place
    except ValueError:
        print("Erreur : Votre saisie ne comporte pas que des nombres. Veuillez entrer exactement 4 nombres compris entre 1 et 10.")


def mastermind():
    """Initialisation du jeux"""
    attempts = 0
    """Getion des tours"""
    while attempts < MAX_ATTEMPTS:
        print(f"\nEssai {attempts + 1}/{MAX_ATTEMPTS}")
        player = player_combinaison()
        if player == secret_combinaison:
            print("Félicitations! Vous avez trouvé la combinaison secrète!")
            break
        else:
            print(f"Il vous reste {MAX_ATTEMPTS - (attempts + 1)} essai(s).")
            compare_combinaison(secret_combinaison, player)

        attempts += 1
        if attempts == MAX_ATTEMPTS:
            print("Dommage, vous avez épuisé tous vos essais!")
            print(f"La combinaison secrète était : {secret_combinaison}")


if __name__ == "__main__":
    secret_combinaison = secret_combinaison()
    print(f"\nBienvenue dans le Mastermind!")
    print(f"\nAvez-vous déjà joué à ce jeux? (O/N)")

    answer = input().lower()
    if answer == "n":
        print(f"\nNous allons vous rappeler les règles du jeux.")
        print(f"\nLe jeux du Mastermind est un jeu de réflexion combinatoire")
        print("Vous devez deviner une combinaison de 4 chiffres")
        print("Vous avez 10 essais pour deviner la combinaison secrète")
        print("Après chaque essai, vous recevrez des indices : le nombre de chiffre bien placé, le nombre de chiffre mal placé.")
        print("Vous pouvez quitter le jeu à tout moment")
        print("Très bien, commençons!")

    print("Voullez-vous que nous vous rappelons les règles du jeux? (O/N)")
    answer = input().lower()
    if answer == "o":
        print(f"\nNous allons vous rappeler les règles du jeux.")
        print(f"\nLe jeux du Mastermind est un jeu de réflexion combinatoire")
        print("Vous devez deviner une combinaison de 4 chiffres")
        print("Vous avez 10 essais pour deviner la combinaison secrète")
        print("Après chaque essai, vous recevrez des indices : le nombre de chiffre bien placé, le nombre de chiffre mal placé")
        print("Vous pouvez quitter le jeu à tout moment")
        print(f"\nTrès bien, commençons!")
    else:
        print("Très bien, commençons!")

    while True:
        mastermind()
        print("Voulez-vous rejouer? (O/N)")
        answer = input().strip().lower()

        if answer == "o":
            print("Très bien, commençons une nouvelle partie!")
        elif answer == "n":
            print("Merci d'avoir joué! À bientôt!")
            break
        else:
            print("Réponse invalide. Le jeu va s'arrêter.")
            break
