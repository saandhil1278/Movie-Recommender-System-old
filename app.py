import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import io

#here my dataframe(new_df=movies) name is movies


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f745c4fb8a9923f640ee22ca829b301a&language=en-US'.format(movie_id))
    data = response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=f745c4fb8a9923f640ee22ca829b301a&language=en-US'.format(movie_id))
    return " https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'What are the movies you recommend',
 movies['title'].values
)

if st.button('Recommend'):



    # Assuming you have two lists: movie_names and movie_posters



    movie_names, movie_posters = recommend(selected_movie_name)

    # Create five columns using st.columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display name and poster in each column
    with col1:
        st.write(movie_names[0])
        response = requests.get(movie_posters[0])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col2:
        st.write(movie_names[1])
        response = requests.get(movie_posters[1])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col3:
        st.write(movie_names[2])
        response = requests.get(movie_posters[2])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col4:
        st.write(movie_names[3])
        response = requests.get(movie_posters[3])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col5:
        st.write(movie_names[4])
        response = requests.get(movie_posters[4])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)
