
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


print(3,4,5,6,7,8,9)
#sep parametresi sayesinde değerlerin arasına nokta konuyor.
print(3,4,5,6,7,8,9,sep = ".")
#  3.4.5.6.7.8.9



name = "Python'ist"
print("Merhaba, %s." % name)
#Merhaba, Python'ist


name = "Python'ist"
age = 23
"Ben, %s.  %s. yasındayım" % (name, age)
#"Ben, Python'ist.  23. yasındayım"


name = "Python'ist"
age = 23
print("Ben, {1} {0} yasındayım".format(age,name))
#Ben, Python'ist 23 yasındayım


person = {'name': 'Python\'ist', 'age': 23}
print("Merhaba, {name}. Sen {age} yasındasın.".format(name=person['name'], age=person['age']))
# "Merhaba, Python'ist. Sen 23 yasındasın."


name = "Python'ist"
age = 23
print(f"Merhaba, {name}. Sen {age} yasındasın.")
#Merhaba, Python'ist. Sen 23 yasındasın.


print(f”{2 * 7}”)
#14


def to_lowercase(input):
    return input.lower()
name = "PYTHON MU,"
print(f"{to_lowercase(name)} çok eğlenceli.")
#python mu, çok eğlenceli.







class Art:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = agedef __str__(self):
        return f"{self.first_name} {self.last_name} in yasi {self.age}."def __repr__(self):
        return f"{self.first_name} {self.last_name}  isn yasi {self.age}. Gercekten Muhtesem!"new_Art = Art("HALUK", "BİLGİNER", "65")
print(f"{new_Art}")
#HALUK BİLGİNER in yasi 65.
print(f"{new_Art!r}")
#HALUK BİLGİNER  isn yasi 65. Gercekten Muhtesem!



name = "Haluk Bilginer"
profession = "Sanatci'sın"
dizi = "Sahsiyet"
message = (
     f"Merhaba {name}. "
     f"Sen  {profession}. "
     f"En son {dizi} te mi oynadın ."
 )
print(message)
#Merhaba Haluk Bilginer. Sen  Sanatci'sın. En son Sahsiyet te mi oynadın


message = f"""
     Merhaba {name}. 
     Sen  {profession}. 
     En son {dizi} te mi oynadın .
     """
print(message)out:"""
    Merhaba Haluk Bilginer. 
    Sen  Sanatci'sın. 
    En son Sahsiyet te mi oynadın .
"""


>>> import timeit
>>> timeit.timeit("""name = "Eric"
... age = 74
... '%s is %s.' % (name, age)""", number = 10000)
#0.004875700000411598>>> import timeit
>>> timeit.timeit("""name = "Eric"
... age = 74
... '{} is {}.'.format(name, age)""", number = 10000)
# 0.003962400000091293
>>> import timeit
>>> timeit.timeit("""name = "Eric"
... age = 74
... f'{name} is {age}.'""", number = 10000)
#0.0020402000000103726


>>> def foo():
...   return 20
...
>>> f'result={foo()}'
#'result=20'

