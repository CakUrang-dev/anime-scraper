from requests.models import ContentDecodingError
from userInput import *
# Library
from bs4 import BeautifulSoup
import requests


def find_anime(genre, counter):
    # Get Anime List from MyAnimeList
    html_text = requests.get(f"https://myanimelist.net/anime/genre/{genre}?page={counter}").text
    soup = BeautifulSoup(html_text, "lxml")
    anime_list = soup.find("div", class_="seasonal-anime-list clearfix")
    try:
        animes = anime_list.find_all("div", class_="seasonal-anime js-seasonal-anime")

        for anime in animes:
            # Get Anime Data
            # Title, Studio, Number of Episodes,Genre ,Source, Rating and Description,
            anime_title = anime.find("div", class_="title").h2.a.text
            # Solving for studio not shown
            try:
                anime_studio = anime.find("span", class_="producer").a.text
            except:
                anime_studio = "-"
                pass
            anime_episodes = anime.find("div", class_="eps").a.span.text
            anime_source = anime.find("span", class_="source").text
            anime_rating = anime.find("span", class_="score").text.replace(' ', '')
            anime_genre = anime.find_all("div", class_="genres-inner js-genre-inner")
            anime_desc = anime.find("span", class_="preline").text
            more_info = anime.find("div", class_="title").h2.a['href']

            if "?" in anime_episodes:
                anime_episodes = "On Going"

            if "N" in anime_rating:
                anime_rating = "Not rated yet"

            # Title for txt files
            text_title = anime_title.replace(':', '').replace('-', '').replace('/', '').replace('?', '').replace('"', '')
            # For list container
            genre_list = []

            # Convert html to list
            for genre in anime_genre:
                genre_list.append(genre.text.split())

            # Print Anime Data
            with open(f"animes/{text_title}.txt", "w") as a:
                a.write(f"Title: {anime_title}\n")
                a.write(f"Producer: {anime_studio}\n")
                a.write(f"Total Episodes: {anime_episodes}\n")
                a.write(f"Anime Source: {anime_source}\n")
                a.write(f"Rating: {anime_rating.strip()}\n")
                
                for genre in genre_list:
                    str_genre = ', '.join(str(i) for i in genre)
                    a.write(f"Genre: {str_genre}\n")

                a.write(f"Synopsis:\n {anime_desc}\n")
                a.write(f"More Info: {more_info}\n")
            print(f"File saved: {anime_title}")
    except AttributeError:
        print("Max Pages Reached")
        exit()

# For User Experience
condition = True
page_counter = 41

while condition:
    find_anime(genre_link, page_counter)
    
    input_user = input("Scraping next page (y/n): ")
    if input_user == "y" or input_user == "Y":
        page_counter +=1
    elif input_user == "n" or input_user == "N":
        condition = False
        print("Thank You")
    else:
        condition = False
        print("Wrong Input") 

