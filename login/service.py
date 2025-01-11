"""
Este módulo fornece funcionalidades de autenticação, incluindo login e logout,
utilizando um serviço de API e a biblioteca Streamlit.
"""

import streamlit as st
from api.service import Auth


def login(username, password):
    """
    Realiza a autenticação do usuário.

    Parâmetros:
    - username: Nome do usuário.
    - password: Senha do usuário.

    Faz uma chamada ao serviço de API para obter o token de acesso.
    Em caso de sucesso, o token é armazenado no estado da sessão do Streamlit.
    Em caso de erro, exibe uma mensagem de falha.
    """
    auth_service = Auth()
    response = auth_service.get_token(username=username, password=password)

    if response.get("error"):
        st.error(f"Falha ao realizar login: {response.get('error')}")
    else:
        st.session_state.token = response.get("access")
        st.rerun()


def logout():
    """
    Efetua o logout do usuário.

    Remove todas as chaves do estado da sessão do Streamlit
    e recarrega a aplicação.
    """
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
