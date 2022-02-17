"""
1. feladat: Összefűzés
Írj Python szkriptet, amely beolvas a standard bemenetről (input()) két szöveget és rendre összefűzi azokat!
Az összefűzés eredményeképpen kapott szöveget írasd ki a konzolra!
"""
szoveg1 = input("Az egyik szoveg: ")                    # elso szoveg beolvasasa
szoveg2 = input("A masik szoveg: ")                     # masik szoveg beolvasasa

print("A ket szoveg osszefuzve: " + szoveg1 + szoveg2)  # a + operatorral osszeuzom a ket szoveget


"""
2. feladat: Négyzetgyök (input)
Írj Python szkriptet, amely beolvas a standard bemenetről egy egész számot, és kiírja annak a négyzetgyökét!
"""
szam = int(input("Adj meg egy egesz szamot: "))             # beolvasas es egesz szamma alakitas

print("A beirt szam negyzetgyoke: " + str(szam ** (1/2)))   # str-re alakitva lehet csak osszefuzni



"""
3. feladat: Négyzetgyök (függvény)
Írj egy negyzetgyok() nevű függvényt, amely egy x nevű paramétert vár. A függvény számolja ki a paraméterben érkező szám négyzetgyökét, majd írja ki!
"""
def negyzetgyok(x):
	eredmeny = x ** (1/2)                                                # itt eloszor elvegszem a gyokvonast, es kimentem egy kulon valtozoba
	print("A parameterben erketo szam negyzetgyoke: " + str(eredmeny))   # itt is str-re kell alakitani, mivel az 'eredmeny'-ben egy szam van

# pelda
negyzetgyok(2)
negyzetgyok(144)
