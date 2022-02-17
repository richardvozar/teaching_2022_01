"""
1. feladat
Írj egy programot, ami függőlegesen írja ki, hogy Hello.
"""
szoveg = "Hello"

for betu in szoveg:               # szintén jó megoldás: for betu in "Hello":
	print(betu)


"""
2. feladat
Készíts egy programot, ami beolvas a konzolról (input) egy egész számot és kiírja, hogy az adott szám páros vagy páratlan-e.
"""
n = int(input("Adj meg egy egész számot: "))

if n % 2 == 0:                 # ha n elosztva 2-vel 0 maradékkal tér vissza, akkor a szám páros
	print("Páros szám!")
else:
	print("Páratlan szám!")


"""
Készíts egy osztas() nevű függvényt, amely az x és y paramétereket várja.
- A program végezze el az x / y osztást, majd írja ki az eredményt!
- próbáld ki, mi történik akkor, ha az y értékének 0-t adsz!
- kezeld le ezt az esetet úgy, hogy ha 0-val akarnánk osztani, akkor csak írjuk ki a képernyőre, hogy "Nullával nem osztunk!"
"""
def osztas(x, y):
	if y == 0:
		print("Nullával nem osztunk!")
	else:
		print(x / y)

# próbáljuk ki:
osztas(5, 2)
osztas(5, 0)
osztas(0, 2)


"""
4. feladat
Készíts egy programot amely a következőt írja ki a képernyőre:
0 Éljen a Python!
2 Éljen a Python!
4 Éljen a Python!
6 Éljen a Python!

Készítsd el for loop-pal is és while loop-pal is!
"""

# for loop - megoldás 1
for i in range(0, 7, 2):
	print(str(i) + " Éljen a Python!")

# for loop - megoldás 2
for i in range(4):
	print(str(i * 2) + " Éljen a python!")

# while loop - megoldás 1
i = 0

while i < 7:
	print(str(i) + " Éljen a python!")
	i += 2                                 # i-t növelem 2-vel

# while loop - megoldás 2
i = 0

while i < 4:
	print(str(i * 2) + " Éljen a python!")
	i += 1


"""
5. feladat: Páros számok összege
Írj Python szkriptet, amely beolvas a standard bemenetről két egész számot: rendre egy zárt intervallum alsó és felső végpontját!
A program írja ki a konzolra az intervallumban található páros számok összegét!
A beolvasott alsó és felső végpontok még részei az intervallumnak.

Példa:
Az intervallum also vegpontja: 42
Az intervallum felso vegpontja: 100

A(z) [42; 100] intervallumba eso paros szamok osszege: 2130
"""

also = int(input("Az intervallum also vegpontja: "))
felso = int(input("Az intervallum felso vegpontja: "))

osszeg = 0

for i in range(also, felso+1):
	if i % 2 == 0:
		osszeg += i

print("A(z) [" + str(42) + "; " + str(100) + "] intervallumba eso paros szamok osszege: " + str(2130))