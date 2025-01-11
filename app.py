"""
Este módulo inicia um aplicativo Streamlit chamado Flix app. Ele autentica o usuário
e permite navegar entre várias páginas, incluindo Início, Gêneros, Atores/Atrizes,
Filmes e Avaliações.
"""

import streamlit as st
from home.page import show_home
from actors.page import show_actors
from genres.page import show_genres
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login


def app():
    """
    Executa o aplicativo Flix. Verifica a autenticação do usuário e apresenta
    diferentes opções de navegação no menu lateral, dependendo da seleção do usuário.
    """
    if "token" not in st.session_state:
        show_login()
    else:
        st.title("Flix app")

        menu_option = st.sidebar.selectbox(
            "Selecione uma opção",
            ["Início", "Gêneros", "Atores/Atrizes", "Filmes", "Avaliações"],
        )

        if menu_option == "Início":
            show_home()

        elif menu_option == "Gêneros":
            show_genres()

        elif menu_option == "Atores/Atrizes":
            show_actors()

        elif menu_option == "Filmes":
            show_movies()

        elif menu_option == "Avaliações":
            show_reviews()


if __name__ == "__main__":
    app()
