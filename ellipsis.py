
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


import numpy as npn = np.arange(16).reshape(2,2,2,2)
print(n)


import numpy as np
n = np.arange(16).reshape(2,2,2,2)
print(n[1:,1])



import numpy as np
n = np.arange(16).reshape(2,2,2,2)
print(n[1,...,1])



import numpy as np
n = np.arange(16).reshape(2,2,2,2)
print(n[1,Ellipsis,1])



from numpy import arange
a = arange(16).reshape(2,2,2,2)
print(a[..., 0].flatten())
print(a[:,:,:,0].flatten())

