from bs4 import BeautifulSoup
import requests
from csv import writer
for i in range(2, 400): # we are iterating through the different pages using loop

    url = f"https://www.bayut.com/to-rent/apartments/dubai/page-{i}/?furnishing_status=unfurnished"
    # i here is the page number, the url gets altered each time the loop runs
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('li', class_='ef447dde') 
    # the class values are for the scraping metrics
    with open('housing.csv', 'a', encoding='utf8', newline='') as f:
        # housing.csv is the file that the data will be saved into automatically
        thewriter = writer(f)
        for list in lists:
            price = list.find('span', class_='f343d9ce').text
            beds_baths_area = list.find('div', class_='_22b2f6ed').text
            address = list.find('div', class_='_7afabd84').text
            info = [price, beds_baths_area, address]
            thewriter.writerow(info)

