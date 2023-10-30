import random
import pickle
import os


jwe_ankò = True
while jwe_ankò:
    nom = input("pou komanse jwe asire ou antre non ou: ")
    while not nom.isalpha() or not nom.islower() or '  ' in nom:
        print("non ou pa correspond")
        nom = input("antre yon non en miniscule et sans espace: ")
        print("ok")

    res = 0
    secret = random.randint(0, 100)
    chans = 5
    sko = 0
    print("odinaté gen poul chwazi yo nonb nan inteval [0,100] eseye jwenn li. Ki nonb li ye?")
    while chans > 0:
        chans = chans - 1
        nonb = int(input("ki nonb ou chwazi itilizate: "))
        if nonb < 0 or nonb > 100:
            print("remet yon nonb ki nan intervalle nou di a")
        if nonb > secret:
            print("nonb ou chwazi a pi gwo: ")
        elif nonb < secret:
            print("nonb ou chwazi a pi pitit")
        else:
            break

    if chans != 0:
        print("ou jwenn nonb la", nonb, "sou", 5 - chans, "eme chans ou")
    else:
        print("ou gentan finn itize 5 chans ou yo non lan se te: ", secret)
    res = chans
    sko = chans * 30
    print("men konbyen chans ou te rete se: ", res)
    print("bravo men sko ou a: ", sko)

    # pou nou anrejistrel nan fichier pickle
    resultat = {nom, sko}
    with open("resultat.pickle", "wb") as fichier_pickle:
        pickle.dump(resultat, fichier_pickle)

    response = input("Pou jwe ankò, peze 'f', oswa 'K'ou 'k' pou koupe: ")
    if response != 'f':
        jwe_ankò = False
