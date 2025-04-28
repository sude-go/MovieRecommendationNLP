import json
import streamlit as st
from recommendation import df, recommend_movies
from omdb import get_movie_details

# Check if the app is running locally or on Streamlit Cloud
if "OMDB_API_KEY" in st.secrets:
    OMDB_API_KEY = st.secrets["OMDB_API_KEY"]
else:
    # If running locally, load the config file
    with open("config.json") as config_file:
        config = json.load(config_file)
    OMDB_API_KEY = config["OMDB_API_KEY"]  # API key

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")

movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']

                plot, poster, genres = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 5])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=300)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"**Genres:** {genres}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
