import streamlit as st
from view import View

class PerfilUI:
    @staticmethod
    def main():
        if "usuario" not in st.session_state:
            st.info("Nenhum usuário logado.")
            return

        usuario = st.session_state["usuario"]
        tipo = st.session_state.get("tipo", "Cliente")

        st.header("Meu Perfil")
        st.write(f"Tipo: {tipo}")

        nome = st.text_input("Nome", usuario.get("nome", ""), key="pf_nome")
        email = st.text_input("E-mail", usuario.get("email", ""), key="pf_email")
        fone = st.text_input("Telefone", usuario.get("fone", ""), key="pf_fone")
        senha = st.text_input("Senha", usuario.get("senha", ""), type="password", key="pf_senha")

        if st.button("Atualizar"):
            if tipo == "Cliente":
                View.cliente_atualizar(usuario["id"], nome, email, fone, senha)
                # atualizar session_state com novos dados
                novo = {"id": usuario["id"], "nome": nome, "email": email, "fone": fone, "senha": senha}
                st.session_state["usuario"] = novo
                st.success("Perfil de cliente atualizado.")
            else:
                View.profissional_atualizar(usuario["id"], nome, email, fone, senha)
                novo = {"id": usuario["id"], "nome": nome, "email": email, "fone": fone, "senha": senha}
                st.session_state["usuario"] = novo
                st.success("Perfil de profissional atualizado.")

        if st.button("Sair"):
            from templates.loginUI import LoginUI
            LoginUI.logout()
