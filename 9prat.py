# -*- coding: utf-8 -*-
from fractions import gcd
# def raskPrivRakta(viesasRaktas, s, modulis):
	# privatusRaktas = []
	# for i in viesasRaktas:
		# temp = i * s % modulis
		# privatusRaktas.append(temp)
	# #print (privatusRaktas)
	# return privatusRaktas
	
# def dekoduokVienaChar(char, privatusRaktas):
	# dekoduotas = 0
	# #print(char)
	# for i in range(0, 8):
		# if (char - privatusRaktas[7-i]) >= 0:
			# dekoduotas += 2**(7-i)
			# char -= privatusRaktas[7-i]
			# #print (char, 7-i)
	# #print (char)
	# return dekoduotas
	
# def normaliaiDekoduok(char):
	# temp = 0
	# if(char & 1) == 1:
		# temp += 128
	# if(char & 2) == 2:
		# temp += 64
	# if(char & 4) == 4:
		# temp += 32
	# if(char & 8) == 8:
		# temp += 16
	# if(char & 16) == 16:
		# temp += 8
	# if(char & 32) == 32:
		# temp += 4
	# if(char & 64) == 64:
		# temp += 2
	# if(char & 128) == 128:
		# temp += 1
	# return temp

# def dekoduok(sifras, privatusRaktas, s, modulis):
	# txt = ""
	# for c in sifras:
		# c0 = c*s%(modulis)
		# dekoduotas = dekoduokVienaChar(c0,privatusRaktas)
		# #print("dekoduotas", dekoduotas)
		
		# #print (bin(dekoduotas))
		# #print("sifras ",c0)
		# txt += chr(normaliaiDekoduok(dekoduotas))
	# return txt







# viesasRaktas = [76929, 96961, 45633, 8705, 181329, 97340, 110916, 86767]
# privRaktoDalis = 1080
# modulis = 182757
# sifras = [262215, 335406, 239934, 326701, 532179, 348982, 45633, 359555, 229361, 521606, 229361, 262215, 229361, 348982, 45633, 359555, 326701, 348982, 335406, 348982]

# v0 = 76929
# s = 11209# s = (privRaktoDalis/gcd(v0,modulis))/(viesasRaktas[0]/gcd(v0,modulis))%(modulis/gcd(v0,modulis))
# s = (privRaktoDalis/gcd(v0,modulis))/(viesasRaktas[0]/gcd(v0,modulis))%(modulis/gcd(v0,modulis))
# privatusRaktas = raskPrivRakta(viesasRaktas, s + 4*modulis//7, modulis)#jei su s neduoda superdidejancios sekos, tada prie s reikia prideti 
# #n * modulis/gcd(v0,modulis), cia n = 1,..,gcd(v0,modulis), o v0 yra pirmas vieso rakto elementas
# print(privatusRaktas)
# s = s + 4*modulis//7
# text = dekoduok(sifras,privatusRaktas, s, modulis)
# print(text)


V = [76929, 96961, 45633, 8705, 181329, 97340, 110916, 86767] #Viesas raktas
C = [262215, 335406, 239934, 326701, 532179, 348982, 45633, 359555, 229361, 521606, 229361, 262215, 229361, 348982, 45633, 359555, 326701, 348982, 335406, 348982]
w0 = 1080  #Viesas raktas
p = 182757 #modulis

d = gcd(V[0], p) #Jei d = 1 tai puiku

print (d)

s = w0/V[0]%(p/d)
print (s)
w = []
for e in V:
    w.append(e*s%p)
print (w)  
    
Cx = []

for c in C:
    Cx.append(c*s%p)
    
print (Cx)


def apverks(str):
    newstr = ""
    s8 = str[0]
    s7 = str[1]
    s6 = str[2]
    s5 = str[3]
    s4 = str[4]
    s3 = str[5]
    s2 = str[6]
    s1 = str[7]
    newstr += s1
    newstr += s2
    newstr += s3
    newstr += s4
    newstr += s5
    newstr += s6
    newstr += s7
    newstr += s8
    
    return newstr


rez = ""

for x in range(len(Cx)):
    temp = Cx[x]
    str = ""
    for i in range(len(w)):
        i += 1
        if(temp >= w[len(w) - i]):
            str += "1"
            temp = temp - w[len(w) - i]
            #print temp
        else:
            str += "0"
    print (str)
    rez += chr(int(apverks(str),2))    


print (rez)
#e = "00100000" #=> 4386
#chr(int(e,2))