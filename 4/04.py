# primitív típusok (int, float, bool, str)

# kollekciók LISTA!! list

# lista egy adatszerkezet (változó), amiben több értéket tárolunk egyszerre

# LISTÁK TULAJDONSÁGAI:
#     - nincs megkötve a benne tárolható adattípus
#     - változtatható (beszúrni a végére: .append()
#     - ugyanaz az érték többször is szerepelhet
#     - van sorrendiség, és mindig marad!!

# létrehozása: list(), vagy []
# elem hozzáadása: lista_neve.append(elem)
# listák hossza: len()  -->  lenght
# indexek lekérdezése: lista_neve[index]--> indexedik elemmel (0-tól indexelünk)


# break, continue
# break: MEGÁLLÍTJA A CIKLUST!
# continue: A MARADÉK KÓDRÉSZLETET KIHAGYVA A KÖVETKEZŐ CIKLUSRA UGRIK

# indexek

feltetek = ["sajt", "bacon", "ananász", "pepperoni"]

# range(kezdőpont, végpont, lépés)
# hogyan kérdezem le a legutolsó elemet?

gyumik = ["apple", "banana", "cherry", "pomelo", "orange"]

print(gyumik[::-1])
