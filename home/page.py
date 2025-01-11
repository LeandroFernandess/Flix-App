"""
Este módulo exibe estatísticas de filmes utilizando Streamlit e Plotly.
As estatísticas incluem total de filmes, filmes por gênero, total de avaliações,
e média de avaliações por filme.
"""

import streamlit as st
from movies.service import MovieService
import plotly.express as px


def show_home():
    """
    Exibe a página inicial com estatísticas de filmes.

    Usa o serviço de filmes para obter dados e os apresenta através de
    gráficos e texto usando Streamlit.
    """
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title("Estatísticas de filmes")

    if len(movie_stats["movies_by_genre"]) > 0:
        st.subheader("Filmes por Gênero")
        fig = px.pie(
            movie_stats["movies_by_genre"],
            values="count",
            names="genre__name",
            title="Filmes por Gênero",
        )
        st.plotly_chart(fig)

    st.subheader("Total de Filmes Cadastrados:")
    st.write(movie_stats["total_movies"])

    st.subheader("Quantidade de filmes por Gênero:")
    for genre in movie_stats["movies_by_genre"]:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader("Total de Avaliações Cadastradas:")
    st.write(movie_stats["total_reviews"])

    st.subheader("Média de Avaliações por Filme:")
    st.write(movie_stats["average_stars"])
