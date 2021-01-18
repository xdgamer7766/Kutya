f0 = open("Kutyak.csv")
f1 = open("KutyaFajtak.csv", encoding="UTF-8")
f2 = open("KutyaNevek.csv")

f0.readline()
f1.readline()
f2.readline()

kutyak = [sor.strip().split(';') for sor in f0]
kutyafajtak = [sor.strip().split(';') for sor in f1]
kutyanevek = [sor.strip().split(';') for sor in f2]



print(f"3. Feladat: {len(kutyanevek)}")


osszkor = 0
for sor in kutyak:
    osszkor = osszkor + int(sor[3])

print(f"6. Feladat: {osszkor / len(kutyak)}")


index = 0
a = 0
for sor in kutyak:
    if sor[3] > kutyak[index][3]:
        index = a
    a += 1
fajt_id = 0
a = 0
for sor in kutyafajtak:
    if kutyak[index][1] == sor[0]:
        fajt_id = a
    a += 1
nev_id = 0
a = 0
for sor in kutyanevek:
    if kutyak[index][1] == sor[0]:
        nev_id = a
    a += 1

print(f"7. Feladat: {kutyanevek[nev_id][1]} , {kutyafajtak[fajt_id][1]}")