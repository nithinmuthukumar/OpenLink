import webbrowser
# from bs4 import BeautifulSoup
# import requests
# response = requests.get('https://www.lightnovelpub.com/novel/reverend-insanity-10051457/chapter-1107')
# soup = BeautifulSoup(response.text, 'html.parser')
# text = soup.find_all('p')
# for tag in text:
#     print(tag.text.strip())
from time import sleep

x1 = int(input("enter the start number"))
x2 = int(input("enter the end number"))
website = "https://www.lightnovelpub.com/novel/reverend-insanity-10051457/chapter-"
#input("enter the website")

for i in range(x1,x2+1):
    webbrowser.open_new_tab(website+str(i))
    sleep(1)