import random
import time

tailleGrille = 10
nbIndividus = 10


def main():
    lesReines = [list(range(tailleGrille))] * nbIndividus
    for i in range(nbIndividus):
        item = lesReines[i].copy()
        random.shuffle(lesReines[i])
        lesReines[i] = item

    lesFitness = [None] * nbIndividus
    for i in range(nbIndividus):
        lesFitness[i] = fitness(lesReines[i])
    start_time = time.time()
    print(lesReines)
    print(lesFitness)
    res = run(lesReines, lesFitness)
    printPositions(res)
    stop_time = time.time() - start_time
    print("temps placement moins de place : ", stop_time)


def run(lesReines, lesFitness):
    res = None
    while res == None:
        for i in range(nbIndividus):
            if lesFitness[i] == tailleGrille:
                print(lesFitness)
                print(lesReines[i])
                print(i)
                print(fitness(lesReines[i]))
                printPositions(lesReines[i])
                res = lesReines[i].copy()
        lesReproducteurs = [None] * nbIndividus
        lesViellesReines = lesReines.copy()
        for i in range(nbIndividus):
            lesReproducteurs[i] = random.choices(lesReines, weights=lesFitness, k=2)
            while lesReproducteurs[i][0] == lesReproducteurs[i][1]:
                lesReproducteurs[i] = random.choices(lesReines, weights=lesFitness, k=2)
        for i in range(nbIndividus):
            if random.random() > 0.10:
                lesReines[i] = croiser(lesReproducteurs[i][0], lesReproducteurs[i][1])
            else:
                lesReines[i] = lesViellesReines[min(lesFitness)]
        for i in range(nbIndividus):
            lesFitness[i] = fitness(lesReines[i])
        print(lesFitness)
    return res


def croiser(pere, mere):
    child = pere.copy()
    for i in range(random.randint(0, 3)):
        mereNombre = mere[random.randint(0, tailleGrille - 1)]
        mereIndex = mere.index(mereNombre)
        childIndex = child.index(mereNombre)
        temp = child[mereIndex]
        child[mereIndex] = mereNombre
        child[childIndex] = temp
    return child


def fitness(tableau):
    score = 0
    for i in range(tailleGrille):
        if estPrise(tableau, i, tableau[i]):
            score = score + 1
    return tailleGrille - score


def estPrise(tableau, ligne, col):
    for i in range(tailleGrille):
        if i >= ligne:
            break
        if tableau.__len__() > i and (
                col == tableau[i] or tableau[i] == col - (ligne - i) or tableau[i] == col + (ligne + i)):
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
