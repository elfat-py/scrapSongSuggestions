from bs4 import BeautifulSoup
import requests


# html_text = requests.get('https://songslikex.com/songs-like/3RbNcjVnQixKa1sULcwd2K/title%3DLosing%20Interest/artists%3DStract%2C%20Shiloh%20Dynasty?listId=7nz3O4oW1EX9XvKMx6FrIx&searched=losing+inte&source=main_page').text
# soup = BeautifulSoup(html_text, 'lxml')
#
# lists = soup.find_all('table', class_='trackList table full')
# # Assuming 'soup' is your BeautifulSoup object and 'lists' contains the desired 'table' elements
# for table in lists:
#     tbody = table.find('tbody')  # Find the 'tbody' element within the 'table'
#
#     if tbody:  # Check if 'tbody' is found
#         tr_elements = tbody.find_all('tr')  # Find all 'tr' elements within 'tbody'
#
#         for tr in tr_elements:
#             titles_td = tr.find('td').find('button')
#            # print(titles_td)
#             if titles_td:
#                 title = titles_td.get('title')
#                 print(title)

htmlHomePage = requests.get("https://songslikex.com/").text
soup = BeautifulSoup(htmlHomePage, 'lxml')


full_body = soup.find_all('div', class_='full')
#print(full_body)

#fullCenter = full_body.find('div', class_='m-b full center')

for content in full_body:
    fullCenter = content.find_all('div', class_='m-b-m full center')
    for button in fullCenter:
        searchButton = button.find(id='songSearchForm')
        if searchButton:
            searchPlace = searchButton.find('div', class_='async-search')
            if searchPlace:
                inputElement = searchPlace.find('input', id='songSearch')
                inputElement['value'] = 'Losing interest'  # Here we will pass the user input
                print(f"The updated value: {inputElement['value']}")

        # for searchPlaceHolder in searchButton:
        #     searchPlace = searchPlaceHolder.find('div', class_='async-search')
        #     print(searchPlace)


searching = soup.find(id='SongSearchForm')
#print(searching)



   # print(full_body)










# print(full_body)
# searchButtons = soup.find_all('div', class_='m-b full center')
# #print(searchButton)
# for searchButton in searchButtons:
#     print(searchButton)