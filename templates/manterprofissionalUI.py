import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProfissionalUI.listar()
        with tab2:
            ManterProfissionalUI.inserir()
        with tab3:
            ManterProfissionalUI.atualizar()
        with tab4:
            ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        df = pd.DataFrame([p.to_json() for p in profissionais])
        st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="prof_nome")
        email = st.text_input("Informe o e-mail", key="prof_email")
        fone = st.text_input("Informe o fone", key="prof_fone")
        senha = st.text_input("Senha (profissional)", type="password", key="prof_senha")
        if st.button("Inserir"):
            if not nome or not email:
                st.error("Nome e e-mail são obrigatórios.")
                return
            View.profissional_inserir(nome, email, fone, senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(1.2)
            st.experimental_rerun()

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        op = st.selectbox("Atualização de Profissionais", profissionais, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}")
        nome = st.text_input("Novo nome", op.get_nome(), key="prof_up_nome")
        email = st.text_input("Novo e-mail", op.get_email(), key="prof_up_email")
        fone = st.text_input("Novo fone", op.get_fone(), key="prof_up_fone")
        senha = st.text_input("Nova senha (opcional)", type="password", key="prof_up_senha")
        if st.button("Atualizar"):
            View.profissional_atualizar(op.get_id(), nome, email, fone, senha if senha else op.get_senha())
            st.success("Profissional atualizado com sucesso")

    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        op = st.selectbox("Exclusão de Profissionais", profissionais, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}")
        if st.button("Excluir"):
            View.profissional_excluir(op.get_id())
            st.success("Profissional excluído com sucesso")
            time.sleep(1)
            st.experimental_rerun()
