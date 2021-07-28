import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
response = requests.get('https://tlauncher.org/ru/mods_2/', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')


# metod 1.a
b_right_menu = soup.find("div", class_ = "wrapper-archive")
b_menu = b_right_menu.find_all("article", class_ = "b-anons clearfix")
for menu in b_menu:
    print("\033[36m {}" .format(menu.h2.text))
    print("\033[37m {}" .format(menu.p.text), "\n")


# metod 1.b
# b_right_menu = soup.find("ul", class_ = "ez-toc-list ez-toc-list-level-1").find_all("title").text
# print(b_right_menu)
