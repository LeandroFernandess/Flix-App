"""
Este módulo fornece uma interface de usuário para exibir e cadastrar atores ou atrizes
utilizando o Streamlit. Ele exibe uma lista de atores/atrizes existentes e permite
o cadastro de novos utilizando um serviço de API.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, ExcelExportMode
from actors.service import ActorService


def show_actors():
    """Exibe a lista de atores/atrizes e permite o cadastro de novos.

    A função utiliza o serviço ActorService para obter dados de atores
    e exibi-los em um formato de tabela interativo. Também permite o cadastro
    de novos atores através de um formulário.
    """
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write("Lista de Atores/Atrizes:")
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key="actors_grid",
        )
    else:
        st.warning("Nenhum Ator/Atriz encontrado.")

    st.title("Cadastrar Novo(a) Ator/Atriz")
    name = st.text_input("Nome")
    birthday = st.date_input(
        label="Data de Nascimento",
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )
    nationality_dropdown = ["BRA", "USA"]
    nationality = st.selectbox(
        label="Nacionalidade",
        options=nationality_dropdown,
    )
    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error("Erro ao cadastrar o(a) Ator/Atriz. Verifique os campos")
