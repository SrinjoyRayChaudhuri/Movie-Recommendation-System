import pickle
import streamlit as st
import requests
from urllib.parse import quote
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


OMDB_API_KEY = "8cffa18c"


def fetch_poster(movie_title):
    movie_title = quote(movie_title)
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()

    if response.get("Poster") and response["Poster"] != "N/A":
        return response["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


def fetch_movie_details(movie_title):
    movie_title = quote(movie_title)
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()

    return {
        "Year": response.get("Year", "N/A"),
        "Genre": response.get("Genre", "N/A"),
        "imdbRating": response.get("imdbRating", "N/A"),
        "Plot": response.get("Plot", "N/A")
    }


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))

    return recommended_movie_names, recommended_movie_posters


# ================= Streamlit UI =================

st.header("Movie Recommender System")

movies = pickle.load(open("movie_list.pkl", "rb"))

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray()
similarity = cosine_similarity(vectors)

movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    for name, poster in zip(recommended_movie_names, recommended_movie_posters):
        details = fetch_movie_details(name)

        st.subheader(name)
        st.image(poster, width=300)

        st.write(f"🎬 **Year:** {details['Year']}")
        st.write(f"⭐ **IMDb Rating:** {details['imdbRating']}")
        st.write(f"🎭 **Genre:** {details['Genre']}")
        st.write(f"📝 **Plot:** {details['Plot']}")

        st.markdown("---")