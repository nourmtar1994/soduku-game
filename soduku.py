# jeu sudoku simple 
# projet pour le cour

import random

# fonction pour faire grille vide
def creer_grille():
    grille = []
    for i in range(9):
        lg = []
        for j in range(9):
            lg.append(0)
        grille.append(lg)
    return grille

# fonction pr afficher grille
def affich_grille(grl):
    print("\n")
    print("    0 1 2   3 4 5   6 7 8")
    print("  -------------------------")
    for i in range(9):
        # ligne horizontale tous les 3 lignes
        if i % 3 == 0 and i != 0:
            print("  -------------------------")
        
        lg = str(i) + " | "  # commencer ligne
        for j in range(9):
            # barre verticale tous les 3 colonnes
            if j % 3 == 0 and j != 0:
                lg = lg + "| "
            
            # si case vide mettre point
            if grl[i][j] == 0:
                lg = lg + ". "
            else:
                lg = lg + str(grl[i][j]) + " "
        
        lg = lg + "|"
        print(lg)
    print("  -------------------------")
    print("\n")

# fonction pour verifer si num est bon
def verif_num(grl, lg, col, num):
    # check ligne
    for i in range(9):
        if grl[lg][i] == num:
            return False
    
    # check colonne
    for i in range(9):
        if grl[i][col] == num:
            return False
    
    # check carre 3x3
    deb_lg = (lg // 3) * 3
    deb_col = (col // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if grl[deb_lg + i][deb_col + j] == num:
                return False
    
    return True

# fonction pour resoudre sudoku
def resoud_sudoku(grl):
    # chercher case vide
    for i in range(9):
        for j in range(9):
            if grl[i][j] == 0:
                # essayer tous les numeros
                for num in range(1, 10):
                    if verif_num(grl, i, j, num):
                        grl[i][j] = num
                        
                        if resoud_sudoku(grl):
                            return True
                        
                        grl[i][j] = 0
                
                return False
    
    return True

# fonction pr generer puzzle
def gener_puzzle():
    grl = creer_grille()
    
    # mettre quelque numeros random au debut
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(15):
        lg = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.choice(nums)
        
        # verifer avant de mettre
        if grl[lg][col] == 0 and verif_num(grl, lg, col, num):
            grl[lg][col] = num
    
    # resoudre grille complete
    resoud_sudoku(grl)
    
    # enlever des numeros pour fair puzzle
    nb_enlev = 45  # nombre de case a enlever
    
    enlev = 0
    while enlev < nb_enlev:
        lg = random.randint(0, 8)
        col = random.randint(0, 8)
        
        # si case pas vide on enleve
        if grl[lg][col] != 0:
            grl[lg][col] = 0
            enlev = enlev + 1
    
    return grl

# fonction principal
def demarrer_jeu():
    print("=" * 40)
    print("  BIENVENU AU JEU SUDOKU")
    print("=" * 40)
    
    # generer puzzle
    print("\nGeneration du puzzle...")
    grl = gener_puzzle()
    grl_orig = [lg[:] for lg in grl]  # copie de la grille original
    
    # boucle principal du jeu
    while True:
        affich_grille(grl)
        
        print("Commandes:")
        print("  - Entrez ligne, colone, numero (exemple: 0 0 5)")
        print("  - Tapez 'resoudre' pour voir solution")
        print("  - Tapez 'quitter' pour sortir")
        
        inp = input("\nVotre coup: ")
        
        # si joueur veut quitter
        if inp.lower() == "quitter":
            print("Merci d'avoir jouer!")
            break
        
        # si joueur veut solution
        if inp.lower() == "resoudre":
            print("\nResolution du puzzle...")
            resoud_sudoku(grl)
            affich_grille(grl)
            print("Puzzle resolu!")
            break
        
        # lire input joueur
        try:
            parts = inp.split()
            lg = int(parts[0])
            col = int(parts[1])
            num = int(parts[2])
            
            # verifier position valide
            if lg < 0 or lg > 8 or col < 0 or col > 8:
                print("Erreur: ligne et colone doit etre entre 0 et 8")
                continue
            
            if num < 1 or num > 9:
                print("Erreur: numero doit etre entre 1 et 9")
                continue
            
            # verifier si case pas deja rempli
            if grl_orig[lg][col] != 0:
                print("Erreur: peut pas changer les numero originaux!")
                continue
            
            # verifier si numero est valide
            if verif_num(grl, lg, col, num):
                grl[lg][col] = num
                print("Bon coup!")
                
                # check si puzzle fini
                fini = True
                for i in range(9):
                    for j in range(9):
                        if grl[i][j] == 0:
                            fini = False
                            break
                
                # si puzzle completer
                if fini:
                    affich_grille(grl)
                    print("Felicitation! Vous avez resolu le puzzle!")
                    break
            else:
                print("Coup pas valide! Ce numero va pas la.")
        
        except:
            print("Entrer invalide! Utilisez format: ligne colone numero")

# demarrer le jeu
if __name__ == "__main__":
    demarrer_jeu()
