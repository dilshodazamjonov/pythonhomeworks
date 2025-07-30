import requests
import random


# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

API_KEY = 'c1d6d5594713c4801b2bb915c8fa5343'

while True:
    city = input('Enter a city to get weather info (or type "exit" to quit): ')
    if city.lower() == "exit":
        print("Goodbye!")
        break

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}\n")
    else:
        print(f"Error {response.status_code}: Could not retrieve weather for '{city}'.\n")

# ## Task 2: Movie Recommendation System
#    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

API_KEY_MOVIE = 'd25fc28c9e14f69a59db14e52c4eaebd'
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY_MOVIE}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json()['genres']
        return {g['name'].lower(): g['id'] for g in genres}
    else:
        print("Error fetching genres:", response.status_code)
        return {}
    

def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY_MOVIE,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": random.randint(1, 5)  # Random page for variety
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print("Error fetching movies:", response.status_code)
        return []

def recommend_movie():
    genres = get_genres()
    if not genres:
        return
    
    while True:
        user_input = input("Enter a genre (or type 'exit' to quit): ").lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        if user_input not in genres:
            print("Invalid genre. Available genres:", ", ".join(genres.keys()))
            continue
        
        movies = get_movies_by_genre(genres[user_input])
        if movies:
            movie = random.choice(movies)
            print(f"\n🎬 Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}\n")
        else:
            print("No movies found for that genre.")

recommend_movie()