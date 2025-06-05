import requests
from colorama import init, Fore, Back, Style
import json
import os
from dotenv import load_dotenv
import time

try:
    init()

    load_dotenv()

    key = os.getenv("OMDbkey")

    print(Fore.GREEN + Style.BRIGHT + "Welcome to my movie lookup project - Just look up a movie name and it will find matching results")
    print()
    searchFor = input("What movie are you looking for?: " + Style.RESET_ALL)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "Now searching results for " + Fore.RESET + Fore.BLACK + searchFor + Style.RESET_ALL)

    url = "http://www.omdbapi.com/"
    params = {
        "apikey": key,
        "s": searchFor
    }

    response = requests.get(url, params=params)
    data = response.json()

    title1 = (data['Search'][0]['Title'])
    year1 = (data['Search'][0]['Year'])
    type1 = (data['Search'][0]['Type'])

    title2 = (data['Search'][1]['Title'])
    year2 = (data['Search'][1]['Year'])
    type2 = (data['Search'][1]['Type'])

    title3 = (data['Search'][2]['Title'])
    year3 = (data['Search'][2]['Year'])
    type3 = (data['Search'][2]['Type'])

    title4 = (data['Search'][3]['Title'])
    year4 = (data['Search'][3]['Year'])
    type4 = (data['Search'][3]['Type'])

    title5 = (data['Search'][4]['Title'])
    year5 = (data['Search'][4]['Year'])
    type5 = (data['Search'][4]['Type'])

    time.sleep(1)
    print()
    print(Fore.GREEN + Style.BRIGHT + "-----Here are the top 5 results for " + Fore.RESET + Fore.BLACK + searchFor + Fore.RESET + Fore.GREEN + "-----" + Style.RESET_ALL)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + title1 + " | " + year1 + " | " + type1)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + title2 + " | " + year2 + " | " + type2)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + title3 + " | " + year3 + " | " + type3)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + title4 + " | " + year4 + " | " + type4)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + title5 + " | " + year5 + " | " + type5 + Style.RESET_ALL)

except KeyError as e:
    print(Fore.RED + Style.BRIGHT + "Could not find results for " + Fore.RESET + Fore.BLACK + searchFor)