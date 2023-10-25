import time 
import random

vstupni_dvere = random.randint(1,2)

uplynuly_cas = 0

seznam_utoku = ["kopnutí","hlavička","pěst"]

spinac = True

pocet_zivotu_hrac = 10
pocet_zivotu_npc = 10
 
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
                time.sleep(1)
                spinac = False
                break
        
            elif uplynuly_cas > 10:
                print("Byl jsi moc pomalý, zkus to znovu")
                break
            elif odpoved != "zmiz":
                print("špatně, zkus to znovu")
                time.sleep(3)
                break
    print("Nyní se můžeš porozhlédnout po místnosti")
    while True:
        odpoved = str(input("Chceš se vydat vpravo nebo vlevo? (pravá/levá): "))
        if odpoved == "pravá":
            print("Našel jsi dveře, ale vypadá to, že k nim potřebuješ 8 místný kód, zkus se ještě porozhlédnout")
            continue
        elif odpoved == "levá":
            time.sleep(1)
            print("Našel jsi zápisky hospodského, odhal který je falešný a datum tohoto textu ti poslouží jako kód k otevření dveří")
            time.sleep(6)
            while True:
                print(
                    """
                    Hospoda - zápisky 2023 (TAJNÉ)
                    [1]	Pondělí 21.8. 2023
                        Tržby: 50 000,-
                        Počet lidí: 150

                    [2]	Úterý 22.8. 2023
                        Tržby: 30 000,-
                        Počet lidí: 78

                    [3]	Středa 23.8. 2023
                        Tržby: 48 900,-
                        Počet lidí: 35

                    [4]	Čtvrtek 24.8. 2023
                        Tržby: 78 000,-
                        Počet lidí: 40

                    [5]	Pátek 25.8. 2023
                        Tržby: 120 000,-
                        Počet lidí: 380

                    [6]	Sobota 26.8. 2023
                        Tržby: 400 000,-
                        Počet lidí: 10

                    [7]	Neděle 27.8. 2023
                        Tržby: -
                        Počet lidí: -


                    """
                    )
                time.sleep(3)
                odpoved = str(input("Tak co, který ze zápisků je falešný? (1/2/3/4/5/6/7) nebo snad potřebuješ nápovědu? (h) "))
                if odpoved == "h":
                    print("No tak dobře, tady máš otevírací dobu:")
                    time.sleep(3)
                    print("""
                        
                        PONDĚLÍ: 16:00 - 22:00
                        ÚTERÝ: 16:00 - 22:00
                        STŘEDA: 16:00 - 22:00
                        ČTVRTEK: 16:00 - 24:00
                        PÁTEK: 16:00 - 24:00
                        SOBOTA: ZAVŘENO
                        NEDĚLE: ZAVŘENO

                            """
                        )
                    continue
                elif odpoved != "6":
                    print("špatně, zkus to znovu")
                    time.sleep(3)
                    continue
                elif odpoved == "6":
                    while True:
                        odpoved = int((input("Správně, došel jsi k zamčeným dveřím a nyní už jen stačí zadat kód (ddmmyyyy) ")))
                        if str(odpoved) == "26082023":
                            break
                        break
                    break
                break
            break
        else:
            print("špatně, zkus to znovu")
            continue
    print("dveře se pomalu otevřely a ty vcházíš dovnitř")
    time.sleep(2)
    print("Najednou se rozsvítí světla a ty uvidíš siluetu člověka")
    time.sleep(1)
    print("Vždyť to je uklízečka Irena a ty jsi jí právě stoupl na vytřenou podlahu")
    print("Tohle se neobejde bez boje...")
    time.sleep(2)
    print("Na začátek máte oba 10 životů, zabij protivníka a dostaň se na svobodu!")
    while True:
        if pocet_zivotu_npc <= 0:
            print("Irena je dole")
            break
        elif pocet_zivotu_hrac <= 0:
            print("Jsi kaput, zkus to znovu")
            pocet_zivotu_hrac = 10
            pocet_zivotu_npc = 10

        print("Vyber, jakým způsobem zaútočíš: ")
        print("""
               [1] kopnutí
               [2] hlavička
               [3] pěst
            """)
        uder_hrac = int(input("Zadej 1,2 nebo 3 pro výběr útoku: "))
        if uder_hrac == 1:
            pocet_zivotu_npc -= 3
            if pocet_zivotu_npc <= 0:
                continue
            else:
                print(f"Kopnul si Irenu a zbývá ji {pocet_zivotu_npc} životů")
        elif uder_hrac == 2:
            pocet_zivotu_npc -= 5
            if pocet_zivotu_npc <= 0:
                continue
            else:
                print(f"Dal si Ireně hlavičku a zbývá ji {pocet_zivotu_npc} životů")
        elif uder_hrac == 3:    
            pocet_zivotu_npc -= 1
            if pocet_zivotu_npc <= 0:
                continue
            else:
                print(f"Irena dostala pěstí a zbývá ji {pocet_zivotu_npc} životů")

        uder_npc = random.choice(seznam_utoku)
        if uder_npc == "kopnutí":
            pocet_zivotu_hrac -= 3
            if pocet_zivotu_hrac <= 0:
                continue
            else:
                print(f"Irena opětovala útok kopnutím a zbývá ti {pocet_zivotu_hrac} životů")
        elif uder_npc == "hlavička":
            pocet_zivotu_hrac -= 5
            if pocet_zivotu_hrac <= 0:
                continue
            else:
                print(f"Dostal si hlavičku, ale neboj máš ještě {pocet_zivotu_hrac} životů")
        elif uder_npc == "pěst":
            pocet_zivotu_hrac -= 1
            if pocet_zivotu_hrac <= 0:
                continue
            else:   
                print(f"Irena ti dala pěstí, ještě máš {pocet_zivotu_hrac} životů")
    time.sleep(3)
    print("Najednou sis všiml pootevřených dveří, které za ní byly celou dobu a zjistil si, že vedou ven")
    print("Tak hurá na svobodu")
    time.sleep(2)
    print("KONEC")
    exit()
        

               

                
        
            


                




