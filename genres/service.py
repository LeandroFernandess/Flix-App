"""
Este módulo define a classe GenreService que fornece métodos de serviço para
interagir com os gêneros, integrando-se ao front-end com o uso de Streamlit.
"""

import streamlit as st
from genres.repository import GenreRepository


class GenreService:
    """Classe de serviço para manipulação de gêneros, utilizando repositório de dados."""

    def __init__(self):
        """Inicializa o serviço com uma instância de GenreRepository."""
        self.__genre_repository = GenreRepository()

    def get_genres(self):
        """Obtém a lista de gêneros. Armazena os gêneros no estado de sessão do Streamlit.

        Retorna:
            list: Lista de gêneros obtidos do estado da sessão ou do repositório.
        """
        if "genres" in st.session_state:
            return st.session_state.genres
        genres = self.__genre_repository.get_genres()
        st.session_state.genres = genres
        return genres

    def create_genre(self, name):
        """Cria um novo gênero e atualiza o estado de sessão.

        Args:
            name (str): Nome do gênero a ser criado.

        Retorna:
            dict: O gênero recém-criado.
        """
        genre = dict(name=name)
        new_genre = self.__genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
