"""
Este módulo exibe uma interface de usuário para listar filmes existentes
e cadastrar novos filmes, utilizando serviços para acessar dados de filmes,
gêneros e atores. Utiliza a biblioteca Streamlit para renderização.
"""

import pandas as pd
from datetime import datetime
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    """
    Exibe a lista de filmes e um formulário para cadastrar novos filmes.

    Utiliza serviços para buscar dados e interagir com o usuário
    através de componentes da interface gráfica Streamlit.
    """
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write("Lista de filmes")
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=["actors", "genre.id"])
        AgGrid(data=movies_df, reload_data=True, key="movies_grid")
    else:
        st.warning("Nenhum filme cadastrado")

    st.title("Cadastrar novo filme")
    title = st.text_input("Título")
    release_date = st.date_input(
        "Data de lançamento",
        value=datetime.now(),
        min_value=datetime(1900, 1, 1),
        max_value=datetime.now(),
        format="DD/MM/YYYY",
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre["name"]: genre["id"] for genre in genres}
    selected_genre_name = st.selectbox("Gênero", list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor["name"]: actor["id"] for actor in actors}
    selected_actors_name = st.multiselect("Atores/Atrizes", list(actor_names.keys()))
    selected_actors_ids = [
        actor_names[actor_name] for actor_name in selected_actors_name
    ]

    resume = st.text_area("Resumo", max_chars=500)

    if st.button("Cadastrar"):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.success("Filme cadastrado com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao cadastrar filme")
