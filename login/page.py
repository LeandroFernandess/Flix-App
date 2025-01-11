"""
Este módulo fornece uma interface simples de login utilizando a biblioteca Streamlit.
Ele exibe um formulário para que o usuário insira suas credenciais de acesso.
"""

import streamlit as st
from login.service import login


def show_login():
    """
    Exibe uma tela de login onde o usuário pode inserir seu nome de usuário e senha.

    Ao clicar no botão de login, a função envia as credenciais para o serviço de login.
    """
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        login(username=username, password=password)
