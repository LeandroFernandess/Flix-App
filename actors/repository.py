"""
Este módulo define a classe ActorRepository, que interage com uma API para 
recuperar e cadastrar informações de atores/atrizes.
"""

import requests
import streamlit as st
from login.service import logout


class ActorRepository:
    """Repositório para gerenciar interações com uma API de atores."""

    def __init__(self):
        """Inicializa o repositório com URLs de base e headers necessários."""
        self.__base_url = "https://LeandroFF.pythonanywhere.com/api/v1/"
        self.__actors_url = f"{self.__base_url}actors/"
        self.__headers = {"Authorization": f"Bearer {st.session_state.token}"}

    def get_actors(self):
        """Obtém a lista de atores da API.

        Retorna:
            list: Lista de atores/atrizes se a requisição for bem-sucedida.

        Lança:
            Exception: Se ocorrer um erro com a requisição que não é tratado
                       por logout.
        """
        response = requests.get(self.__actors_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_actor(self, actor):
        """Cadastra um novo ator/atriz via API.

        Args:
            actor (dict): Dados do ator/atriz a serem cadastrados.

        Retorna:
            dict: Dados do ator/atriz cadastrado se a requisição for bem-sucedida.

        Lança:
            Exception: Se ocorrer um erro com a requisição que não é tratado
                       por logout.
        """
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao cadastrar dados na API. Status code: {response.status_code}"
        )
