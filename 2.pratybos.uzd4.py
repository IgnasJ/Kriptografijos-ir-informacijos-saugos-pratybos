#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """YŽRVČ ZSŲVS GŽGJČ GĖJGŽ ŪLŠGF 
GŽĄZG ŠGZGY HCĄŠI ČIĄIC LVUKZ 
ŪPJTD CČŪYŽ LRŠIO ŠŲČBA MCOŠZ 
PČILŪ ŽSBEU ŲMLVĘ DCHTČ IBSEN 
ZCFZG ŽYDŽS ZNŪME BGŽOĄ ŪČUĘŽ 
POĄGD CJHFĖ OĖŪ   """

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = [['T','A'], ['V', 'S']]
#det = abc.index('T') * abc.index('S') - abc.index('A') * abc.index('V')
det = 2 *25 - 3 * 25
atv = [[9, 0], [29, 7]]

ans = ""

for i in range(int(len(c)/2)):
	ans = ans + abc[(abc.index(c[i*2]) * 25 + 
					 abc.index(c[i*2+1]) * 5) % 32]
	ans = ans + abc[(abc.index(c[i*2]) * 29 + 
					 abc.index(c[i*2+1]) * 2) % 32]
	ans = ans + " "
	if (len(ans.replace('\n', ''))%72 == 0):
		ans = ans + "\n"
	
print(ans)
	
print("win")

