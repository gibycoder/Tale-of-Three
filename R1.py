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

print("""

        _________ _______  _        _______    _______  _______   _________          _______  _______  _______ 
        \__   __/(  ___  )( \      (  ____ \  (  ___  )(  ____ \  \__   __/|\     /|(  ____ )(  ____ \(  ____ \

           ) (   | (   ) || (      | (    \/  | (   ) || (    \/     ) (   | )   ( || (    )|| (    \/| (    \/
           | |   | (___) || |      | (__      | |   | || (__         | |   | (___) || (____)|| (__    | (__    
           | |   |  ___  || |      |  __)     | |   | ||  __)        | |   |  ___  ||     __)|  __)   |  __)   
           | |   | (   ) || |      | (        | |   | || (           | |   | (   ) || (\ (   | (      | (      
           | |   | )   ( || (____/\| (____/\  | (___) || )           | |   | )   ( || ) \ \__| (____/\| (____/\
   
           )_(   |/     \|(_______/(_______/  (_______)|/            )_(   |/     \||/   \__/(_______/(_______/
        

    """)

print("#"*118)
print("""
    
    Zasady:

    1. Baw się dobrze.

    2. Masz na początku:

        kasa - 10 ser
        siła - 5
        hp - 30
        iq - 5

    3. Czas od czasu morzesz przeglądać swój plecak i swoje cechy.
    """)

name = input("""
Podaj swoją ksywę i zaczynaj przygodę.
Twoja ksywa: """)
#name - imię



print("\n")
print("\n")

print("^"*118)
print("""

\t\t\t Jesień 31.10.1333 - Włochy, Slowan San Danero. 21:03

""")
print("v"*118)
print("\n")

print("""
                         _____             _     _       _    _____            ____             
                        |  __ \           | |   (_)     | |  |_   _|          |  _ \            
                        | |__) |___ ______| |_____  __ _| |    | |    ______  | |_) | __ _ _ __ 
                        |  _  // _ \_  / _` |_  / |/ _` | |    | |   |______| |  _ < / _` | '__|
                        | | \ \ (_) / / (_| |/ /| | (_| | |   _| |_           | |_) | (_| | |   
                        |_|  \_\___/___\__,_/___|_|\__,_|_|  |_____|          |____/ \__,_|_|   
                                                                       
 
""")
ansS = input("Jestes przed barem. Chcesz wejść? (1 (Tak) / 2 (Nie) ) : ")
#ansS - odpwiedz Start


if ansS == "1":
    
    print("""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Wszdłeś w barze było bardzo głośno, zobaczyłeś pijanego starzca, który chciał piwa za darmo. 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    - Aaaaa, jak to niema piwa, wiedziałem go. Dawaj mi go lub ty wiecej nie bedziesz mógł mieszać swoje napoje!!!!!


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ty podszedłeś do niego i uspokoiłeś go tym, że kupiłeś mu piwa.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\t\t\t\t\t ************************
\t\t\t\t\t
\t\t\t\t\t   Masz 7 srebra i 7 iq
\t\t\t\t\t
\t\t\t\t\t ************************
        """)

    self.money = 7
    self.iq = 7

    ansB = input("Widzisz stoły. Gdzie chcesz pójść? (1 (Starzec) / 2 (Facet) ): ")
    #ansB - odpowiedz Bar 

    if ansB == "1":
        print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Usiadłeś ze starcem

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    - Dziękuje wędrowcu za piwo. Opowiem ci legendę o Piterosu. Głosi ona, iż istnieją ziemie, na których żyją potwory, 
    mogące cię zabić jednym tchem i bohaterzy zdolni do nieludzkich czynów i okrucieństw. 
    Mój dziadek powiedział o 3 książkach, za pomocą których możesz się tam dostać.
    
    - To są bzdury!!

    - Cholera jasna, jak nie wierzysz, to zapytaj innych!!


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Odszedłeś od stołu.

