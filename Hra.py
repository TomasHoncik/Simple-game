import time 
import random


while True:

    vstupni_dvere = random.randint(1,2)
    print(vstupni_dvere)

    print("*Probudil ses*")
    print("Ale né, kde to jsem?")
    time.sleep(1)
    print("Tak počkat, já jsem pořád v hospodě")
    print("Vždyť už je po zavíračce, jak mě tu mohli nechat?!")
    time.sleep(1)
    print("No nic, radši se podívám jestli jsou dveře ještě odemklé")
    time.sleep(1)
    if vstupni_dvere == 1:
        print("Tak jdu hledat dál...")
        print("Chvíli se procházíš po místnost když tu najednou si všimneš, že")

    else:

        print("A hele ono to jde, no nic jdu domů, než někdo zjistí, že jsem tu byl")
        time.sleep(5)
        print("KONEC")
        time.sleep(5)
        break

