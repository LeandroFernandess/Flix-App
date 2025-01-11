"""
Este módulo define a classe GenreRepository para interagir com uma API
de gerenciamento de gêneros de filmes. Inclui métodos para obter e criar gêneros.
"""

import streamlit as st
import requests
from login.service import logout


class GenreRepository:
    """Classe responsável por acessar a API de gêneros de filmes."""

    def __init__(self):
        """Inicializa os atributos URLs base e de gêneros, e o cabeçalho da requisição."""
        self.__base_url = "https://LeandroFF.pythonanywhere.com/api/v1/"
        self.__genre_url = f"{self.__base_url}genres/"
        self.__headers = {"Authorization": f"Bearer {st.session_state.token}"}

    def get_genres(self):
        """Obtém a lista de gêneros da API.

        Retorna:
            list: Uma lista de gêneros se a requisição for bem-sucedida.
            None: Se o token for inválido e o usuário for deslogado.

        Lança:
            Exception: Se houver erro ao obter os dados da API com status diferente de 200 ou 401.
        """
        response = requests.get(self.__genre_url, headers=self.__headers)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None

        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_genre(self, genre):
        """Cria um novo gênero na API.

        Args:
            genre (dict): Dados do gênero a ser criado.

        Retorna:
            dict: Os dados do gênero criado se a requisição for bem-sucedida.
            None: Se o token for inválido e o usuário for deslogado.

        Lança:
            Exception: Se houver erro ao criar o gênero com status diferente de 201 ou 401.
        """
        response = requests.post(self.__genre_url, data=genre, headers=self.__headers)

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            logout()
            return None

        raise Exception(f"Erro ao criar gênero. Status code: {response.status_code}")
