
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



height = [1.63, 1.68, 1.71, 1.89, 1.79]
weight = [65.3, 59.4, 76.5, 78.5, 68.7]
>>> weight
[65.3, 59.4, 76.5, 78.5, 68.7]
>>> height
[1.63, 1.68, 1.71, 1.89, 1.79]



>>> weight / height **2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'




import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)


>>> np_weight / np.array(height) ** 2

array([24.57751515, 21.04591837, 26.16189597, 21.97586854, 21.44127836])

