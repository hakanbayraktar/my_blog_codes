
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
import pandas as pd

df = pd.DataFrame(np.random.rand(12,3,)*10, columns=list("AXD"))
df.head()


df[list("AXD")] = df[list("AXD")].astype(int)
df.head()


# df.loc[i, 'weightkglabel'] = 2  // gibi denermisin. ? 



import time
start = time.time()
for i in range(len(df['D'])):
    #print(i)
    if df.loc[i, 'D'] == 0:
        df.loc[i, 'D'] = "a"
    elif df.loc[i, 'D'] == 1:
        df.loc[i, 'D'] = "b"    
    elif df.loc[i, 'D'] == 2:
        df.loc[i, 'D'] = "c"
    elif  df.loc[i, 'D'] == 3:
        df.loc[i, 'D'] = "d"
    elif df.loc[i, 'D'] == 4 :
        df.loc[i, 'D'] = "e"
    elif df.loc[i, 'D'] == 5:
        df.loc[i, 'D'] = "f"
    elif df.loc[i, 'D'] == 6 :
        df.loc[i, 'D'] = "g"
    elif df.loc[i, 'D'] == 7:
        df.loc[i, 'D'] = "h"
    elif df.loc[i, 'D'] == 8:
        df.loc[i, 'D'] = "i"

stop = time.time()
print(stop-start)
df



import time
start = time.time()
for i in range(len(df['A'])):
    #print(i)
    if df['A'].loc[i] == 0:
        df['A'].loc[i] =  "a"
    elif df['A'].loc[i] ==  1:
        df['A'].loc[i] =  "b"
    elif df['A'].loc[i] ==  2:
        df['A'].loc[i] =  "c"
    elif df['A'].loc[i] ==  3:
        df['A'].loc[i] =  "d"
    elif df['A'].loc[i] ==  4 :
        df['A'].loc[i] =  "e"
    elif df['A'].loc[i] ==  5:
        df['A'].loc[i] = "f"
    elif df['A'].loc[i] ==  6 :
        df['A'].loc[i] =  "g"
    elif df['A'].loc[i] ==  7:
        df['A'].loc[i] = "h"
    elif df['A'].loc[i] ==  8:
        df['A'].loc[i] = "i" 
stop = time.time()
print(stop-start)
df



# enhızlısı bu :)

equal_4 = df[(df["X"] == 4)]
df.iloc[equal_4.index] = "a"
"""
...
...
"""
equal_8 = df[(df["X"]==8)]
df.iloc[equal_8.index] = "h"
df

