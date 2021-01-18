f0 = open("Kutyak.csv")
f1 = open("KutyaFajtak.csv")
f2 = open("KutyaNevek.csv")

f0.readline()
f1.readline()
f2.readline()

kutyak = [sor.strip().split(';') for sor in f0]
kutyafajtak = [sor.strip().split(';') for sor in f1]
kutyanevek = [sor.strip().split(';') for sor in f2]