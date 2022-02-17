"""
1. feladat: Leghosszabb szó
Írj egy leghosszabb_szo nevű függvényt, amely egy szöveget kap paraméterül (a szöveg szóközzel elválasztott szavakat tartalmaz)!
A függvény térjen vissza a szövegben található leghosszabb szóval!
Amennyiben több szó is ugyanolyan hosszú, akkor közülük a szövegben korábban előfordulót add vissza!
Ha a paraméterül kapott szöveg az üres string, akkor a visszatérési érték a HIBA! szöveg legyen! (üres string = 0 hosszú szöveg)
"""
def leghosszabb_szo(s):
	# ha ures a string
	if len(s) == 0:
		print('HIBA!')
		return # kilép a függvényből

	words = [] # lista amibe a szavakat rakom majd

	kezdobetu_idx = 0
	utolso_betu_idx = 0

	for i in range(len(s)):
		if s[i] == ' ':
			words.append(s[kezdobetu_idx:i])  # belerakom a words listába a szót így: szöveg[kezdőbetűtől - a szóköz indexéig]
			kezdobetu_idx = i + 1   # a következő szó kezdőbetűjének az indexe a szóköz utáni karakter lesz

	words.append(s[kezdobetu_idx:]) # utolsó szót is belerakom

	
	leghosszabb = words[0]   # beállítom a kezdőértékét, hogy tudjunk mihez viszonyítani

	for word in words:
		if len(word) > len(leghosszabb):  # ha a következő vizsgált szó hossza nagyobb, mint az eddigi leghosszabb
			leghosszabb = word


	print(leghosszabb)

leghosszabb_szo("Szia uram! Mondd mar meg, hogy hany ora van!")
leghosszabb_szo("")


"""
2. feladat: Gyenge jelszavak
Elliot egy új feladattal bízza meg alkalmazottját.
Elliotnak ki kell válogatnia a vállalat által használt jelszavak közül azokat, amelyek gyengének minősülnek.
Írj egy gyenge_jelszavak nevű függvényt, amely egy jelszavakat tartalmazó listát kap paraméterül!
A függvény tegye egy új listába és írja ki ezek közül a gyenge jelszavakat!
Egy jelszót gyengének tekintünk, ha azrövidebb, mint 5 karakter.
"""
def gyenge_jelszavak(jelszavak):
	gyengek = []

	for jelszo in jelszavak:
		if len(jelszo) < 5:
			gyengek.append(jelszo)

	print(gyengek)

gyenge_jelszavak(['Root', 'Kekw2000', 'H0sszuJelszoG0esBrrr', 'Admin123456', 'sub2Pewdiepie', 'asdqwe', 'K1L0'])


"""
3. feladat: Abszolútérték-maximum
Írj egy abs_max nevű függvényt, amely két egész számot vár paraméterül, és visszatér ezek abszolútérték-maximumával!
Tehát vesszük mindkét szám abszolútértékét, és ezek közül visszaadjuk a nagyobbat.
"""
def abs_max(a, b):
	if a < 0:
		a = -a
	if b < 0:
		b = -b

	if a < b:
		print(b)
	elif b < a:
		print(a)
	else:
		print("Egyenloek!")

abs_max(12, -15)


"""
4. feladat:  Kuba
Kuba egy Discord szerveren moderátor. A szabadidejét sokszor azzal tölti, hogy a szerver bizonyos tagjainak a felhasználónevét átírja a következőképpen:
- a felhasználónév végére egy . (pont) karaktert tesz, amennyiben az eredetileg nem végződött pontra
- ellenkező esetben, pont karakterre végződő felhasználónevek esetén eltávolítja a név végéről a pontot.
Írj egy kuba nevű függvényt, amely egy felhasználónevet (string) kap paraméterül, elvégzi a fenti szabályok alapján a név átalakítását, majd kiírja az így kapott eredményt!
"""
def kuba(fnev):
	if fnev[-1] == '.':
		print(fnev[:-1])
	else:
		print(fnev + '.')

kuba('Korte12')
kuba('Tamas.')



"""
5. feladat: Armstrong-szám
A matematikában egy n-jegyű számot Armstrong-számnak nevezünk, ha minden számjegyét az n-edik hatványra emelve és összeadva az eredeti számot kapjuk.
Például a 153 egy Armstrong-szám.
Írj egy armstrong_szam nevű függvényt, amely garantáltan egy nemnegatív egész számot kap paraméterül, és kiírja, hogy a paraméterben kapott szám Armstrong-szám vagy sem!
"""
def armstrong_szam(n):
	n_len = len(str(n)) # a szam merete (pl: 1234 --> 4; 1234567 -> 7) szöveggé alakítva kaphatom meg a hosszát
	szumma = 0
	for szamjegy in str(n):  # a számot egy sztringre alakítom, és be tudom járni a karaktereit, pl: 12345 --> "12345" és a karakterei az 1, 2, 3 stb..
		szumma += int(szamjegy) ** n_len     # hosszáadom az adott számjegyet hatványra emelve, és közben int-re alakítom, hogy tudjak matematikai műveletet használni
	
	if n == szumma:
		print(True)
	else:
		print(False)

armstrong_szam(153)
armstrong_szam(1999)
armstrong_szam(8208)