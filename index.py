import streamlit as st
from templates.manterservicoUI import ManterServicoUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.loginUI import LoginUI
from templates.perfilUI import PerfilUI
from view import Views

st.set_page_config(page_title="Sistema de Agendamento", layout="wide")

def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Perfil", "Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Sair"])
    return op

def main():
    if "usuario" not in st.session_state:
        # se não logado, mostra tela de login à esquerda e um card explicativo
        with st.sidebar:
            st.write("Faça login para acessar o sistema")
        LoginUI.main()
        return

    usuario = st.session_state["usuario"]
    tipo = st.session_state.get("tipo", "Cliente")
    st.sidebar.write(f"Usuário logado: {usuario.get('nome')} ({tipo})")
    op = menu_admin()

    if op == "Perfil":
        PerfilUI.main()
    elif op == "Cadastro de Clientes":
        ManterClienteUI.main()
    elif op == "Cadastro de Serviços":
        ManterServicoUI.main()
    elif op == "Cadastro de Horários":
        ManterHorarioUI.main()
    elif op == "Cadastro de Profissionais":
        ManterProfissionalUI.main()
    elif op == "Sair":
        # limpa sessão e retorna para login
        if "usuario" in st.session_state:
            del st.session_state["usuario"]
        if "tipo" in st.session_state:
            del st.session_state["tipo"]
        st.experimental_rerun()

if __name__ == "__main__":
    main()
