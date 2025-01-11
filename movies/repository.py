"""
Este módulo define a classe MovieRepository, que interage com uma API
para obter, criar e fornecer estatísticas sobre filmes. Utiliza requisições
HTTP e gerencia sessões com Streamlit.
"""

import requests
import streamlit as st
from login.service import logout


class MovieRepository:
    """
    Repositório para acessar a API de filmes, permitindo operações
    de leitura, criação e obtenção de estatísticas sobre filmes.
    """

    def __init__(self):
        """Inicializa o MovieRepository com URLs e cabeçalhos de autenticação."""
        self.__base_url = "https://LeandroFF.pythonanywhere.com/api/v1/"
        self.__movies_url = f"{self.__base_url}movies/"
        self.__headers = {"Authorization": f"Bearer {st.session_state.token}"}

    def get_movies(self):
        """
        Obtém a lista de filmes da API.

        Returns:
            list: Lista de filmes se a requisição for bem-sucedida.
            None: Se a autenticação falhar e realizar logout.

        Raises:
            Exception: Se ocorrer um erro não tratado ao obter os dados.
        """
        response = requests.get(self.__movies_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_movie(self, movie):
        """
        Cria um novo filme usando a API.

        Args:
            movie (dict): Dicionário com os detalhes do filme.

        Returns:
            dict: Os dados do filme criado se a requisição for bem-sucedida.
            None: Se a autenticação falhar e realizar logout.

        Raises:
            Exception: Se ocorrer um erro não tratado ao cadastrar os dados.
        """
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao cadastrar dados na API. Status code: {response.status_code}"
        )

    def get_movies_stats(self):
        """
        Obtém estatísticas sobre os filmes da API.

        Returns:
            dict: Estatísticas dos filmes se a requisição for bem-sucedida.
            None: Se a autenticação falhar e realizar logout.

        Raises:
            Exception: Se ocorrer um erro não tratado ao obter os dados.
        """
        response = requests.get(f"{self.__movies_url}stats/", headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )
