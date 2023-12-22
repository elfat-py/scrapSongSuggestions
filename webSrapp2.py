from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://songslikex.com/songs-like/3RbNcjVnQixKa1sULcwd2K/title%3DLosing%20Interest/artists%3DStract%2C%20Shiloh%20Dynasty?listId=7nz3O4oW1EX9XvKMx6FrIx&searched=losing+inte&source=main_page').text
soup = BeautifulSoup(html_text, 'lxml')

lists = soup.find_all('table', class_='trackList table full')
# Assuming 'soup' is your BeautifulSoup object and 'lists' contains the desired 'table' elements
for table in lists:
    tbody = table.find('tbody')  # Find the 'tbody' element within the 'table'

    if tbody:  # Check if 'tbody' is found
        tr_elements = tbody.find_all('tr')  # Find all 'tr' elements within 'tbody'

        for tr in tr_elements:
            titles_td = tr.find('td').find('button')
           # print(titles_td)
            if titles_td:
                title = titles_td.get('title')
                print(title)
            # for button in titles_td:
            #     buttons = tr.find('button')
            # # if title_td:
            # #     title = title_td.text.strip()
            # #     print(title)
            #     title = button['title']



