import streamlit as st
import pickle
import pandas as pd

try:
    movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
except FileNotFoundError:
    st.error("Error: movies_dict.pkl file not found! Make sure it's in the same directory.")
    st.stop()

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie to get recommendations:", movies['title'].values)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


try:
    similarity = pickle.load(open("similarity.pkl", "rb"))
except FileNotFoundError:
    st.error("Error: similarity.pkl file not found! Make sure it's in the same directory.")
    st.stop()


if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for movie in recommendations:
        st.write(f"- {movie}")


