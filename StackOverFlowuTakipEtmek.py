
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


import requests
from bs4 import BeautifulSoup

def get_html_from_web(zipcode):

    url = 'https://stackoverflow.com/questions/tagged/{}'.format(zipcode)

    response = requests.get(url)
    totalQuestionOverview = BeautifulSoup(response.content, "html.parser")
    findLinks = totalQuestionOverview.find("div", {"id": "mainbar"})
    #print(findLinks)
    findLinks = findLinks.find_all("a", {'class':"question-hyperlink"})
    #print(findLinks)

    for i in findLinks:
      print(i.text)
      print("---"*15)
      
#datascience yok :
#deeplearnıng yok :)
tag_listem = ["python"]
for i in tag_listem:
    get_html_from_web(i)
    
