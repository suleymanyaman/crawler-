import requests
from bs4 import BeautifulSoup
import re

def yemekhane():
    url = 'https://kafeterya.metu.edu.tr/'
    source_code = requests.get(url)  #connect to web page and html code is stored
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    meals = soup.find_all('p')

    i=0
    for meal in meals:
        if i==1:
            print("\nÖğle Yemeği\n")

        elif i==5:
            print("\nAkşam Yemeği\n")
        meal = str(meal)
        result = re.sub("<.*?>","",meal)
        print(result)
        i+=1





    input("\nPress ENTER to exit")



yemekhane()


