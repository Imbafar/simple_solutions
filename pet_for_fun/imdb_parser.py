from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'


def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movietag = soup.select('td.titleColumn')
    for i in range(20):
        movietagi = movietag[i].text.split()
        print(' '.join(movietagi))


if __name__ == '__main__':
    main()
