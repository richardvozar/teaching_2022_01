"""
1. feladat
Írj egy programot amely bekéri a születési dátumodat, kiszámítja a korodat (idén hányadik évedet töltöd be), és ezt kiírja a képernyőre!
"""
szul_dat = int(input("Add meg a szuletesi evedet: "))
ev = 2022
kor = ev - szul_dat

print("Iden a " + str(kor) + ". evedet toltod be!")


"""
2. feladat
"""
print("elso kiiratas")
print("masodik kiiratas")
print("harmadik kiiratas")

# helytelen mukodes:
#prtni("elso kiiratas")    --> print fuggveny roosz: NameError: name 'prtni' is not defined
#print("masodik kiiratas)  --> hianyzo idezojel: SyntaxError
#print("harmadik kiiratas" --> hianyzo zarojel: SyntaxError


"""
3. feladat
Készíts egy rövid programot, amely egy változóban eltárol egy szót.
Próbáld meg ennek a változónak a tartalmát int értékké átalakítani. (cast-olni)
Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?
"""
szo = "sorosterv"
#szo = int(szo)         --> ValueError: invalid literal for int() with base 10: 'sorosterv'


"""
4. feladat
Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is szerepel a kódodban.
Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?
"""

#print(nem_letezo_valtozo)    --> NameError: name 'nem_letezo_valtozo' is not defined


"""
5. feladat
Írj egy programot, ami a felhasználótól bekéri először a keresztnevét, majd a vezetéknevét.
A program ezután összefűzi ezeket egy teljes_nev nevű változóba.
Végül a program a teljes nevén üdvözli a felhasználót!
"""
knev = input("Keresztneved: ")
vnev = input("Vezetekneved: ")
teljes_nev = knev + " " + vnev

print("Udvozlehelletem, " + teljes_nev + "!")


"""
6. feladat
Írj egy progarmot, amely bekéri egy téglalap két oldalát és kiszámolja, majd kiírja annak kerületét, területét és az átlójának a hosszát.
"""
print("Add meg egy teglalap ket oldalanak hosszat!")
a = float(input("Egyik oldal: "))
b = float(input("Masik oldal: "))

kerulet = 2 * (a + b)
terulet = a * b
atlo = (a ** 2 + b ** 2) ** (1/2)

print("Kerulet = " + str(kerulet))
print("Terulet = " + str(terulet))
print("Atlo = " + str(atlo))


"""
7. feladat
Írj egy programot, amely bekér a felhasználótól egy méterben megadott hosszt és azt átkonvertája kilométerbe, mérföldbe, inch-be és lábba.
A váltószámokat keresd ki a Google segítségével.
"""
hossz = float(input("Adj meg egy hosszt: "))

km = hossz / 1000
merfold = hossz * 0.0006213712
inch = hossz * 39.3700787
lab = hossz * 3.2808399

print(str(hossz) + " meter =")
print(str(km) + " km")
print(str(merfold) + " merfold")
print(str(inch) + " inch")
print(str(lab) + " lab")


"""
8. feladat
Írj egy kob() nevű függvényt, amely egy x nevű paramétert vár.
A függvény számolja ki a paraméterben érkező szám köbét, majd írja ki!
"""
def kob(x):
	print(x * x * x)    # teljesen jo az: (x ** 3)  megoldas is