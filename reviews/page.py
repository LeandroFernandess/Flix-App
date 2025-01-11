"""
Este módulo permite exibir e cadastrar avaliações de filmes usando Streamlit. Ele
exibe uma lista de avaliações existentes e fornece uma interface para adicionar novas
avaliações.
"""

import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
import pandas as pd
from reviews.service import ReviewService


def show_reviews():
    """
    Exibe a lista de avaliações existentes e a interface para cadastrar novas
    avaliações de filmes. Utiliza os serviços de filmes e avaliações para obter
    dados e registrar nova avaliação.
    """
    reviews_service = ReviewService()
    reviews = reviews_service.get_reviews()

    if reviews:
        st.write("Lista de reviews")
        reviews_df = pd.json_normalize(reviews)
        AgGrid(data=reviews_df, reload_data=True, key="reviews_grid")
    else:
        st.warning("Nenhuma avaliação encontrada.")

    st.title("Cadastrar nova avaliação")

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_title = {movie["title"]: movie["id"] for movie in movies}
    selected_movie_title = st.selectbox("Filme", list(movie_title.keys()))

    stars = st.number_input("Estrelas", min_value=0, max_value=5, step=1)
    comment = st.text_area("Comentário")

    if st.button("Cadastrar"):
        new_review = reviews_service.create_review(
            movie=movie_title[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error("Erro ao cadastrar avaliação. Verifique os campos.")
