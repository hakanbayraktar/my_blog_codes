

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
     
     
     
 #kaggleblalyasar
df = pd.read_csv("/kaggle/input/prisoner-numbers-of-turkey-between-1998-and-2017/prisoner.csv")
df.head()


df.columns  = ["Year","TotalPrisonersers","MalePrisoners","FemalePrisoners"]
data = []
new_row = {'Year':1998, 'TotalPrisonersers':66096, 'MalePrisoners':63576, 'FemalePrisoners':2520}
data.insert(0,new_row)
df = pd.concat([pd.DataFrame(data), df], ignore_index=True)
df


df["KadınToplamaOranı%"] =df ["FemalePrisoners"] /  df["TotalPrisonersers"] *100
df["ErkekToplamaOranı%"] = df ["MalePrisoners"] / df["TotalPrisonersers"] * 100
df


