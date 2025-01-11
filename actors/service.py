"""
Este módulo define a classe ActorService, que fornece métodos para gerenciar
atores/atrizes. Inclui funcionalidades para recuperar a lista de atores e
cadastrar novos atores, utilizando um repositório de atores.
"""

import streamlit as st
from actors.repository import ActorRepository


class ActorService:
    """Serviço para gerenciar atores, incluindo recuperação e cadastro."""

    def __init__(self):
        """Inicializa o serviço com um repositório de atores."""
        self.actor_repository = ActorRepository()

    def get_actors(self):
        """Obtém a lista de atores.

        Retorna:
            list: Lista de atores/atrizes já carregados no estado da sessão,
            ou busca do repositório se ainda não carregados.
        """
        if "actors" in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        """Cadastra um novo ator/atriz.

        Args:
            name (str): Nome do ator/atriz.
            birthday (date): Data de nascimento.
            nationality (str): Nacionalidade do ator/atriz.

        Retorna:
            dict: Novo ator/atriz cadastrado.
        """
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
