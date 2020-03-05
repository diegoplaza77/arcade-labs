import random
def main():
    millas_recorridas = 0
    sed = 0
    cansancio_camello = 0
    distancia_nativos = -20
    bebidas = 3
    print("Ola k ase vienbenido a Camel!!")
    print("You have stolen a camel to make your way across the great Mobi desert. "
          "\nThe natives want their camel back and are chasing you down! "
          "\nSurvive your desert trek and out run the natives.")
    done = False
    while done == False:
        print("A. Drink from your canteen. "
              "\nB. Ahead moderate speed."
              "\nC. Ahead full speed. "
              "\nD. Stop for the night. "
              "\nE. Status check. "
              "\nQ. Quit.")
        decision = input("¿Cual es tu decision? ")
        if decision.upper() == "Q":
            done = True
            print("Has salido del juego")
        elif decision.upper() == "E":
            print("Millas recorridas: ", millas_recorridas, " millas"
                  "\nBebida en cantina: ", bebidas,
                  "\nDistancia nativos: ", millas_recorridas - distancia_nativos, " millas detrás tuya")
        elif decision.upper() == "D":
            cansancio_camello = 0
            print("El camello esta tope happy")
            distancia_nativos += random.randint(7, 14)
        elif decision.upper() == "C":
            millas_recorridas += random.randint(10, 20)
            print("Has viajado ", millas_recorridas, " millas")
            sed += 1
            cansancio_camello += random.randint(1, 3)
            distancia_nativos += random.randint(7, 14)
        elif decision.upper() == "B":
            millas_recorridas += random.randint(5, 12)
            print("Has viajado ", millas_recorridas, " millas")
            sed += 1
            cansancio_camello += 1
            distancia_nativos += random.randint(7, 14)
        elif decision.upper() == "A":
            if bebidas >= 1:
                bebidas -= 1
                sed = 0
            else:
                print("ERROR")

        if sed > 4:
            print("Tienes sed :)")
        elif sed > 6:
            print("TAS MORIO")
            done = True

        if cansancio_camello > 5:
            print("Tu camello esta cansadete :)")
        elif cansancio_camello > 8:
            print("Se te ha muerto el camello hulio")
            done = True

        if distancia_nativos >= millas_recorridas:
            print("Te han atrapado weeeyyy")
            done = True
        elif millas_recorridas - 15 <= distancia_nativos:
            print("Los nativos se acercan webon")
        elif millas_recorridas >= 200:
            print("GANASTE, disfruta de tu camello")
            done = True

main()