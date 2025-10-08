import streamlit as st
from view import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Login no Sistema")
        tipo = st.radio("Entrar como:", ("Cliente", "Profissional"), index=0)
        email = st.text_input("E-mail", key="login_email")
        senha = st.text_input("Senha", type="password", key="login_senha")

        if st.button("Entrar"):
            usuario = None
            if tipo == "Cliente":
                usuario = View.autenticar_cliente(email, senha)
            else:
                usuario = View.autenticar_profissional(email, senha)

            if usuario:
                # armazenar apenas os dados necessários (dicionário)
                st.session_state["usuario"] = usuario.to_json()
                st.session_state["tipo"] = tipo
                st.success(f"Bem-vindo(a), {usuario.get_nome()}!")
                st.experimental_rerun()
            else:
                st.error("E-mail ou senha inválidos.")

    @staticmethod
    def logout():
        if "usuario" in st.session_state:
            del st.session_state["usuario"]
        if "tipo" in st.session_state:
            del st.session_state["tipo"]
        st.experimental_rerun()
