"""
Este módulo define a classe MovieService, que fornece métodos para
interagir com filmes, utilizando o MovieRepository para acessar a API.
Utiliza o Streamlit para gerenciar o estado da sessão.
"""

import streamlit as st
from movies.repository import MovieRepository


class MovieService:
    """
    Serviço para gerenciar filmes, fornecendo métodos para
    recuperar filmes, criar novos e obter estatísticas de filmes.
    """

    def __init__(self):
        """Inicializa o MovieService com uma instância de MovieRepository."""
        self.movie_repository = MovieRepository()

    def get_movies(self):
        """
        Obtém a lista de filmes, recuperando-a do estado da sessão
        se já estiver disponível, ou da API, se necessário.

        Returns:
            list: Lista de filmes armazenados no estado da sessão
            ou obtidos da API.
        """
        if "movies" in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, actors, resume):
        """
        Cria um novo filme e o adiciona ao estado da sessão.

        Args:
            title (str): Título do filme.
            release_date (str): Data de lançamento do filme.
            genre (str): Gênero do filme.
            actors (list): Lista de atores do filme.
            resume (str): Resumo do filme.

        Returns:
            dict: O novo filme criado.
        """
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        new_movie = self.movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        """
        Obtém estatísticas dos filmes.

        Returns:
            dict: Estatísticas dos filmes.
        """
        return self.movie_repository.get_movies_stats()
