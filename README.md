# Jeu de Sudoku - Projet pour la matiére: Dévelopement caté serveur

## Ouvrir le jeu

Il suffit de lancer le fichier python:

```
python sudoku.py
```

## Comment Jouer

1. Un puzzle de sudoku sera genere automatiquement
2. La grille montre des numeros et des points (.) pour les cases vides
3. Les lignes et colonnes sont numerotees de 0 a 8

## Controles

- Pour placer un numero: tapez `ligne colonne numero` (exemple: `0 0 5`)
- Pour voir la solution: tapez `resoudre`
- Pour quitter le jeu: tapez `quitter`

## Exemple

Si vous voulez mettre le numero 7 dans la ligne 3, colonne 4, vous tapez:

```
3 4 7
```

## Regles du Sudoku

- Chaque ligne doit avoir les numeros 1-9 sans repetition
- Chaque colonne doit avoir les numeros 1-9 sans repetition
- Chaque carre 3x3 doit avoir les numeros 1-9 sans repetition

## Notes

- Vous ne pouvez pas changer les numeros originaux qui sont venus avec le puzzle
- Le jeu vous dira si votre coup est invalide
- Quand vous remplissez toutes les cases correctement, vous gagnez!
