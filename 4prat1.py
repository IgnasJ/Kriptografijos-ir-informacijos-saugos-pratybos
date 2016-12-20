 # coding=UTF-8
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lmbda1=[20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
lmbda2=[8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
raktas=[2, 13]
sifras=[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
# Teksto ðifravimas su keitiniu

def roNuoA(a, m):
	return (m + abc.index(a) )%26

k1 = raktas[0]
k2 = raktas[1]	

def atsifr(raide, lmb, m):
	naujaraide = lmb[roNuoA(raide, m)]
	return roNuoA(abc[naujaraide], -m)

def rez(txt, lmbda1, lmbda2, k1, k2):
	raidesNrTekste = 0
	rezultatas = ''
	for a in txt:
		m1 = raidesNrTekste % 26
		m2 = raidesNrTekste //26
		m1 = (m1 + k1)%26
		m2 = (m2 + k2)%26
		atsifruotaspagal1 = atsifr(a, atv(lmbda2), m2)
		atsifruotaspagal2 = atsifr(abc[atsifruotaspagal1], atv(lmbda1), m1)
		rezultatas += abc[atsifruotaspagal2]
		raidesNrTekste+=1
	return rezultatas
	
# Atvirkðtinio keitinio radimas
def atv(lmb):
    l=len(lmb)
    atv=[0]*l
    for i in range(0,l):
        atv[lmb[i]]=i
    return atv

		
txt='IXDEGESDBMIBDLSWOVMBWFTPGMTTXWCZAZFSHAFPLPEABWPXCBEHDUYQTNCBLYCONKWONFLYTHO'

print (rez(txt, lmbda1, lmbda2, k1, k2))

