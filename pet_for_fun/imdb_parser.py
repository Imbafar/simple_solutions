from bs4 import BeautifulSoup
import requests


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
url_dollar = 'https://cbr.ru/'


def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    movietag = soup.select("td.titleColumn")
    for i in range(20):
        movietagi = movietag[i].text.split()
        print(" ".join(movietagi))


def main_dollar():
    response = requests.get(url_dollar)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    dolla = soup.find_all('div', class_='col-md-2 col-xs-9 _right mono-num')
    for item in dolla:
        print(item.text.strip())
    # print(dolla)


if __name__ == "__main__":
    main_dollar()