Usiadłeś z facetem.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        print("-"*118)
        input("Naciśnij klawiszę ENTER, aby zacząć rozmowę z facetem.")
        print("-"*118)

        print("""

    - Witaj młody! Ten starzec powiedział, że znasz legendę o Piterosu. 

    - Nic nie wiem, pewnie znowu jest pijany i wymyślił jakąś bzdurę. O czym on ci powiedział?

    - Opowiadał, że istnieją ziemie, zamieskujące przez nieznanych potworów, którzy bez trudu cię zabiją.

    - No dobra, być może coś wiem. Musiałbym odświeżyć pamięć. Myślę, że kubek cydru mi w tym pomoże.

        
\t\t\t\t\t ************************
\t\t\t\t\t
\t\t\t\t\t   Masz 5 srebra i 8 iq
\t\t\t\t\t
\t\t\t\t\t ************************

 
    - Trzymaj. 

    - Dzięki. A więc tak...
    Istnieje taka legenda, lecz nikt tak naprawdę nie zna jej do końca.

    - Dobra, a o co chodzi z tymi książkami?

    - Chodzą plotki o trzech książkach...

    - Czyli starzec miał rację odnośnie tego.
    Dzięki młody, ale muszę już iść. Widzimy się później.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Wracasz do stołu, przy którym siedzi starzec

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        self.money = 5
        self.iq = 8
        
        print("-"*118)
        input("Naciśnij klawiszę ENTER, aby zacząć rozmowę ze starcem.")
        print("-"*118)

        print("""

    - Dobra starcu, miałeś racje.

    - Hehe, wiedziałem, że wrócisz. Pewnie chcesz, żebym ci dalej opowiedział o tej legendzie?!

    - Tak, prosiłbym.

    - A wiec słuchaj... Dwie z trzech ksiązek możesz otrzymać od Bartello.
    Mieszka on w wieży znajdującej się w lesie niedaleko jeziora Groch. Wieża ta zbudowana jest na niewielkim wzgórzu. 
    Jak już będziesz miał te dwie książki - przyjdź do mnie, dostaniesz ode mnie ostatnią.

    - O, niebosa! Odczuwam, że będzie to czarująca przygoda. Powiedźże mi, z kim rozmawiałem?!

    - Jestem Donatello.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Opuściłeś bar.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            """)
        
    else:
        
        print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Usiadłeś z facetem, był smutny.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    - Coś się stało?

    - Tak, pokłóciłem się z matką.	

    - Z jakiego powodu?

    - Opowiedziałem jej jadną legende, w którą ja wierze, a ona mnie wyśmiała i zaczęła mnie obrażać,
    że ją wykorzystuję.

    - Jest mi przykro. Czy mógłbyś opowiedzieć mi tą legendę.

    - Ta legenda jest od starca którego uspokoiłeś. Legenda głosi, iż istnieją ziemie, na których żyją potwory, 
    mogące cię zabić jednym tchem i bohaterzy zdolni do nieludzkich czynów i okrucieństw.
    Jeszcze chodzą plotki o trzech książkach, ale o to zapytaj starca.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Usiadłeś ze starcem.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        print("-"*118)
        input("Nacisnij klawiszę ENTER, aby zacząć rozmowę ze starcem.")
        print("-"*118)
        
        print("""

    - Dziękuje wędrowcu za piwo. 

    - Podobno znasz legendę o Piterosu. Prośiłbym opowiedzić o trzech książkach.

    - Aaaa, no to są trzy książki za pomocą których morzesz dostać się do świata tych potworów

    - W jaki sposób mogę je dostać?

    - Dwie z trzech ksiązek możesz otrzymać od Bartello.
    Mieszka on w wieży znajdującej się w lesie niedaleko jeziora Groch. Wieża ta zbudowana jest na niewielkim wzgórzu. 
    Jak już będziesz miał te dwie książki - przyjdź do mnie, dostaniesz ode mnie ostatnią.

    - O, niebosa! Odczuwam, że będzie to czarująca przygoda. Powiedźże mi, z kim rozmawiałem?!

    - Jestem Donatello.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Opuściłeś bar.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 """)

else:

    print()
    print("-"*118)
    print("""Po prawej stronie siedzi bezdomny. Po lewej stronie widziś babciu która czeka na kogoś.""")
    print("-"*118)

    print()
    ansB2 = input("Pójdzieś na prawo czy na lewo? (1 (Prawo) / 2(Lewo) ): ")
    #ansB2 - odpowiedz Bar 2

    if ansB2 == "1":

        print("""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Podszedłeś do bezdomnego. U niego na tablice było napisane:"Na książki".

Dałeś mu 2 srebra.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    
    - Witaj, biedaku. Na jakie ty ksiąki zbierasz ?

    - Ksiązki, za pomocą, których mogę stać się bohaterem.

    - Ile takie książki kosztują ? Gdzie mogę je dostać ? 

    - Ehh... Idź do starca, on ci wszystko opowie, ale nie mów, że to ja ci powiedziałem !!!

    - Gdzie mogę go znaleźć ? 

    - Zazwyczaj siedzi w barze.

    - Dobra. Powiedźże mi, z kim rozmawiałem?!

    - Mascet jestem.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Wszedłeś w bar.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")

        print("-"*118)
        input("Nacisnij klawiszę ENTER, aby zacząć rozmowę ze starcem.")
        print("-"*118)
        
        print("""

    - Witaj starzcu. Powiedzieli mi, że znasz o książkach, które pozwolą stać się bohaterem. 

    - No znam o nich.
    
    - Czy mógłbyś mi coś o nich opowiedzieć ? 

    - Opowiem ci legendę o Piterosu. Głosi ona, iż istnieją ziemie, na których żyją potwory, 
      mogące cię zabić jednym tchem i bohaterzy zdolni do nieludzkich czynów i okrucieństw. 
      Mój dziadek powiedział o 3 książkach, za pomocą których możesz się tam dostać.
    
    - To są bzdury!!

    - Cholera jasna, jak nie wierzysz, to zapytaj innych!!


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Odszedłeś od stołu.

Usiadłeś z facetem.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        print("-"*118)
        input("Naciśnij klawiszę ENTER, aby zacząć rozmowę z facetem.")
        print("-"*118)

        print("""

    - Witaj młody! Ten starzec powiedział, że znasz legendę o Piterosu. 

    - Nic nie wiem, pewnie znowu jest pijany i wymyślił jakąś bzdurę. O czym on ci powiedział?

    - Opowiadał, że istnieją ziemie, zamieskujące przez nieznanych potworów, którzy bez trudu cię zabiją.

    - No dobra, być może coś wiem. Musiałbym odświeżyć pamięć. Myślę, że kubek cydru mi w tym pomoże.

        
\t\t\t\t\t ************************
\t\t\t\t\t
\t\t\t\t\t   Masz 5 srebra i 8 iq
\t\t\t\t\t
\t\t\t\t\t ************************

 
    - Trzymaj. 

    - Dzięki. A więc tak...
    Istnieje taka legenda, lecz nikt tak naprawdę nie zna jej do końca.

    - Dobra, a o co chodzi z tymi książkami?

    - Chodzą plotki o trzech książkach...

    - Czyli starzec miał rację odnośnie tego.
    Dzięki młody, ale muszę już iść. Widzimy się później.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Wracasz do stołu, przy którym siedzi starzec

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        
        self.money = 5
        self.iq = 8
        
        print("-"*118)
        input("Naciśnij klawiszę ENTER, aby zacząć rozmowę ze starcem.")
        print("-"*118)

        print("""

    - Dobra starcu, miałeś racje.

    - Hehe, wiedziałem, że wrócisz. Pewnie chcesz, żebym ci dalej opowiedział o tej legendzie?!

    - Tak, prosiłbym.

    - A wiec słuchaj... Dwie z trzech ksiązek możesz otrzymać od Bartello.
    Mieszka on w wieży znajdującej się w lesie niedaleko jeziora Groch. Wieża ta zbudowana jest na niewielkim wzgórzu. 
    Jak już będziesz miał te dwie książki - przyjdź do mnie, dostaniesz ode mnie ostatnią.

    - O, niebosa! Odczuwam, że będzie to czarująca przygoda. Z kim miałem okazję porozmawiać ?!

    - Jestem Donatello.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Opuściłeś bar.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            """)

    else:
        
        print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Podszedłeś do babci.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    - Dobry wieczór ! Czemu Pani jest taka smutna ? 

    - No witaj młody! Pokłóciłam się z synem.

    - Z jakiego powodu ? Być może mogę czymś pomóc ? 

    - Jak masz ochotę, to możesz. Wszystko zaczęło się przez jakieś książki. Ciagle o nich rozmawia i gada jakieś głupoty.

    - Mogę z nim porozmawiać ? 

    - Tak, byłabym bardzo wdzięczna. 

    - Gdzie on jest teraz ? 

    - Pewnie siedzi w barze, możesz do niego podejść, jest wysoki i ma ciemne włosy.

    - Sprobuję czymś pomoć. Do zobaczenia!

    - Do zobaczenia!


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Wszedłeś w bar.

Zobaczyłeś faceta.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")

        print("-"*118)
        input("Nacisnij klawiszę ENTER, aby zacząć rozmowę z facetem.")
        print("-"*118)

        print("""

    - Witaj młody, wiem że pokłociłeś się z matką przez jakieś książki.

    - Tak, pokłóciłem się z matką.  

    - Z jakiego powodu? O co chodzi z tymi książkami ?

    - Opowiedziałem jej jedną legende, w którą ja wierze, a ona mnie wyśmiała i zaczęła mnie obrażać,
    że ją wykorzystuję.

    - Jest mi przykro. Czy mógłbyś opowiedzieć mi tą legendę.

    - Ta legenda jest od starca którego uspokoiłeś. Legenda głosi, iż istnieją ziemie, na których żyją potwory, 
    mogące cię zabić jednym tchem i bohaterzy zdolni do nieludzkich czynów i okrucieństw.
    Jeszcze chodzą plotki o trzech książkach, ale o to zapytaj starca.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Usiadłeś ze starcem.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
        print("-"*118)
        input("Nacisnij klawiszę ENTER, aby zacząć rozmowę ze starcem.")
        print("-"*118)
        
        print("""

    - Dziękuje wędrowcu za piwo. 

    - Podobno znasz legendę o Piterosu. Prośiłbym opowiedzić o trzech książkach.

    - Aaaa, no to są trzy książki za pomocą których morzesz dostać się do świata tych potworów

    - W jaki sposób mogę je dostać?

    - Dwie z trzech ksiązek możesz otrzymać od Bartello.
    Mieszka on w wieży znajdującej się w lesie niedaleko jeziora Groch. Wieża ta zbudowana jest na niewielkim wzgórzu. 
    Jak już będziesz miał te dwie książki - przyjdź do mnie, dostaniesz ode mnie ostatnią.

    - O, niebosa! Odczuwam, że będzie to czarująca przygoda. Powiedźże mi, z kim rozmawiałem?!

    - Jestem Donatello.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Opuściłeś bar.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")

print(h.bp())

print("\\"*118)
input("""

Niciśnij klawiszę ENTER, aby zacząć 2 Rozdział.

    """)
print("\\"*118)
print("\n"*50)
