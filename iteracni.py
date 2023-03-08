import math
from cmath import sqrt
import sympy as sym

x=sym.Symbol("x")

###########################################################################
##NEWTON

xzad1=0.5
xzad2=2.5

#puvodni fce
fce=(-x/(1+x**2))

#prvni deriv
fone=sym.diff(fce,x,1)
#druha deriv
ftwo=sym.diff(fce,x,2)

'''
#pro bod xzad1
'''


#x2 pro x1 sub.

x2=(xzad1-(fone.subs(x,xzad1)/ftwo.subs(x,xzad1)))

x3=(x2-((fone.subs(x,x2)/ftwo.subs(x,x2))))

x4=(x3-((fone.subs(x,x3)/ftwo.subs(x,x3))))

#print(x2,"\n",x3,"\n",x4,"\n")

'''
#pro bod xzad2
'''

x2=(xzad2-(fone.subs(x,xzad2)/ftwo.subs(x,xzad2)))

x3=(x2-((fone.subs(x,x2)/ftwo.subs(x,x2))))

x4=(x3-((fone.subs(x,x3)/ftwo.subs(x,x3))))


#print(x2,"\n",x3,"\n",x4,"\n")

###########################################################################
##REGULA FASI

xzad1=0
xzad2=0.25
xzad3=0.5

fce=(-x/(1+x**2))
'''
pro body 1,2
'''

fone=sym.diff(fce,x,1)

fx1=fone.subs(x,xzad2)
fx2=(((fone.subs(x,xzad2))-(fone.subs(x,xzad1)))/(xzad2-xzad1))

x3=(xzad2-(fx1/fx2))

x4=(x3-((fone.subs(x,x3)/fx2.subs(x,x3))))

x5=(x4-((fone.subs(x,x4)/fx2.subs(x,x4))))



#print(fx1,"\n",fx2,"\n",x3,"\n",x4,"\n",x5,"\n")



'''
pro bod3
'''
fone=sym.diff(fce,x,1)


#fx1=fone.subs(x,xzad3)

#pro2
fx12=((fce.subs(x,xzad2)-fce.subs(x,xzad1))/(xzad2-xzad1))

#pro x3
fx1=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
fx2=((fx1-fx12)/(xzad3-xzad2))
############

x4=(xzad3-(fx1/fx2)) 

#print(x4)

fx12=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
fx1=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
fx2=((fx1-fx12)/(x4-xzad3))
x5=(x4-(fx1/fx2)) 
#print(x5)

fx12=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
fx1=((fce.subs(x,x5)-fce.subs(x,x4))/(x5-x4))
fx2=((fx1-fx12)/(x5-x4))
x6=(x5-(fx1/fx2)) 
#print(x6)



##########################################
#CV1

#a

xzad1=1

fce=((-12*(-x+2))/(x**2))

#prvni deriv
fone=sym.diff(fce,x,1)
#druha deriv
ftwo=sym.diff(fce,x,2)

#x2 pro x1 sub.
x2=(xzad1-(fone.subs(x,xzad1)/ftwo.subs(x,xzad1)))

x3=(x2-((fone.subs(x,x2)/ftwo.subs(x,x2))))

x4=(x3-((fone.subs(x,x3)/ftwo.subs(x,x3))))

x5=(x4-((fone.subs(x,x4)/ftwo.subs(x,x4))))

x6=(x5-((fone.subs(x,x5)/ftwo.subs(x,x5))))

#print(xzad1,"\n",x2,"\n",x3,"\n",x4,"\n",x5,"\n",x6,"\n")


#b
xzad1=0.5
xzad2=1
xzad3=1.5

fce=((-12*(-x+2))/(x**2))

fone=sym.diff(fce,x,1)

fx1=fone.subs(x,xzad2)
fx2=(((fone.subs(x,xzad2))-(fone.subs(x,xzad1)))/(xzad2-xzad1))

x3=(xzad2-(fx1/fx2))

x4=(x3-((fone.subs(x,x3)/fx2.subs(x,x3))))

x5=(x4-((fone.subs(x,x4)/fx2.subs(x,x4))))



#print(fx1,"\n",fx2,"\n",x3,"\n",x4,"\n",x5,"\n")


fone=sym.diff(fce,x,1)


#fx1=fone.subs(x,xzad3)

#pro2
fx12=((fce.subs(x,xzad2)-fce.subs(x,xzad1))/(xzad2-xzad1))

#pro x3
fx1=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
fx2=((fx1-fx12)/(xzad3-xzad2))
############

x4=(xzad3-(fx1/fx2)) 

#print(x4)

fx12=((fce.subs(x,xzad3)-fce.subs(x,xzad2))/(xzad3-xzad2))
fx1=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
fx2=((fx1-fx12)/(x4-xzad3))
x5=(x4-(fx1/fx2)) 
#print(x5)

fx12=((fce.subs(x,x4)-fce.subs(x,xzad3))/(x4-xzad3))
fx1=((fce.subs(x,x5)-fce.subs(x,x4))/(x5-x4))
fx2=((fx1-fx12)/(x5-x4))
x6=(x5-(fx1/fx2)) 
#print(x6)

fx12=((fce.subs(x,x5)-fce.subs(x,x4))/(x5-x4))
fx1=((fce.subs(x,x6)-fce.subs(x,x5))/(x6-x5))
fx2=((fx1-fx12)/(x6-x5))
x7=(x6-(fx1/fx2)) 
#print(x7)

la=4
lb=5
lc=6

'''
for i in range(10):
    xa="x"+str(la)
    la=la+1
    
    xb="x"+str(lb)
    lb=lb+1
    
    xc="x"+str(lc)
    lc=lc+1

    fx12=((fce.subs(x,xb)-fce.subs(x,xa))/(xb-xa))
    fx1=((fce.subs(x,xc)-fce.subs(x,xb))/(xc-xb))
    fx2=((fx1-fx12)/(xc-xb))
    x7=(xc-(fx1/fx2))  
    print(x7)
   
'''
