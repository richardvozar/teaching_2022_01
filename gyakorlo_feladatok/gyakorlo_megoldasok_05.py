# 1. feladat ---------------

def piramis(n):
    for i in range(1, n+1):
        print((str(i) + ' ') * i)

#piramis(5)

#---------------------------


# 2. feladat----------------

def szorzotabla():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=' ')
        print()

#szorzotabla()

#---------------------------


# 3. feladat----------------

for i in range(5, 0, -1):
    print('* ' * i)

#---------------------------