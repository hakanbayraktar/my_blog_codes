
"""
    )   (           (                                   
 ( /(   )\      )   )\   (         )           )   (    
 )\()) ((_)  ( /(  ((_)  )\ )   ( /(   (    ( /(   )(   
((_)\   _    )(_))  _   (()/(   )(_))  )\   )(_)) (()\  
| |(_) | |  ((_)_  | |   )(_)) ((_)_  ((_) ((_)_   ((_) 
| '_ \ | |  / _` | | |  | || | / _` | (_-< / _` | | '_| 
|_.__/ |_|  \__,_| |_|   \_, | \__,_| /__/ \__,_| |_|   
                         |__/                           

"""


from scipy import integrate
dir(integrate)
help(integrate.quad)


import scipy.integrate as integrate
import scipy.special as special
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
result# (1.1178179380783253, 7.866317250224184e-09)


from numpy import sqrt, sin, cos, pi
I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) +
                sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])# 1.117817938088701
                


print(abs(result[0]-I))# 1.03761443881e-11



from scipy.integrate import quad
def integrand(x, a, b):
    return a*x**2 + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
I# (1.6666666666666667, 1.8503717077085944e-14)




from scipy.integrate import quad
def integrand(t, n, x):
    return np.exp(-x*t) / t**ndef expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]vec_expint = np.vectorize(expint)
vec_expint(3, np.arange(1.0, 4.0, 0.5))# array([ 0.1097,  0.0567,  0.0301,  0.0163,  0.0089,  0.0049])



from scipy.integrate import quad, dblquad
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)print(I(4))
# (0.2500000000043577, 1.29830334693681e-08)print(I(3))
# (0.33333333325010883, 1.3888461883425516e-08)print(I(2))
# (0.4999999999985751, 1.3894083651858995e-08)



from scipy.integrate import dblquad
area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)area# (0.010416666666666668, 1.1564823173178715e-16)



from scipy import integrate
N = 5
def f(t, x):
   return np.exp(-x*t) / t**N

integrate.nquad(f, [[1, np.inf],[0, np.inf]])# (0.20000000000002294, 1.2239614263187945e-08)



from scipy import integrate
def f(x, y):
    return x*y

def bounds_y():
    return [0, 0.5]

def bounds_x(y):
    return [0, 1-2*y]

integrate.nquad(f, [bounds_x, bounds_y])# (0.010416666666666668, 4.101620128472366e-1


