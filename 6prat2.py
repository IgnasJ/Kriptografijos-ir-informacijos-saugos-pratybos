#  -*- coding: utf-8 -*-
def iter(M,k,f):
    r=M[1]
    l=M[0]^eval(f)
    return [r,l]

f='(r&k)^((k%16)|r)'
M=[[82, 225], [161, 58], [85, 249], [176, 62], [77, 254], [163, 57], [73, 227], [174, 45], [72, 235], [176, 47], [92, 232], [176, 44], [73, 231], [172, 35], [78, 230], [165, 46], [88, 241], [172, 56], [71, 255], [183, 63], [66, 248], [181, 62], [94, 234], [173, 54], [87, 232], [182, 41], [72, 225], [161, 32], [87, 241], [182, 47], [66, 228], [178, 56], [69, 246], [166, 52], [70, 230], [171, 40], [70, 248], [162, 62], [89, 234], [171, 50], [93, 245], [178, 41], [89, 234], [167, 34], [83, 247], [167, 53], [92, 247], [176, 44], [75, 248], [173, 57], [66, 250], [187, 61], [88, 250], [172, 41], [94, 252], [173, 43], [92, 245], [176, 63], [66, 245], [164, 46]]

itervect = [186, 35]


#raktas =[92, 125, 105]
#naudojam atvirkscia
#CFB  ir CRT rakto nekeiciam vietom 
k=[105, 125, 92]

#CBC skaiciuoja
for i in range(0, len(M)):
	iteraciju_rez = iter(iter(iter(M[i],k[0],f),k[1],f),k[2],f)
	ats = [iteraciju_rez[1]^itervect[0], iteraciju_rez[0]^itervect[1]]
	itervect = M[i]
	print(chr(ats[0]), end="")
	print(chr(ats[1]), end="")
	
	