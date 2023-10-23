import random
import time
import os
#ann bay itilizate posiblite antre kod la pun ks konn taille ak konbyen carre nou bezwen
print("bonjou byenvini nan konsol la jwet sa similaire ak tetris la ou ap gen swiv res posessis la ou ka mete kantite ou vle")
print("--------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------")
kantite = int(input("di nou konbyen carre ou ta vle affiche : "))
dimansion = int(input("kounyea ou pral mete ki dimension ou ta vlel ye: "))

#pou initialisation affichage ak duree a ak pwen
laje = 20
wote = 10
duree= 1/3
pwen=0

# pou ka bay nonb carre foctionnement e jan y ap disperse et pou construction imaj la
for _ in range(kantite):
    x = random.randint(0, laje - dimansion)
    y = random.randint(0, wote - dimansion)


    carre = [["*" for _ in range(dimansion)] for _ in range(dimansion)]

    # la position 
    for i in range(y):
        print()
    for ligne in carre:
        for i in range(x):
            print(" ", end=" ")
        print(" ".join(ligne))
    print()
    #ann mete pwen pou moun nan fe a
    pwen=pwen+100
    time.sleep(duree)
print(" Bravo sa se nouvo pwen ou realize", pwen)
print("Di nou si nou vle kontinyea")
