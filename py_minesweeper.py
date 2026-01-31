import random

test_grid = [
    [' ', '*', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' '],
]


def bomb_checker(grid: list, line: int, column: int) -> bool:
    """Renvoie True ou False si la case indiqué par la ligne(line) et la colonne(column) contient une bombe ou non"""
    check = False
    if grid[line][column] == '*':
        check = True
    return check

#revoie True si il y a une bombe à cette case là
assert bomb_checker(test_grid, 0, 1) == True , 'Ton code ne marche pas bien'
#revoie False si il y a une bombe à cette case là           
assert bomb_checker(test_grid, 1, 1) == False , 'Ton code ne marche pas bien'

test_check_win = [['*' for i in range(5)] for i in range(5)]
test_check_win2 = [[' ' for i in range(5)] for i in range(5)]

def check_win_game(grid: list) -> bool: 
    """Verifie s'il reste des cases vides dans la grille afin de savoir si le joueur à gagner"""
    fin_de_partie = True
    for i in grid:
        for j in i:
            if j == ' ':
                fin_de_partie=False 
    return fin_de_partie

#affiche True si toute les espaces ont été révélé  
assert check_win_game(test_check_win) == True , 'ça marche pas alors'
#affiche False si une espace
assert check_win_game(test_check_win2) == False , 'ça marche pas alors'


def random_bomb(nbomb: int) -> list:
    """Place un nombre de bombe choisit dans une grille vide, chaque bombe a des coordonnées au hasard"""
    grid = [[' ' for i in range(5)] for i in range(5)]
    for i in range (nbomb):
        column = random.randint(0,4)
        line = random.randint(0,4)
        while grid[line][column] != ' ':
            column = random.randint(0,4)
            line = random.randint(0,4)
        grid[line][column] = '*'
    return grid

# random_bomb renvoie bien une grille avec des bombes posées aléatoirement en fonction du nombre de bombe demandé

def bomb_around(game: list, line: int, column: int) -> str:
    """Renvoie le nombre de bombes autour d'une case donnée par le numéro de ligne et de colonne dans une grille"""
    nb_bomb = 0
    for i in range(-1,2):
        for j in range(-1,2):
            l = line+i
            c = column+j
            if c >=0 and l >=0  and l<len(game) and c<len(game[l]) and game[l][c] == '*':
                nb_bomb +=1
    return str(nb_bomb)

assert bomb_around(test_grid, 3, 2) == str(0), "La fonction ne renvoie pas le nombre de bombes autour de la case en 3, 2"
assert bomb_around(test_grid, 1, 1) == str(2), "La fonction ne renvoie pas le nombre de bombes autour de la case en 1, 1"

def positionne_request(game: list) -> tuple:
    """Demande à l'utilisateur un numéro de ligne et de colonne en fonction de la case qu'il choisit. Et renvoit la ligne et la colonne.
    """
    max_line = len(game)-1
    max_column = len(game[0])-1
    line = input("quelle ligne veux-tu prendre? : ")
    line = int(line)
    while type(line)!=int or line>max_line or line<0:
        print("le nombre maximale de line est ",max_line)
        line = int((input("quelle ligne veux-tu prendre? : ")))
    column = (input("quelle colonne veux-tu prendre? : "))
    column = int(column)
    while type(column)!=int or column>max_column or column<0:
        print("le nombre maximale de colonne est ",max_column)
        column = int(input("quelle colone veux-tu prendre? : "))
        
    return(line,column)

# Cette fonction demande bien les coordonnées du joueur par rapport a la grille

grille_bool = [[True for i in range(5)] for i in range(5)]

def open_case(game: list, line: int, column: int) -> None:
    """Modifie la grille pour y faire appaitre les indicateurs de bombes et révéler les cases"""
    game[line][column] = bomb_around(game, line, column)
    if game[line][column] == str(0):
        for i in range(-1,2):
            for j in range(-1,2):
                l = line+i
                c = column+j
                if c >=0 and l >=0  and l<len(game) and c<len(game[l]) and game[l][c] == ' ':
                    if grille_bool[l][c]:
                        grille_bool[l][c] = False
                        open_case(game, l, c)
                    else:
                        grille_bool[l][c] = False
    return None

# La fonction modifie correctement la grille en fonction des coordonnées demandées en ajoutant les indicateurs

grid_test = [ 
    [' ', ' ', ' ', ' ', ' '],
    [' ', '1', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]
    

grid_vide = [ 
    [' ', ' ', ' ', ' ', ' '],
    [' ', '1', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

def hide_bomb(game: list) -> list:
    """Renvoie la grille de comparaison mais sans les bombe afin de l'afficher avec show_grid"""
    no_bomb_grid = [ [game[indice_ligne][indice_column] for indice_column in range(len(game[indice_ligne]))] for indice_ligne in range(len(game)) ]
    for x in range(len(no_bomb_grid)):
        for y in range(len(no_bomb_grid[x])):
            if no_bomb_grid[x][y] == '*':
                no_bomb_grid[x][y] = ' '
    return no_bomb_grid

assert hide_bomb(grid_test)== grid_vide, "Ca marche pas"

def show_grid(grid: list) -> str:
    """affiche une grille avec un tableau, des coordonees, qui separent chacunes des valeurs de grid"""
    grille_2 = ''
    print("   0 1 2 3 4")
    for i in range(5):
        grille = str(i) + " |" + grid[i][0] + "|"+ grid[i][1] + "|"+ grid[i][2]+ "|"+ grid[i][3]+ "|"+ grid[i][4]+ "|"
        grille_2 = grille_2 + grille + "\n"
    return grille_2

# La fonction renvoie correctement la grille demandée dans le paramètre grid avec les coordonnées placées aux bon endroit


main_grid = random_bomb(4)
perdu = False

while check_win_game(main_grid) == False and not perdu:
    no_bomb_grid = hide_bomb(main_grid)
    print(show_grid(no_bomb_grid))
    coord_player = positionne_request(main_grid)
    if bomb_checker(main_grid, coord_player[0], coord_player[1]):
        perdu = True
        print("Perdu !")
        print(show_grid(main_grid))
    else:
        open_case(main_grid, coord_player[0], coord_player[1])
        if check_win_game(main_grid):
            print("Gagné !")
            print(show_grid(main_grid))
