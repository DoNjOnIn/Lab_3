import math as m
x=float(input('x='))
d=x*x*m.sin(x/2)
if x<=-5:
    print('y='+str(d+m.atan(m.e**x)))
elif x >= -5 and x<=0:
    print('y='+str(d+1+x**3/4))
elif x > 0:
    print('y=' + str(d + m.log10(x)))