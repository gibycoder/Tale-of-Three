import random

class Hero(object):

    def __init__(self, money, power, hp, iq, clvl, plvl, inv):
        self.money = money
        # self.money - kasa bohatera
        self.power = power
        # self.power - siła bohatera
        self.hp = hp
        # self.hp - zdrowie bohatera
        self.iq = iq
        # self.iq - intelect bohatera
        self.inv = inv
        # self.inv - rzeczy bohatera
        self.clvl = clvl
        # self.clvl - poziom bohatera
        self.plvl = plvl
        # self.plvl - punkty pozioma bohatera


    def bp(self):
        print("\n")
        print("^"*118)
        print()

        ansBP = input("Czy chcesz przeglądać swój plecak i cechy?(1 (Tak) / 2(Nie)): ")
        # ansBP - odpowiedz z powodu plecaka bohatera
        
        print()

        if ansBP == "1":
            print("Cechy:")
            print()
            print("   Masz %d srebra." % self.money)
            print("   Masz %d siły." % self.power)
            print("   Masz %d zdrowia." % self.hp)
            print("   Masz %d iq." % self.iq)
            print("   U cibie jest %d poziom bohatera." % self.clvl)
            print("   Teraz masz %d/20 punktów." % self.plvl)
            print()

            if self.inv == "":
                return "   Jeszcze nic nie masz w plecaku."

            else:
                print ("Masz w plecaku:")
                return "   %s" % self.inv
        else:
            return "Ok, lieczimy dalej."

        print()
        print("v"*118)


h = Hero(5, 5, 30, 8, 0, 0, "")

class MonsterZom(object):

    def __init__(self, hp, money, power, plvl):
        self.hp = hp
        # self.hp - zdrowie monstra
        self.money = money
        # self.money - kasa monstra
        self.power = power
        # self.power - siła monstra
        self.plvl = plvl
        # self.plvl - punkty pozioma monstra

    def zom(self):
        item = int(random.randint(1,7))
        # item - random z powodu jaki przedmiot bohater dostanie od

        print("\n")
        print("^"*118)
        print()

        ansM = int(input("Jesteś przed monstrem, chcesz się z nim bić? (1 (Tak)/ 2(Nie)): "))
        # ansM - odpowiedz czy chce bohater biś się z monstrem

        print()

        if ansM == 1:
            
            print("Zaczyna się walka. Monster ma %d życia. " % self.hp)
            print()

            while self.hp > 0:
                print("    Monster uderzył ciebie na %d życia." % self.power)
                h.hp -= 2
                print("    Masz %d życia." % h.hp)
                
                print("    Uderzyłeś monstra na %d życia." % h.power )
                self.hp -= h.power

                print("    Monster ma %d życia." % self.hp)

                if h.hp > 0:
                    print("    Na razie żyjesz.")
                else:
                    return "Przegrałeś."

            h.plvl += self.plvl
            h.money += self.money

            if item == 1:
                h.inv = "Miecz Kyrielieson"

                print()
                print(sword_Kyr(5))
                return "Zabiłeś monstra, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            elif item == 3:
                h.inv = "Tarcza Iferusa"

                print()
                print(shield_If(4))
                return "Zabiłeś monstra, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)
            
            elif item == 5:
                h.inv = "Kaska Gribanello"

                print()
                print(helmet_Grib(3))
                return "Zabiłeś monstra, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            elif item == 6:
                h.inv = "Pancerz Bluda"

                print()
                print(armor_Blu(6))
                return "Zabiłeś monstra, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            else:
                h.inv = ""

                print()
                return "Zabiłeś monstra, masz +%d punktów, +%d srebra." % (self.plvl, self.money)
                return"W końcu masz %d/20 punktów pozioma bohatera, %d kasy." % (h.plvl, h.money)

        else:
            return "No dobra, jak chcesz idziemy dalej."


m = MonsterZom(5, 3, 2, 4)

