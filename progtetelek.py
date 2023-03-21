from random import randint

szamok:list[int] = []
for x in range(10):
    szamok.append(randint(10, 99))
print(szamok)

sm:int = 0
for n in szamok:
    sm += n
print(f'számok összege: {sm}')

mini:int = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = i
print(f'minimum index: {mini}')
print(f'minimum érték: {szamok[mini]}')

c:int = 0
for n in szamok:
    if n % 2 == 0:
        c += 1
print(f'páros számok száma: {c}')

ksz:int = int(input('keresett szám: '))

i:int = 0
while i < len(szamok) and szamok[i] != ksz:
    i += 1
if i < len(szamok):
    print('benne van a keresett szám a sorozatban')
    print(f'a {ksz} idexe: {i}')
else:
    print('nincs benne a keresett szám a sorozatban')