from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(5, input_dim=4, activation='relu'))
model.add(Dense(5, activation='sigmoid'))
model.add(Dense(5, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

from keras.utils.vis_utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)



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


import networkx as nx 
import matplotlib.pyplot as pltg = nx.Graph()# giris katmanı
g = nx.Graph()# giris katmanı
g.add_edge(1, 11)
g.add_edge(1, 12)
g.add_edge(1, 13)
g.add_edge(1, 14)
g.add_edge(1, 15)g.add_edge(2, 11)
g.add_edge(2, 12)
g.add_edge(2, 13)
g.add_edge(2, 14)
g.add_edge(2, 15)g.add_edge(3, 11)
g.add_edge(3, 12)
g.add_edge(3, 13)
g.add_edge(3, 14)
g.add_edge(3, 15)g.add_edge(4, 11)
g.add_edge(4, 12)
g.add_edge(4, 13)
g.add_edge(4, 14)
g.add_edge(4, 15)g.add_edge(5, 11)
g.add_edge(5, 12)
g.add_edge(5, 13)
g.add_edge(5, 14)
g.add_edge(5, 15)# 1.gizli katman
g.add_edge(11, 21) 
g.add_edge(11, 22) 
g.add_edge(11, 23) 
g.add_edge(11, 24) 
g.add_edge(11, 25)g.add_edge(12, 21) 
g.add_edge(12, 22) 
g.add_edge(12, 23) 
g.add_edge(12, 24) 
g.add_edge(12, 25)g.add_edge(13, 21) 
g.add_edge(13, 22) 
g.add_edge(13, 23) 
g.add_edge(13, 24) 
g.add_edge(13, 25)g.add_edge(14, 21) 
g.add_edge(14, 22) 
g.add_edge(14, 23) 
g.add_edge(14, 24) 
g.add_edge(14, 25)g.add_edge(15, 21) 
g.add_edge(15, 22) 
g.add_edge(15, 23) 
g.add_edge(15, 24) 
g.add_edge(15, 25)# 2.gizli katman
g.add_edge(21, 31) 
g.add_edge(21, 32) 
g.add_edge(21, 33) 
g.add_edge(21, 34) 
g.add_edge(21, 35)g.add_edge(22, 31) 
g.add_edge(22, 32) 
g.add_edge(22, 33) 
g.add_edge(22, 34) 
g.add_edge(22, 35)g.add_edge(23, 31) 
g.add_edge(23, 32) 
g.add_edge(23, 33) 
g.add_edge(23, 34) 
g.add_edge(23, 35)g.add_edge(24, 31) 
g.add_edge(24, 32) 
g.add_edge(24, 33) 
g.add_edge(24, 34) 
g.add_edge(24, 35)g.add_edge(25, 31) 
g.add_edge(25, 32) 
g.add_edge(25, 33) 
g.add_edge(25, 34) 
g.add_edge(25, 35)# Çıkış Katmanı
g.add_edge(31,41) 
g.add_edge(32,41) 
g.add_edge(33,41) 
g.add_edge(34,41) 
g.add_edge(35,41)g.add_edge(31, 41) 
g.add_edge(32, 41) 
g.add_edge(33, 41) 
g.add_edge(34, 41) 
g.add_edge(35, 41)g.add_edge(31, 41) 
g.add_edge(32, 41) 
g.add_edge(33, 41) 
g.add_edge(34, 41) 
g.add_edge(35, 41)g.add_edge(31, 41) 
g.add_edge(32, 41) 
g.add_edge(33, 41) 
g.add_edge(34, 41) 
g.add_edge(35, 41)g.add_edge(31, 41) 
g.add_edge(32, 41) 
g.add_edge(33, 41) 
g.add_edge(34, 41) 
g.add_edge(35, 41)# ağı çizmek için
nx.draw_circular(g, with_labels = True) 
plt.show()







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





digraph G {                                                       rankdir=LR                        splines=line                                                              node [fixedsize=true, label=""];                                                       subgraph cluster_0 {                         color=white;                         node [style=solid,color=blue4, shape=circle];                         x1 x2 x3;                         label = "layer 1 (Input layer)";                        }                                                subgraph cluster_1 {                         color=white;                         node [style=solid,color=red2, shape=circle];                         a12 a22 a32;                         label = "layer 2 (hidden layer)";                        }                                                subgraph cluster_2 {                         color=white;                         node [style=solid,color=seagreen2, shape=circle];                         O;                         label="layer 3 (output layer)";                        }                                                       x1 -> a12;                               x1 -> a22;                               x1 -> a32;                               x2 -> a12;                               x2 -> a22;                               x2 -> a32;                               x3 -> a12;                               x3 -> a22;                               x3 -> a32;                                                       a12 -> O                               a22 -> O                               a32 -> O                                               }



