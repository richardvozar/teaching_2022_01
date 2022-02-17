
# print() --> kiírjunk valamit a képernyőre / konzolra
# input() --> beolvasás a konzolról | !!! MINDIG STR TÍPUST TÁROL!!!

# tároljuk el a születési évét a felhasználónak
# majd írjuk ki az életkorát

ev = int(input("Melyik évben születtél: "))

eletkor = 2022 - ev

print("Te " + str(eletkor) + " éves vagy.")
