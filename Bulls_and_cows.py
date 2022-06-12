"""
projekt_2: druhý projekt do Engeto Online Python Akademie
Bulls_&_Cows.py
author: Martin Žůrek
email: zurek.m@email.cz
discord: MartinZ#0894
"""

# Dodelat profily s heslama, statistiky odehranych her, vyhrane, prohrane, 
# nedokoncene casy, celkovy odehrany cas. POstupne profily pridavat 
# a kontrolovat, jestli pri vytvareni uz neexistuje


# Poznamka:
#
# Cely kod jsem pro pochopitelnost a prehlednost rozdelil do nekolika celku:
#   - Hlavni while smycka
#      - Menu 1 - Nova hra
#         - Overeni spravnosti uzivatelem zadaneho cisla
#         - Pocitani bulls a cows
#      - Menu 2 - Statistiky  
#

import os

bool_konec_programu = False

str_volba_menu = None

str_zadane_cislo = None

###############################################################################
# Hlavni while smycka                                                         #
###############################################################################

while not bool_konec_programu:

    os.system("cls")

    print()
    print("Hlavni menu:")
    print(" 1 - Nova hra")
    print(" 2 - Statistiky")
    print(" q - Konec hry")
    print()

    str_volba_menu = input("Zvol menu:")
    # int_volba_menu = "1"

    print()

    ###############################################################################
    # Menu 1 - Nova hra                                                           #
    ###############################################################################

    if str_volba_menu == "1":

        os.system("cls")

        print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""
)
        # Iniciace promennych 
        int_pocet_bulls = 0
        int_pocet_cows = 0
        int_pocet_pokusu = 0

        while int_pocet_bulls != 4:

            # rand funkce od 1000 do 9999
            str_tajne_cislo = "1234"

            str_zadane_cislo = input("")

            int_pocet_pokusu += 1

            
            ###########################################################################
            # Overeni spravnosti uzivatelem zadaneho cisla                            #
            ###########################################################################

            bool_parametry_cisla_ok = False

            # Zjisteni, jestli ma uzivatelem zadane cislo povolene parametry
            if str_zadane_cislo.isdecimal() == True:
                # Pocet cislic v cisle je od 1 do 3.
                if len(str_zadane_cislo) >= 1 and len(str_zadane_cislo) <= 3:
                    print("Pocet zadanych cislic je mensi nez 4")
                    print("-----------------------------------------------")
                # Pocet cislic v cisle = 4.
                elif len(str_zadane_cislo) == 4:
                    # Je prvni cislice v cisle nula?
                    if str_zadane_cislo[0] == "0":
                        print("Cislo nesmi zacinat nulou")
                        print("-----------------------------------------------")
                    # Pokud neni prvni cislice v cisle nula.
                    else:
                        # Cyklus vezme jednotlive cisla v uzivetelem zadanem cisle 
                        # a pomoci funkce count spocita pocet vyskytu.
                        for xx_pocet_stejnych_cisel in set(str_zadane_cislo):
                            # Pokud je pocet vyskytu dva a vice
                            if str_zadane_cislo.count(xx_pocet_stejnych_cisel) > 1:
                                print("V zadanem cisle jsou duplicity")
                                print("-----------------------------------------------")
                                break
                        # Pokud se kazda cislice v cisle vyskytuje pouze jednou.
                        else:
                            bool_parametry_cisla_ok = True
                            # print("Zadane cislo ma spravny format")
                # Pocet cislic v cisle je 5 a vice.
                elif len(str_zadane_cislo) >= 5:
                    print("Pocet zadanych cislic je vetsi nez 4")
                    print("-----------------------------------------------")
            # Uzivatel nic nezadal.
            elif str_zadane_cislo == "":
                print("Nezadal jsi nic")
                print("-----------------------------------------------")
            # Navrat do hlavniho menu
            elif str_zadane_cislo == "q":
                break           
            # Uzivatel nezadal cislo.
            else:
                print("Nezadal jsi cislo")
                print("-----------------------------------------------")


            ###########################################################################
            # Pocitani bulls a cows                                                   #
            ###########################################################################

            if bool_parametry_cisla_ok == True:

                # Pocet bulls a cows po kazdem pruchodu smyckou musi smazat. Pokud se
                # nesmaze, tak dochazi k tomu, ze se pocty inkrementuji s pocty 
                # z predchoziho kola.
                int_pocet_bulls = 0
                int_pocet_cows = 0

                # Spocita pocet bulls
                for idx, cislo in enumerate(str_zadane_cislo):
                    if cislo == str_tajne_cislo[idx]:
                        int_pocet_bulls += 1

                # Spocita pocet cows
                for idx, cislo_zadane in enumerate(str_zadane_cislo):
                    for idx_2, cislo_tajne in enumerate(str_tajne_cislo):
                        if cislo_zadane == cislo_tajne and idx != idx_2:
                            int_pocet_cows += 1

                # Urci bull / bulls
                if int_pocet_bulls == 0 or int_pocet_bulls == 1:
                    str_bull_bulls = "bull"
                else:
                    str_bull_bulls = "bulls"

                # Urci cow / cows
                if int_pocet_cows == 0 or int_pocet_cows == 1:
                    str_cow_cows = "cow"
                else:
                    str_cow_cows = "cows"

                print(f"{int_pocet_bulls} {str_bull_bulls}, \
                        {int_pocet_cows} {str_cow_cows}")
                print("-----------------------------------------------")
                
                if int_pocet_bulls == 4:

                    print("Correct, you've guessed the right number")
                    print(f"in {int_pocet_pokusu} guesses!")
                    print("-----------------------------------------------")

                    bool_navrat_do_menu = False
                    str_navrat_do_menu = input("Pro navrat do hlavniho menu zadej pismeno q:")
                    if str_navrat_do_menu == "q":
                        bool_navrat_do_menu = True

        print(f"Pocet pokusu: {int_pocet_pokusu}")

    ###############################################################################
    # Menu 2 - Statistiky                                                         #
    ###############################################################################

    if str_volba_menu == "2":

        os.system("cls")

        str_ukonceni_statistik = None
        while str_ukonceni_statistik != "q":
            print("Statistiky ..")
            print()
            str_ukonceni_statistik = input("Pro navrat do hlavniho menu \
                                            zadej pismeno q:")

    if str_volba_menu == "q":
        break
    
    # Hlavni smycka projede pouze jednou
    # bool_konec_programu = True

