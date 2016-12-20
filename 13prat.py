# -*- coding: utf-8 -*-

# 1. A->C: igja2281 betkas 3
# 2. A<-C:  Ta25JA1IaTSaIHPywzqHHNG
	# Desifruojam ka gaunam (vedam 36*Ta25JA1IaTSaIHPywzqHHNG)	3 betkas 32 srzXVYPrrxq
# 3. A->B: srzXVYPrrxq
# 4. A<-B:  Ya   (32*Ya) desifr

# 35

# YZ siuncima 5 zings

# 5. A->B: YZ
# Pasitikrinkite įvedę eilutę, sudarytą iš protokolo žingsnių informacijos į tikrinimo lauką. Žingsnių domenis atskirkite * 

# igja2281 betkas 3*Ta25JA1IaTSaIHPywzqHHNG*srzXVYPrrxq*Ya*YZ

# 1.
# Jums skirtas laiškas:
# qD FfF6DIPJE6f9QDM6ODNg
# Įveskite į atsakymų puslapį:
# Needham-Shroeder
# igja2281 betkas 3*Ta25JA1IaTSaIHPywzqHHNG*srzXVYPrrxq*Ya*YZ
# VTWNppvoxORgXNfxq

# 2.
# pagal Shamiro schemą s = 10300400

# 3.
# pagal  Asmutho-Blumo schema s = 9174800

# p =  68719476767
# [X1, S1] = [ 146796817 , 29056378155 ]
# [X2, S2] = [ 146796817 , 29056378155 ]
# [X3, S3] = [ 146796817 , 29056378155 ]
# [X4, S4] = [ 146796817 , 29056378155 ]
# [X5, S5] = [ 146796817 , 29056378155 ]

#VEIK ANT SAGE
x1 = 980759118118
x2 = 3065256035496
x3 = 963336033070
s1 = 2462948040396
s2 = 2764336936139
s3 = 676749965840
p=3138428376749

S = s1 * ((x2 * x3) / ((x2 - x1)*(x3 - x1))) + s2 * ((x1 * x3) / ((x1 - x2)*(x3 - x2))) + s3 * ((x1 * x2) / ((x1 - x3)*(x2 - x3)))
print (S % p)



p = 18349601
p1 = 36699211
p2 = 73398427
p3 = 146796817
s1 = 27522574
s2 = 27522584
s3 = 27522547

S0 = s1 * (p2*p3)* (1/(p2*p3) % p1) + s2 * (p1*p3)* (1/(p1*p3) % p2) + s3 * (p1*p2)* (1/(p1*p2) % p3)

S = (S0 %(p1*p2*p3)) % p

print S

def naujassifras(a1,x, p, S):
    return (a1*x+S)%p

naujas_p = next_prime(2^36)
naujas_x1 = 146796817
naujas_s1 = naujassifras(666, naujas_x1,naujas_p,S) 
naujas_x2 = 146796817
naujas_s2 = naujassifras(666, naujas_x2,naujas_p,S) 
naujas_x3 = 146796817
naujas_s3 = naujassifras(666, naujas_x3,naujas_p,S) 
naujas_x4 = 146796817
naujas_s4 = naujassifras(666, naujas_x4,naujas_p,S) 
naujas_x5 = 146796817
naujas_s5 = naujassifras(666, naujas_x5,naujas_p,S) 

print "p = ", naujas_p
print"[X1, S1] = [" , naujas_x1 , "," ,+ naujas_s1, "]"
print"[X2, S2] = [" , naujas_x2 , "," ,+ naujas_s2, "]"
print"[X3, S3] = [" , naujas_x3 , "," ,+ naujas_s3, "]"
print"[X4, S4] = [" , naujas_x4 , "," ,+ naujas_s4, "]"
print"[X5, S5] = [" , naujas_x5 , "," ,+ naujas_s5, "]"