import random

def selectionSort(lista):
    for i in range(0, len(lista) -1):
        minimum = lista[i]
        swap = -1
        for j in range(i + 1, len(lista)):
            if minimum > lista[j]:
                minimum = lista[j]
                swap = j
        if swap != -1:
            lista[swap] = lista[i]
            lista[i] = minimum

def mergeSort(lista):
    if len(lista) == 1:
        return lista

    middle = len(lista)//2
    left = lista[:middle]
    right = lista[middle:]
    l1 = mergeSort(left)
    l2 = mergeSort(right)
    return merge(l1, l2)


def merge(listaA, listaB):
    listaNueva = []
    while len(listaA) > 0 and len(listaB) > 0:
        if listaA[0] > listaB[0]:
            listaNueva.append(listaB.pop(0))
        else:
            listaNueva.append(listaA.pop(0))

    if len(listaA) > 0:
        listaNueva.extend(listaA)
    elif len(listaB) > 0:
        listaNueva.extend(listaB)
    return listaNueva


def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        for j in range(i - 1, -1, -1):
            if key < lista[j]:
                lista[j + 1] = lista[j]
                lista[j] = key


def radixSort(lista):
    print("Done")


while True:
    n = input("Enter n: ")
    try:
        num = int(n)
        if num > 1:
            numbersList = list(range(1, num + 1))
            random.shuffle(numbersList)
            print(numbersList)
        else:
            print("Ingrese un número mayor que 1!\n")
            continue

    except ValueError:
        print("Input invalido, ingrese un número válido!")
        continue

    s = input("\n1. Selection\n2. Merge\n3. Insertion\n4. Radix\n5. Salir: ")
    sNum = -1
    print("\n")

    try:
        sNum = int(s)
    except ValueError:
        print("Input invalido, ingrese una opción válida!")

    if sNum == 1:
        lista = list(numbersList)
        selectionSort(lista)
        print(lista)
    elif sNum == 2:
        lista = list(numbersList)
        print(mergeSort(lista))
    elif sNum == 3:
        lista = list(numbersList)
        insertionSort(lista)
        print(lista)
    elif sNum == 4:
        lista = list(numbersList)
        radixSort(lista)
    elif sNum == 5:
        break

