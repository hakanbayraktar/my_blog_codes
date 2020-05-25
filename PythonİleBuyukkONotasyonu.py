
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


import numpy as np
from math import log
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
print(plt.style.available)


n = np.linspace(1,30)
labels = ["Constant-1","Logarithmic-logn","Linear-n","LogLinear-nlogn","Quadratic-n^2","Cubic-n^3","Exponential-2^n"]
big_o = [np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,n**3,2**n]


plt.figure(figsize=(12,10))
plt.ylim(0,50)


for i in range(len(big_o)):
    plt.plot(n,big_o[i], label = labels[i])
    
    
plt.ylabel("RelativeRuntime")
plt.xlabel("n")
plt.show()
