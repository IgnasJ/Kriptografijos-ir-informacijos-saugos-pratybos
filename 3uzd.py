#!/usr/bin/python3

#kodas tikrai veikiantis

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """PYBVEJHVGAKHETSDTIRPHCMVFAEYUOCVHVAC"""

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = ['K', 'A', 'R', 'D', 'A', 'S']

ans = ""

for i in range(len(c)):
	ch = abc[ (abc.index(c[i]) - abc.index(key[i % len(key)])) % 32 ]
	ans = ans + ch
	if (len(ans.replace('\n', '').replace(' ', ''))%5 == 0):
		ans = ans + " "
	if (len(ans.replace('\n', '').replace(' ', ''))%60 == 0):
		ans = ans + "\n"
	
print(ans)
	
print("win")

