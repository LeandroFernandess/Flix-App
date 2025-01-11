"""
Este módulo define a classe ReviewService, que fornece métodos para
interagir com as avaliações de filmes, utilizando o ReviewRepository
para acessar a API. Utiliza o Streamlit para gerenciar o estado da sessão.
"""

import streamlit as st
from reviews.repository import ReviewRepository


class ReviewService:
    """
    Serviço para gerenciar avaliações de filmes, fornecendo métodos
    para recuperar e criar novas avaliações.
    """

    def __init__(self):
        """
        Inicializa o ReviewService com uma instância de ReviewRepository.
        """
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        """
        Obtém a lista de avaliações, recuperando-as do estado da sessão
        se já estiverem disponíveis, ou da API, se necessário.

        Returns:
            list: Lista de avaliações armazenadas no estado da sessão
            ou obtidas da API.
        """
        if "reviews" in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        """
        Cria uma nova avaliação e a adiciona ao estado da sessão.

        Args:
            movie (int): Identificador do filme a ser avaliado.
            stars (int): Número de estrelas na avaliação.
            comment (str): Comentário da avaliação.

        Returns:
            dict: A nova avaliação criada.
        """
        review = dict(movie=movie, stars=stars, comment=comment)
        new_review = self.review_repository.create_review(review)
        st.session_state.reviews.append(new_review)
        return new_review
