# Movie Recommender App 🎬

## Description
The **Movie Recommender App** uses <b>content-based filtering<b> to recommend movies to users. By analyzing a selected movie's title, the app finds similar movies based on plot descriptions and other related features. The app uses the OMDB API to fetch detailed information about each movie, including its plot, poster, and genres.

## Features
- **Content-Based Recommendations**: The app recommends movies that are similar to the one you select based on its content (plot).
- **Movie Details**: Fetches and displays detailed information about each movie including plot, poster, and genres.
- **Interactive Interface**: Built using **Streamlit**, it allows users to interactively select movies and get recommendations in real-time.

## Technologies Used
- **Python**
- **Streamlit**
- **OMDB API**
- **Pandas**
- **matplotlib**
- **sklearn**
- **wordcloud**
- **re**
- **nltk**

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-recommender-app.git
    cd movie-recommender-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `config.json` file with your OMDB API key:

    ```json
    {
      "OMDB_API_KEY": "your_omdb_api_key"
    }
    ```

5. Run the app:

    ```bash
    python preprocess.py
    streamlit run app.py
    ```

Your browser should open with the app running. You can now start selecting movies and receiving recommendations.

## How It Works

1. **Movie Selection**: The user selects a movie from a list of available titles.
2. **Recommendation**: Once a movie is selected, the app recommends movies with similar plots by using the content-based filtering approach.
3. **Movie Details**: For each recommended movie, the app displays detailed information, including the plot, poster, and genres.

### OMDB API Integration
The app uses the **OMDB API** to fetch detailed movie information, including:
- **Plot**: The storyline of the movie.
- **Poster**: An image of the movie poster.
- **Genres**: The genre(s) of the movie.
