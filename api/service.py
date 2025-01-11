"""
Este módulo define a classe Auth que fornece funcionalidades para autenticação
de usuários utilizando uma API externa. O código se comunica com um endpoint
para obter um token de autenticação.
"""

import requests


class Auth:
    """Classe responsável pela autenticação de usuários através de uma API externa."""

    def __init__(self):
        """Inicializa a classe Auth com as URLs base e de autenticação."""
        self.__base_url = "https://LeandroFF.pythonanywhere.com/api/v1/"
        self.__auth_url = f"{self.__base_url}authentication/token/"

    def get_token(self, username, password):
        """Obtém o token de autenticação para um usuário específico.

        Args:
            username (str): Nome de usuário para autenticação.
            password (str): Senha do usuário para autenticação.

        Retorna:
            dict: Um dicionário com o token de autenticação ou uma mensagem de erro.
        """
        auth_payload = {"username": username, "password": password}
        auth_response = requests.post(self.__auth_url, data=auth_payload)

        if auth_response.status_code == 200:
            return auth_response.json()
        return {
            "error": f"Erro ao autenticar. Status code: {auth_response.status_code}"
        }
