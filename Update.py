# Read website

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

pd.set_option('display.max_colwidth', 500)


def latestVersion():
    page = requests.get("https://files.teamspeak-services.com/releases/server")
    soup = bs(page.content, features="html.parser")
    version = [i.text for i in soup.find_all('a', href=True)]
    version.remove('../')
    return version


# final = 0
# i = 0
# val1 = latestVersion()[0]
# val2 = latestVersion()[1]
#
# while final == 0:
#     if val1 > val2:
#         i += 1
#         val1 = latestVersion()[i]
#     else:

final = 0
x = 0
y = 1

while final == 0:
    if latestVersion()[y] > latestVersion()[x]:
        print(True)
    else:
        print(False)

# index = getVersion().index("3.13.1")

print(type(latestVersion()[0]))
print(latestVersion()[0:11])
