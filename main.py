import random

tailleGrille = 10
nbIndividus = 10


def main():
    lesReines = [list(range(tailleGrille))] * nbIndividus
    for i in range(nbIndividus):
        random.shuffle(lesReines[i])
    printPositions(lesReines[0])
    print(lesReines[0])
    print(fitness(lesReines[0]))


def fitness(tableau):
    score = 0
    for i in range(tailleGrille):
        if estPrise(tableau, i, tableau[i]):
            score = score + 1
    return score


def estPrise(tableau, ligne, col):
    for i in range(tailleGrille):
        if i >= ligne:
            break
        if tableau.__len__() > i and (col == tableau[i] or tableau[i] == col - (ligne - i) or tableau[i] == col + (ligne + i)):
            return True
    return False


def estLibre(ligne, col, lesReines):
    res = True
    if lesReines[ligne] == col:
        res = False
    if col == (lesReines[ligne] - (lesReines.__len__() - ligne)) or col == (
            lesReines[ligne] + (lesReines.__len__() - ligne)):
        res = False
    return res


def printPositions(lesReines):
    grille = [[0] * tailleGrille for _ in range(tailleGrille)]
    output = ""
    it = 0
    for i in lesReines:
        grille[it][i] = 1
        it = it + 1

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if grille[i][j] == 1:
                output = output + " 👸 "
            else:
                output = output + " _ "
        output = output + "\n"
    print(output)


if __name__ == '__main__':
    main()
