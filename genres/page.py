"""
Este módulo exibe e gerencia gêneros de filmes usando Streamlit.
Inclui funções para listar gêneros e cadastrar novos gêneros de filmes.
"""

import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService


def show_genres():
    """Exibe e cadastra gêneros de filmes.

    Usa o serviço de gêneros para buscar e apresentar a lista de
    gêneros. Também permite cadastrar novos gêneros.
    """
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de gêneros")
        genres_df = pd.json_normalize(genres)

        AgGrid(data=genres_df, reload_data=True, key="genres_grid")
    else:
        st.warning("Nenhum gênero cadastrado")

    st.title("Cadastrar novo gênero")
    name = st.text_input("Nome do gênero")

    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.rerun()
        else:
            st.error("Erro ao cadastrar gênero")
