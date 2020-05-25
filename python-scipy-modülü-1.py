
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


python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



from scipy import linalg, optimize
np.info(optimize.fmin)"""
fmin(func, x0, args=(), xtol=0.0001, ftol=0.0001, maxiter=None, maxfun=None,full_output=0, disp=1, retall=0, callback=None)
.....
.....
.....
"""



import numpy as np
np.some_function()



from scipy import some_module
some_module.some_function()


import numpy as np
a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
a"""
array([ 3.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -1.        , -0.77777778, -0.55555556, -0.33333333,
       -0.11111111,  0.11111111,  0.33333333,  0.55555556,  0.77777778,
        1.        ])
"""


a = np.r_[3,[0]*5,-1:1:10j]



np.mgrid[0:5,0:5]"""
array([[[0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]],
       [[0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4]]])
"""


np.mgrid[0:5:4j,0:5:4j]"""
array([[[ 0.    ,  0.    ,  0.    ,  0.    ],
        [ 1.6667,  1.6667,  1.6667,  1.6667],
        [ 3.3333,  3.3333,  3.3333,  3.3333],
        [ 5.    ,  5.    ,  5.    ,  5.    ]],
       [[ 0.    ,  1.6667,  3.3333,  5.    ],
        [ 0.    ,  1.6667,  3.3333,  5.    ],
        [ 0.    ,  1.6667,  3.3333,  5.    ],
        [ 0.    ,  1.6667,  3.3333,  5.    ]]])
"""


from numpy import poly1d
p = poly1d([3,4,5])
print(p)"""
   2
3 x + 4 x + 5
"""



from numpy import poly1d
p = poly1d([3,4,5])print(p*p)     4      3      2
# 9 x + 24 x + 46 x + 40 x + 25
####################################################################print(p.integ(k=6))
     3     2
# 1 x + 2 x + 5 x + 6

####################################################################print(p.deriv())# 6 x + 4####################################################################p([4, 5])# array([ 69, 100])



def addsubtract(a,b):
   if a > b:
       return a - b
   else:
       return a + b
       
       

vec_addsubtract = np.vectorize(addsubtract)
vec_addsubtract([0,3,6,9],[1,3,5,7])# array([1, 6, 1, 2])


x = np.arange(10)
condlist = [x<3, x>5]
choicelist = [x, x**2]
np.select(condlist, choicelist)# array([ 0,  1,  2,  0,  0,  0, 36, 49, 64, 81])