class MonsterSkel(object):

    def __init__(self, hp, money, power, plvl):
        self.hp = hp
        # self.hp - zdrowie monstra
        self.money = money
        # self.money - kasa monstra
        self.power = power
        # self.power - siła monstra
        self.plvl = plvl
        # self.plvl - punkty pozioma monstra

    def skel(self):
        item = int(random.randint(1,7))
        # item - random z powodu jaki przedmiot bohater dostanie od

        print("\n")
        print("^"*118)
        print()

        ansM = int(input("Jesteś przed śkilietem, chcesz się z nim bić? (1 (Tak)/ 2(Nie)): "))
        # ansM - odpowiedz czy chce bohater biś się z monstrem

        print()

        if ansM == 1:
            
            print("Zaczyna się walka. Śkielet ma %d życia. " % self.hp)
            print()

            while self.hp > 0:
                print()
                print("    Śkielet uderzył ciebie na %d życia." % self.power)
                h.hp -= 2
                print("    Masz %d życia." % h.hp)
                
                print("    Uderzyłeś śkieleta na %d życia." % h.power )
                self.hp -= h.power

                print("    Śkielet ma %d życia." % self.hp)

                if h.hp > 0:
                    print("    Na razie żyjesz.")
                else:
                    return "Przegrałeś."

            h.plvl += self.plvl
            h.money += self.money

            if item == 1:
                h.inv = "Miecz Kyrielieson"

                print()
                print(sword_Kyr(5))
                return "Zabiłeś śkieleta, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            elif item == 3:
                h.inv = "Tarcza Iferusa"

                print()
                print(shield_If(4))
                return "Zabiłeś śkieleta, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)
            
            elif item == 5:
                h.inv = "Kaska Gribanello"

                print()
                print(helmet_Grib(3))
                return "Zabiłeś śkieleta, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            elif item == 6:
                h.inv = "Pancerz Bluda"

                print()
                print(armor_Blu(6))
                return "Zabiłeś śkieleta, masz +%d punktów, +%d srebra i zdobyłeś %s." % (self.plvl, self.money, h.inv)
                return "W końcu masz %d/20 punktów pozioma bohatera, %d kasy i %s." % (h.plvl, h.money, h.inv)

            else:
                h.inv = ""

                print()
                return "Zabiłeś śkieleta, masz +%d punktów, +%d srebra." % (self.plvl, self.money)
                return"W końcu masz %d/20 punktów pozioma bohatera, %d kasy." % (h.plvl, h.money)

        else:
            return "No dobra, jak chcesz idziemy dalej."

s = MonsterSkel(9, 4, 3, 5)
    


def sword_Kyr(price):
    h.power += 2

    return """Cechy miecza Kyrieliesona:

        1. Siła + 2, czyli masz %d siły.
        2. Jego cena w sklepie %d srebra.
        """ % (h.power, price)

def shield_If(price):
    h.hp += 3
    h.power += 1

    return """Cechy tarczy Iferusa:

        1. Życie + 3, czyli masz %d zdrowia.
        2. Siła + 1, czyli masz %d siły.
        3. Jego cena w sklepie %d srebra.
        """ % (h.hp, h.power, price)

def helmet_Grib(price):
    h.hp += 2

    return """Cechy kaski Gribanello:

        1. Życie + 2, czyli masz %d zdrowia.
        2. Jego cena w sklepie %d srebra.
        """ % (h.hp, price)

def armor_Blu(price):
    h.hp += 4

    return """Cechy pancerza Bluda:

        1. Życie + 4, czyli masz %d zdrowia.
        2. Jego cena w sklepie %d srebra.
        """ % (h.hp, price)



print("""

             _____             _     _       _   _____ _____            ____             _       _ _       
            |  __ \           | |   (_)     | | |_   _|_   _|          |  _ \           | |     | | |      
	    | |__) |___ ______| |_____  __ _| |   | |   | |    ______  | |_) | __ _ _ __| |_ ___| | | ___  
	    |  _  // _ \_  / _` |_  / |/ _` | |   | |   | |   |______| |  _ < / _` | '__| __/ _ \ | |/ _ \ 
	    | | \ \ (_) / / (_| |/ /| | (_| | |  _| |_ _| |_           | |_) | (_| | |  | ||  __/ | | (_) |
	    |_|  \_\___/___\__,_/___|_|\__,_|_| |_____|_____|          |____/ \__,_|_|   \__\___|_|_|\___/ 

	""")

print("\n")

print("^"*118)
print("""

\t\t\t Jesień 1.11.1333 - Włochy, Slowan San Danero. 14:04

""")
print("v"*118)
print("\n")

ansS = int(input("Widziś las i jeziro. Gdzie chcesz pójść? (1(Las) / 2(Jeziro)): "))
#ansS - odpowiedz sartowa

if ansS == 1:
    print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Poszedłeś do lasa, w lasie możesz pójść na lewo czy na prawo?
    Po lewej i po prawej stronie jest wieża.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """)
    
    ansTr = int(input("Gdzie chcesz pójść( 1(Lewo) / 2(Prawo)): "))
    print()

    if ansTr == 1:
        print("""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
    Szdełeś lasem i z drewa wyszedł monster!!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            """)
        print()

        print(m.zom())
        print(h.bp())

        print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
    Szedłeś dalej i zobaczyłeś wieże. Chciałeś wejść, ale jest zamknieta.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            """)
        ansT = int(input("Możesz wejść przez okno, chcesz?( 1(Tak) / 2(Nie)): "))

        if ansT == 1:
            print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Wszedłeś przez okno. Ciebie uwiedział śkielet.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            print(s.skel())
            print(h.bp())
        else:
            print()

    else:
        print()

else:
    print()
