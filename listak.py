#                     0         1        2         3
nevek:list[str] = ['Zoltán', 'Erika', 'Dénes', 'Eszter']

for nev in nevek:
    print(f'\t- {nev}')

lista_hossza:int = len(nevek)
print(f'lista hossza: {lista_hossza}')

print(nevek)
print(nevek[0])

nevek[0] = 'András'
print(nevek)

# ha "nem létező" helyre hivatkozol 
# -> [out of rage exception]t fogsz kapni
# print(nevek[99])

for i in range(len(nevek)):
    print(f'a lista {i + 1}. eleme: {nevek[i]}')

nevek.append('Balázs')
print(nevek)

nevek.insert(2, 'Flóra')
print(nevek)

# a paraméterben megadott indexű helyen lévő elemet eltávolítja
nevek.pop(2)
print(nevek)

# zárójelben megadott értékű elem ELSŐ ELŐFORDULÁSÁT
# eltávolítja a listáról
nevek.remove('Eszter')
print(nevek)

# ha olyat kap a remove, ami nincs, akkor -> exception
# nevek.remove('Héfaisztosz')

nevek.insert(0, 'Béla')
nevek.insert(3, 'Béla')
print(nevek)
nevek.remove('Béla')
print(nevek)

denes_index:int = nevek.index('Dénes')
print(f'Dénes indexe: {denes_index}')

# hef_index:int = nevek.index('Héfaisztosz')

nevek.sort()
print(nevek)

nevek.reverse()
print(nevek)

szamok:list[int] = [3, 4, 12, 6, 71]

if 23 in szamok: print('a 23 benne van a listában')
else: print('a 23 nincs benne a listában')