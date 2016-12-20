# -*- coding: utf-8 -*-
from fractions import gcd

A='abcdefghijklmnopqrstuvwxyz'
def i_skaiciu(text):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)  

def i_teksta(M):
    n=M
    text=''
    while n>0:
        ind=n%100
        ind=ind-1
        if (ind>=0) & (ind<len(A)):
            text+=A[ind]
            n=(n-ind+1)//100
        else:
            text+='?'
            n=(n-ind+1)//100            
    return text[::-1]     
    
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
	
viesasp = 12016012609141909200527091927191118250205281601
viesasAlpha = 161058
viesasBeta = 7735393332951406594699297041779941866239626261

# Algio parašai
# tekstas_1:nieko nepasirasykite=1409051115271405160119091801192511092005
# Parašas: [7739575821110705684999402384263707077895488033, 11156545394182764321741332166354317996384218342]
# tekstas_2:nepakanka lesu=1405160111011411012712051921
# Parašas: [7739575821110705684999402384263707077895488033, 1535504875397234784607977866283997512924807850]
 
tekstas_1 = 1409051115271405160119091801192511092005
parasas_1 = [7739575821110705684999402384263707077895488033, 11156545394182764321741332166354317996384218342]
 
tekstas_2 = 1405160111011411012712051921
parasas_2 = [7739575821110705684999402384263707077895488033, 1535504875397234784607977866283997512924807850]
 
print ((pow(viesasBeta, parasas_1[0], viesasp) * pow(parasas_1[0], parasas_1[1], viesasp)) % viesasp == pow(viesasAlpha, tekstas_1, viesasp))
print ((pow(viesasBeta, parasas_2[0], viesasp) * pow(parasas_2[0], parasas_2[1], viesasp)) % viesasp == pow(viesasAlpha, tekstas_2, viesasp))

# Šifruotas laiškas Algiui [C_1,C_2]=
# [11753667601652506267355175922966788227693389721, 10391180379014989098124759496258667151649033236]
# Patikrinkite parašus ir, jei pavyks, iššifruokite Algiui skirtą šifrą 
c1 = 11753667601652506267355175922966788227693389721
c2 = 10391180379014989098124759496258667151649033236


c = (parasas_1[1]-parasas_2[1])
d = (tekstas_1 - tekstas_2)
n = (viesasp-1)
e = gcd(c,n)

c0 = (c//e)
n0 = n//e
d0 = d//e
print(c0)

k0 = (d0 * modinv(c0, n0)) % n0
k1 = k0 + n0
k2 = k0 + 2*n0
k3 = k0 + 3*n0
print ("sprend")
print (k0)
print (k1)
print (k2)
print (k3)
print("tikrinimas")
print(pow(viesasAlpha, k0, viesasp) == parasas_1[0] % viesasp)
print(pow(viesasAlpha, k1, viesasp) == parasas_1[0]% viesasp)
print(pow(viesasAlpha, k2, viesasp) == parasas_1[0]% viesasp)
print(pow(viesasAlpha, k3, viesasp) == parasas_1[0]% viesasp)

print("Ar gama ir p-1 = 1?")
print(gcd(parasas_2[0],(viesasp -1)))

a = ((tekstas_2 - k0 * parasas_2[1]) * modinv(parasas_2[0], (viesasp -1)) ) % (viesasp -1)
print(a)
print(pow(viesasAlpha, a, viesasp) ==viesasBeta% viesasp)

a = ((tekstas_1 - k0 * parasas_1[1]) * modinv(parasas_1[0], (viesasp -1)) ) % (viesasp -1)
print(a)
print(pow(viesasAlpha, a, viesasp) ==viesasBeta% viesasp)


M = (c2 * pow(modinv(c1, viesasp), a, viesasp) ) % viesasp

T=i_teksta(M)
print(T)