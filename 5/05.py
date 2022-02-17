# return utasítás --> függvényeken belül!!
# ha egy függvény elér a return utasításig --> abban a pontban ki fogunk lépni a függvényből!!
# AKÁRMILYEN TÍPUSÚ ÉRTÉKKEL VISSZA LEHET TÉRNI!
#---------------------------------------------------------

# Listaelem előfordulásának az ellenőrzése
# szintakszis:
# if elem in lista:
#----------------------------------------------------------

# SZTRINGMŰVELETEK - sztringkezelő függvények

szoveg = "a füstölt szalonna a legjobb szalonna Sváb szerint"

szoveg2 = "1234567890"

# a sztringeket kisbetűssé, és nagybetűssé alakítja
# sztring_neve.upper()
# sztring_neve.lower()

# igazzal tér vissza, ha a sztring_neve változó a paraméterben adott sztringgel kezdődik
# sztring_neve.startswith('a')
# sztring_neve.endswith('a')

# visszaadja, hogy a paraméterben átadott részsztring hányszor szerepel
# sztring_neve.count('a')

# lecseréli a sztringben lévő ÖSSZES 'old' részsztringet 'new'
# sztring_neve.replace(old, new)

# feldarabolja a sztringet a paraméterben megadott részsztring alapján
# sztring_neve.split()   --> ha nem adunk meg paramétert: szóköz alapján vágja el
# EGY LISTÁVAL FOG VISSZATÉRTNI

# igazzal tér vissza, ha a sztringünkben csak betűk szerepelnek
# sztring_neve.isalpha()

# igazzal tér vissza, ha a sztringünkben csak számok szerepelnek
# sztring_neve.isdigit()

print(szoveg2.isdigit())








