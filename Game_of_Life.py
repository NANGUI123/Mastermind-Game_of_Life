import numpy
import itertools
import time


frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    """Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    La cellule cible est située à (3,3) de la matrice avec bordure.
    Comme dans la matrice avec bordure le contenu de la grille du jeu commence à la ligne 1 et se termine à la ligne m-2, 
    à la colonne 1 et se termine à la colonne n-2. Ce qui veut dire que index_line=1 et index_line=m-2, index_column=1 et index_column=n-2
    cela signifie que index_line-1=0 et index_line + 2 = m, index_column-1=0 et index_column-2=n => la cellule cible est située à (index_line+2, index_column+2) dans la matrice sans bordure."""
    neighbors = paded_frame[index_line-1:index_line+2, index_column-1:index_column + 2]
    number_neighbors = numpy.sum(neighbors) - paded_frame[index_line, index_column]
    return number_neighbors


def compute_next_frame(frame):
    """Cette fonction calcule la frame suivante en appliquant les règles du jeu de la vie."""
    paded_frame = numpy.pad(frame, 1, mode="constant")
    next_frame = frame.copy()
    rows, cols = frame.shape

    for index_line, index_column in itertools.product(range(rows), range(cols)):
        number_neighbors = compute_number_neighbors(paded_frame, index_line + 1, index_column + 1)

        """La cellule reste vivante si elle a exactement 2 ou 3 voisines vivantes."""
        if frame[index_line, index_column] == 1:
            next_frame[index_line, index_column] = 1 if 2 <= number_neighbors <= 3 else 0
        else:
            next_frame[index_line, index_column] = 1 if number_neighbors == 3 else 0

    return next_frame




"""Pour les tets j'ai arrêté le jeu après 100 générations"""
MAX_GENERATION = 100
generation = 0
""" Boucle infinie pour afficher les frames successives"""
while generation < MAX_GENERATION:
    print(f"Generation {generation}:\n{frame}")
    new_frame = compute_next_frame(frame)

    frame = new_frame
    generation += 1
    time.sleep(0.5)
"""while True:
    # boucle infinie pour afficher les frames successives (ctrl + c pour arrêter le script)
        print(frame)
        frame = compute_next_frame(frame)
"""
