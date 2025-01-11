"""
Este módulo define a classe ReviewRepository que interage com uma API para
obter e criar avaliações de filmes. Ele utiliza a sessão do Streamlit para
autenticação através de um token.
"""

import requests
from login.service import logout
import streamlit as st


class ReviewRepository:
    """
    Uma classe para interagir com a API de avaliações de filmes, permitindo
    buscar e criar novas avaliações.
    """

    def __init__(self):
        """
        Inicializa o ReviewRepository com as URLs base e de avaliações,
        além dos cabeçalhos de autenticação.
        """
        self.__base_url = "https://LeandroFF.pythonanywhere.com/api/v1/"
        self.__reviews_url = f"{self.__base_url}reviews/"
        self.__headers = {"Authorization": f"Bearer {st.session_state.token}"}

    def get_reviews(self):
        """
        Obtém a lista de avaliações da API.

        Returns:
            list: Lista de avaliações se a solicitação for bem-sucedida.
            None: Se a autenticação falhar.

        Raises:
            Exception: Se houver um erro na solicitação à API.
        """
        response = requests.get(self.__reviews_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_review(self, review):
        """
        Cria uma nova avaliação na API.

        Args:
            review (dict): Um dicionário contendo os dados da avaliação.

        Returns:
            dict: A avaliação criada se a solicitação for bem-sucedida.
            None: Se a autenticação falhar.

        Raises:
            Exception: Se houver um erro na solicitação à API.
        """
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,
            data=review,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao cadastrar dados na API. Status code: {response.status_code}"
        )
