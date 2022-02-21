# 1. feladat
def konyveket_rendez(konyvek):
	konyvek.sort()         # .sort() rendezi
	konyvek.reverse()      # konyvek[::-1] is jó megoldás lehet
	return konyvek         # visszatérek a listával

print(konyveket_rendez(['Vajak I', 'Allatfarm', 'Harry Potter es a bolcsek kove', 'A hobbit', 'Szamitogep Architekturak']))


# 2. feladat
def akcios_ar(arak, akcio):
	for i in range(len(arak)):
		# végigiterálok az árak listán

		# mindig az i-edik elemek árát lecsökkentem
		arak[i] = int(arak[i] * (1-akcio/100)) # közben elvégzem az egésszé konvertálást: int()
	
	# visszatérek a listával, amiben már a csökkentett árak vannak
	return arak

print(akcios_ar([5000, 12000, 10000, 29000, 47000], 30.0))


# 3. feladat
def belat_kirug(l):
	while 'EpicBela20' in l:
		# addig, amíg szerepel a listában, addig fut a ciklus
		l.remove('EpicBela20')

	# visszatérek a listával
	return l

print(belat_kirug(['EpicBela20', 'python4life', 'EpicBela20', 'EpicBela20', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']))


# 4. feladat
def leghosszabb_szo(szoveg):
	if len(szoveg) == 0:
		# lekezelem azt az esetet, amikor üres string érkezik
		return "HIBA!"

	# beérkezett szöveg szétradabolása szóközök mentén
	szavak = szoveg.split()

	# üres string, aminél csak hosszabb sztring lehet
	legh_szo = ""

	for szo in szavak:
		# végigiterálok a szavak listán
		if len(szo) > len(legh_szo):
			# ha hosszabb az adott szó, akkor kicserélem az eddigi leghosszabbal
			legh_szo = szo

	# visszatérek a leghosszabb szóval
	return legh_szo


print(leghosszabb_szo("Szia uram! Mondd mar meg, hogy hany ora van!"))
print(leghosszabb_szo(""))