
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


import datetimet = datetime.datetime.today()
print(f'{t}')# 2020-01-16 22:08:45.310966


#include <stdio.h>
#include <time.h>int main()
{
    time_t timer;
    char buffer[26];
    struct tm* tm_info;    timer = time(NULL);
    tm_info = localtime(&timer);
    strftime(buffer, 26, "%Y-%m-%d %H:%M:%S", tm_info);
    puts(buffer);return 0;
}// 2020-01-16 22:16:52



x = 251
print("The decimal value of", x, "is:")
print( bin(x) ,  "in binary.")
print( oct(x) ,  "in octal.")
print( hex(x) ,  "in hexadecimal.")# The decimal value of 251 is:
# 0b11111011 in binary.
# 0o373 in octal.
# 0xfb in hexadecimal.




#include <stdio.h>
int main()
{
 unsigned int u = 57054; printf( "u = %u \n ", u) ; 
 printf( "u = %o \n ", u) ; 
 printf( "u = %X \n ", u) ;  return 0;
}// u = 57054
// u = 157336
// u = DEDE





return albatross # doğru 
return(albatross) # yanlıs


return albatross; // correct
return(albatross); // incorrect 

