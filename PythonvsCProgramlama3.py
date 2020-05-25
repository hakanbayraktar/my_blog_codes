
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


import collections
Kisi = collections.namedtuple('Kisi', 'isim yas cinsiyet')
print ('Kisi tipi:', type(Kisi),"\n")birincikisi = Kisi(isim='Ahmet', yas=30, cinsiyet='erkek')
print(birincikisi,"\n")ikincikisi = Kisi(isim='Fatma', yas=29, cinsiyet='kadın')
print('İkinci kisinin ismi:', ikincikisi.isim)
print('İkinci kisinin ismi:', ikincikisi.yas)
print('İkinci kisinin ismi:', ikincikisi.cinsiyet)
# Kisi tipi: <class 'type'># Kisi(isim='Ahmet', yas=30, cinsiyet='erkek')# İkinci kisinin ismi: Fatma
# İkinci kisinin ismi: 29
# İkinci kisinin ismi: kadın





#include <stdio.h>struct Date {
            int day, month, year;
            } ;
int main()
{
    struct Date x = { 03, 02, 2020} ;
    struct Date y = { 10} ;
    printf( "Structure:x %d/%d/%d\n", x.day, x.month, x.year);
    printf( "Structure:y %d/%d/%d\n", y.day, y.month, y.year);
    return 0;
}// Structure:x 3/2/2020
// Structure:y 10/0/0





def swap(x, y):
    s = x < y
    return x * s + y * (1 - s), y * s + x * (1 - s)print(swap(3, 15), swap(15, 3))
print(swap(-13, 5), swap(5, -13))
# (3, 15) (3, 15)
# (-13, 5) (-13, 5)



#include <stdio.h>void swap(int *x, int *y) {
    int u = *x, v = *y;
    int s = (u - v) << (sizeof(int) * 8 - 1);
    *x = v * (1 + s) - u * s;
    *y = u * (1 + s) - v * s;
}int main()
{
    int a = 13, b = -5; 
    swap( &a , &b) ;
    printf( "a = %d\n b = %d\n", a, b);
    return 0;
}
// a = -5 
// b =  13


