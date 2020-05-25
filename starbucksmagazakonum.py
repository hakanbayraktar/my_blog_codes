
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



import folium
map1 = folium.Map(location=[36.8, 30.7],
                    zoom_start = 10)
map1



import folium
map1 = folium.Map(location=[36.8, 30.7],
                    zoom_start = 10)

df = pd.read_csv("/kaggle/input/store-locations/directory.csv")
df.head()

df = df[(df['Country'] == "TR")]
df.head()



# Plotting a bar graph of the number of stores in each city, for the first ten cities listed
# in the column 'City'
city_count  = df['City'].value_counts()
city_count = city_count[:10,]
plt.figure(figsize=(10,5))
sns.barplot(city_count.index, city_count.values, alpha=0.8)
plt.title('Starbucks İlk 10 Sehir')
plt.ylabel('Mağaza sayisi', fontsize=12)
plt.xlabel('Sehir', fontsize=12)
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


import foliumm = folium.Map(location=[39.92,32.854], control_scale=True, zoom_start=7,attr = "text some")
df_copy = df.copy()
for i in range(0,len(df_copy)):    html="""
    <h4> ADRES: </h4>""" + str( df_copy.iloc[i]['Street Address'])    
    iframe = folium.IFrame(html=html, width=150, height=250)
    popup = folium.Popup(iframe)folium.Marker(
    location=[df_copy.iloc[i]['Latitude'], df_copy.iloc[i]['Longitude']],
    popup=popup,
    tooltip=str(df_copy.iloc[i]['City']),
    icon=folium.Icon(color='lightblue',icon='medkit',prefix="fa"),
    ).add_to(m)
m





