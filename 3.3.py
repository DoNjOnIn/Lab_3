import math as m
x = float(input('x='))
r = float(input('R='))
if x<=-r:
    y=r
elif x>-r and x<r:
    y=r-m.sqrt(r*r-x*x)
elif x>=r and x<=6:
    y=r+(-3-r)/(6-r)*(x-r)
elif x>6:
    y=x+9
print('y='+str(y))