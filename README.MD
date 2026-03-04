# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and Streamlit.  
The app suggests similar movies based on textual features and enriches results with posters and metadata fetched from the OMDb API.

🔗 **Live App:**  
https://movie-recommendation-system-iq8oj3r66zmgngu8qfwx45.streamlit.app/

---

## 📌 Features

- Content-based movie recommendations
- Similarity computed using text vectorization and cosine similarity
- Movie posters fetched dynamically using OMDb API
- Additional metadata such as:
  - Release year
  - IMDb rating
  - Genre
  - Plot summary
- Clean and simple Streamlit UI
- Deployed on Streamlit Cloud

---

## 🧠 How It Works

1. Movies are represented using a **tags** column (combined textual features).
2. Text data is vectorized using **CountVectorizer**.
3. **Cosine similarity** is computed at runtime to find similar movies.
4. For each recommended movie:
   - Poster and metadata are fetched using the OMDb API.
5. Results are displayed vertically for better readability.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- requests
- OMDb API

---

