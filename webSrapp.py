from bs4 import BeautifulSoup
import requests


session = requests.Session()
song = 'losing interest'  # This should be the AI song response
INITIALLINK = 'https://songslikex.com/'
URLSEARCHVALUE = f"{INITIALLINK}?song={song}"

htmlHomePage = requests.get(URLSEARCHVALUE).text
soup = BeautifulSoup(htmlHomePage, 'lxml')


def findSearchBar(userInput):
    list_song_suggestions = []
    full_body = soup.find_all('div', class_='full')
    for content in full_body:
        fullCenter = content.find_all('div', class_='m-b-m full center')
        for button in fullCenter:
            searchButton = button.find(id='songSearchForm')
            if searchButton:
                searchPlace = searchButton.find('div', class_='async-search')
                if searchPlace:
                    inputElement = searchPlace.find('input', id='songSearch')
                    inputElement['value'] = userInput  # Here we will pass the user input
                    #print(inputElement)
                    #print(f"The updated value: {inputElement['value']}")
                    if inputElement['value'] == userInput:
                        for songSuggest in fullCenter:
                            songSuggestionsList = songSuggest.find_all('ul', class_='song-results left pad-m')
                            if songSuggestionsList:
                                for songList in songSuggestionsList:
                                    songs = songList.find_all('li', class_='song')
                                    for songElement in songs:
                                        title_tag = songElement.find_all('a')
                                        for songTitleA in title_tag:
                                            title_tag = songTitleA.get('href')
                                            list_song_suggestions.append(title_tag)
    return list_song_suggestions

list_suggestions = findSearchBar(song)
first_suggestion = list_suggestions[0]
linkHeader = INITIALLINK[:-1] + first_suggestion # We are using slicing since the last char is: / and it gets doubled

#print(linkHeader)
websiteResponse = session.get(linkHeader)


responseHtml = websiteResponse.text
suggestion_soup = BeautifulSoup(responseHtml, 'html.parser')
#print(suggestion_soup)


def resultsFromResponse(responseLink):  # This method returns a list of songs each of which is similar to the one provided
    songs_list =[]
    html_text = session.get(responseLink).text  # previously it was:  requests.get
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
                    songs_list = title[15:]
                    print(title[15:])  # SHOULD BE REMOVED ONCE NOT NEEDED
    return songs_list



listOfSongRecommendation = resultsFromResponse(linkHeader)

