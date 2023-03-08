import math
from cmath import sqrt
import sympy as sym

x=sym.Symbol("x")


xzad1=0.5
xzad2=1
xzad3=1.5

fce=((-12*(-x+2))/(x**2))

fone=sym.diff(fce,x,1)

f1der=fone.subs(x,xzad2)
f2der=(((fone.subs(x,xzad2))-(fone.subs(x,xzad1)))/(xzad2-xzad1))

x3=(xzad2-(f1der/f2der))

x4=(x3-((fone.subs(x,x3)/f2der.subs(x,x3))))

x5=(x4-((fone.subs(x,x4)/f2der.subs(x,x4))))



#print(f1der,"\n",f2der,"\n",x3,"\n",x4,"\n",x5,"\n")


fone=sym.diff(fce,x,1)


#f1der=fone.subs(x,xzad3)

#pro2
fxlower=((fce.subs(x,xzad2)-fce.subs(x,xzad1))/(xzad2-xzad1))

#pro x3
f1der=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
f2der=((f1der-fxlower)/(xzad3-xzad2))
############

x4=(xzad3-(f1der/f2der)) 
#print(x4)

fxlower=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
f1der=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
f2der=((f1der-fxlower)/(x4-xzad3))
x5=(x4-(f1der/f2der)) 
#print(x5)

fxlower=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
f1der=((fce.subs(x,x5)-fce.subs(x,x4))/(x5-x4))
f2der=((f1der-fxlower)/(x5-x4))
x6=(x5-(f1der/f2der)) 
#print(x6)

fxlower=((fce.subs(x,x5)-fce.subs(x,x4))/(x5-x4))
f1der=((fce.subs(x,x6)-fce.subs(x,x5))/(x6-x5))
f2der=((f1der-fxlower)/(x6-x5))
x7=(x6-(f1der/f2der)) 
print(x7)

lista=[]
lista.append(x4)
listb=[]
listb.append(x5)
listc=[]
listc.append(x6)

inc=0
for i in range(20):
    
    
    fxlower=((fce.subs(x,listb[inc])-fce.subs(x,lista[inc]))/(listb[inc]-lista[inc]))
    f1der=((fce.subs(x,listc[inc])-fce.subs(x,listb[inc]))/(listc[inc]-listb[inc]))
    f2der=((f1der-fxlower)/(listc[inc]-listb[inc]))
    x7=(listc[inc]-(f1der/f2der)) 
    
    lista.append(listb[inc])
    listb.append(listc[inc])
    listc.append(x7)
    inc=inc+1
    print(x7,'lop')







  