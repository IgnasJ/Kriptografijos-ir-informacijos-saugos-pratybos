 # coding=UTF-8
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lmbda1=[5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
lmbda2=[20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
raktas=[11, 14]
# Teksto ðifravimas su keitiniu

def roNuoA(a, m):
	return (m + abc.index(a) )%26

k1 = raktas[0]
k2 = raktas[1]	

def atsifr(raide, lmb, raidesIndex):
	naujaraide = lmb[roNuoA(raide, raidesIndex)]
	return roNuoA(abc[naujaraide], -raidesIndex)

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

for i in range(0, 26):
	print (i)
	print (rez(txt, lmbda1, lmbda2, k1, i))

