bosszuallok1 = ["Thor", "Hulk"]
bosszuallok2 = ["Vízió", "Hangya", "Vasember"]

# lista i. elemének a törlése --> del lista_neve[i]

# lista_neve.append(elem)   --> lista_neve lista végére szúrta az elem értéket
# listába elem beszúrása adott indexre: lista_neve.insert(index, elem)

# listák összefűzésére: + operátor
# törlés 2.0 : lista_neve.remove(elem)
# lista ürítése: lista_neve.clear()

b = bosszuallok1 + bosszuallok2 + ["3", "2", "1"]

# rendezés: lista_neve.sort(reverse=True)

b.sort()

print(b)
