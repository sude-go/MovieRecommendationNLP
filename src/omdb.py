import requests


def get_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    res = requests.get(url).json()

    if res.get("Response") == "True":
        plot = res.get("Plot", "N/A")
        poster = res.get("Poster", "N/A")
        genres = res.get("Genre", "N/A")  # Extract genres

        return plot, poster, genres  # Return plot, poster, and genres

    return "N/A", "N/A", "N/A"  # Return N/A for all if the movie is not found
