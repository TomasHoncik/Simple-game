import time 
import random

vstupni_dvere = random.randint(1,2)

uplynuly_cas = 0

spinac = True
 
while True:

    print("*Probudil ses*")
    print("Ale né, kde to jsem?")
    time.sleep(1)
    print("Tak počkat, já jsem pořád v hospodě?\nAle vždyť je sobota, a o víkendu bývá zavřeno!")
    time.sleep(1)
    print("Tak to opravdu nevím jak se odtud dostanu...")
    time.sleep(3)
    while True:
        odpoved = str(input("Máš na výběr, buďto zkusit jestli hlavní dveře nezůstaly otevřené nebo se podívat do sklepa (sklep/dveře): "))
        if odpoved == "dveře" and vstupni_dvere == 1:
            print("A hele, ono to jde...")
            time.sleep(1)
            print("No nic, radši půjdu domů, než někdo zjistí, že jsem tu byl")
            time.sleep(3)
            print("KONEC")
            exit()
        elif odpoved == "dveře" and vstupni_dvere != 1:
            print("A sakra, dveře jsou zamčené, proto tedy jdeš do sklepa")
            time.sleep(2)
            break
        elif odpoved == "sklep":
            print("Jdeš se tedy podívat do sklepa")
            break
        else:
            print("To je špatná volba")
            continue
    print("Právě si vešel do sklepa, ale je tu tma tak dávej pozor")
    time.sleep(2)
    print("Ale néé na obličej  ti skočila krysa")
    while spinac == True:
        pocatecni_cas = time.time()
        while True:
            odpoved = str(input('Máš 10 vteřin na to napsat "zmiz" nebo tě kousne: '))
            aktualni_cas = time.time()

            uplynuly_cas = aktualni_cas - pocatecni_cas

            if uplynuly_cas <= 10 and odpoved == "zmiz":
                print("Skvěle, krysy si se zbavil")
                spinac = False
                break
            elif uplynuly_cas > 10:
                print("Byl jsi moc pomalý, zkus to znovu")
                break
            elif odpoved != "zmiz":
                print("špatně, zkus to znovu")
                break
    print("")
    while True:
        odpoved = str(input("Chceš se vydat vpravo nebo vlevo?(pravá/levá): "))
        if odpoved == "pravá":
            print("Našel jsi dveře, ale vypadá to, že k nim potřebuješ x místný kód, zkus se ještě porozhlédnout")
            continue
        elif odpoved == "levá":
            while True:
                print("Našel jsi zápisky hospodského, odhal který je falešný a datum tohoto textu ti poslouží jako kód k otevření dveří")
                print(
                    """
                    [1] 17


                    """
                    )
                time.sleep(3)
                odpoved = str(input("Tak co, který ze zápisků je falešný? (1/2/3) nebo snad potřebuješ nápovědu? (h) "))
                if odpoved == "h":
                    print("Správně, vracíš se teď")
                else:
                    print("Taková volba tu není")
                    continue
        
            


                




