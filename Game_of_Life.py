import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    La cellule cible est située à (3,3) de la matrice avec bordure.
    Comme dans la matrice avec bordure le contenu de la grille du jeu commence à la ligne 1 et se termine à la ligne m-2, 
    à la colonne 1 et se termine à la colonne n-2. Ce qui veut dire que index_line=1 et index_line=m-2, index_column=1 et index_column=n-2
    cela signifie que index_line-1=0 et index_line + 2 = m, index_column-1=0 et index_column-2=n => la cellule cible est située à (index_line+2, index_column+2) dans la matrice sans bordure.
    """
    neighbors = paded_frame[index_line-1:index_line+2, index_column-1:index_column+2]
    number_neighbors = numpy.sum(neighbors) - paded_frame[index_line, index_column]
    return number_neighbors

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    paded_frame = numpy.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !
    
    next_frame = frame.copy()
    """
    # Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.
    Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)
    #for index_line_strated
    # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)
    
    # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
    On fait appelle à la fonction (compute_number_neighbors)
    
    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
    si il y a des modifications à faire.
    Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
    utilisé ! )"""
    
    return frame

while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)

