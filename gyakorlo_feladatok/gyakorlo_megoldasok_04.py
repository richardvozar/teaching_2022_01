"""
1. feladat
Írj egy programot, ami összeszorozza 1-től 10-ig számokat, eltárolja az eredményt, majd kiírja.
"""
osszeg = 1
for i in range(2, 11):
	osszeg *= i
print(osszeg)


"""
2. feladat
Készíts egy szamok nevű listát rendre a következő elemekkel: 10, 11, 12, 20, 21, 23
	a) írj egy programot, ami összeadja az összes elemet a listában, majd kiírja
	b) írj egy programot, ami kiírja a listában a legnagyobb elemet
	c) írj egy programot, ami a második elemtől (1. indexű) kezdve a negyedik (3. indexű) elemig kiírja a lista tartalmát (a negyedik elem még legyen benne)
	d) írj egy programot, ami az utolsó elemet megváltoztatja 22-re
"""
szamok = [10, 11, 12, 20, 21, 23]

# a)
osszeg = 0
for szam in szamok:
	osszeg += szam

print(osszeg)

# b)
legnagyobb = szamok[0] # adok egy kezdőértéket a legnagyobbnak, mondjuk a lista legelső elemét

for szam in szamok:
	if szam > legnagyobb:
		legnagyobb = szam

print(legnagyobb)

# c)
print(szamok[1:4])

# d)
szamok[-1] = 22


"""
3. feladat
Írj egy programot, amely eltárolja a teljes_nev változóba a "Vladimir Putyin" szöveget.
A program mentse ki a teljes nevet egy v_nev és egy k_nev változóba.
Gondolatmenet: járjuk végig a sztringet, majd ha találunk szóközt, mentsük el, hogy melyik indexen van. Ezután már csak a megfelelő intervallumát kell kimenteni a sztringnek.
"""
teljes_nev = "Vladimir Putyin"

szokoz_indexe = 0
for i in range(len(teljes_nev)):
	if teljes_nev[i] == " ":
		szokoz_indexe = i

v_nev = teljes_nev[szokoz_indexe+1:]
k_nev = teljes_nev[:szokoz_indexe]


"""
4. feladat
a) Hozd létre az egytol_huszig nevű üres listát.
b) For ciklus segítségével pakolj bele minden számot 1-20-ig.
c) Írj egy programot, ami egy paros_szamok nevű listába eltárol minden páros számot az egytol_huszig nevű listából.
"""
# a)
egytol_huszig = []

# b)
for i in range(1, 21):
	egytol_huszig.append(i)

# c) megoldás 1
paros_szamok = []

for szam in egytol_huszig:
	if szam % 2 == 0:
		paros_szamok.append(szam)

# c) megoldás 2
paros_szamok = egytol_huszig[1::2]