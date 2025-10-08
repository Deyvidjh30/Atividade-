import streamlit as st
from datetime import datetime
import time
from view import View

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterHorarioUI.listar()
        with tab2:
            ManterHorarioUI.inserir()
        with tab3:
            ManterHorarioUI.atualizar()
        with tab4:
            ManterHorarioUI.excluir()

    @staticmethod
    def listar():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return

        clientes = {c.get_id(): c for c in View.cliente_listar()}
        servicos = {s.get_id(): s for s in View.servico_listar()}
        profissionais = {p.get_id(): p for p in View.profissional_listar()}

        for horario in horarios:
            st.markdown(f"### Horário ID: {horario.get_id()}")
            st.write("Data:", horario.get_data().strftime("%d/%m/%Y %H:%M"))
            st.write("Confirmado:", "Sim" if horario.get_confirmado() else "Não")
            cliente = clientes.get(horario.get_id_cliente())
            servico = servicos.get(horario.get_id_servico())
            prof = profissionais.get(horario.get_id_profissional())
            st.write("Cliente:", cliente.get_nome() if cliente else "N/A")
            st.write("Serviço:", servico.get_descricao() if servico else "N/A")
            st.write("Profissional:", prof.get_nome() if prof else "N/A")
            st.markdown("---")

    @staticmethod
    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()

        data = st.text_input("Informe a data e horário do serviço (dd/mm/yyyy HH:MM)", datetime.now().strftime("%d/%m/%Y %H:%M"), key="hr_data")
        confirmado = st.checkbox("Confirmado", key="hr_conf")
        cliente = st.selectbox("Informe o cliente", clientes, format_func=lambda c: f"{c.get_id()} - {c.get_nome()}")
        servico = st.selectbox("Informe o serviço", servicos, format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}")
        profissional = st.selectbox("Informe o profissional", profissionais, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}")

        if st.button("Inserir"):
            try:
                data_formatada = datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.horario_inserir(data_formatada, confirmado, cliente.get_id(), servico.get_id(), profissional.get_id())
                st.success("Horário inserido com sucesso.")
                time.sleep(1)
                st.experimental_rerun()
            except ValueError:
                st.error("Data inválida. Use o formato dd/mm/yyyy HH:MM.")

    @staticmethod
    def atualizar():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return

        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()

        op = st.selectbox("Selecione um horário para atualizar", horarios, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}")
        data = st.text_input("Nova data e horário", op.get_data().strftime("%d/%m/%Y %H:%M"), key="hr_up_data")
        confirmado = st.checkbox("Confirmado", value=op.get_confirmado(), key="hr_up_conf")

        cliente_index = next((i for i, c in enumerate(clientes) if c.get_id() == op.get_id_cliente()), 0)
        servico_index = next((i for i, s in enumerate(servicos) if s.get_id() == op.get_id_servico()), 0)
        prof_index = next((i for i, p in enumerate(profissionais) if p.get_id() == op.get_id_profissional()), 0)

        cliente = st.selectbox("Novo cliente", clientes, index=cliente_index, format_func=lambda c: f"{c.get_id()} - {c.get_nome()}")
        servico = st.selectbox("Novo serviço", servicos, index=servico_index, format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}")
        profissional = st.selectbox("Novo profissional", profissionais, index=prof_index, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}")

        if st.button("Atualizar"):
            try:
                data_formatada = datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.horario_atualizar(op.get_id(), data_formatada, confirmado, cliente.get_id(), servico.get_id(), profissional.get_id())
                st.success("Horário atualizado com sucesso.")
            except ValueError:
                st.error("Data inválida. Use o formato dd/mm/yyyy HH:MM.")

    @staticmethod
    def excluir():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return
        op = st.selectbox("Selecione um horário para excluir", horarios, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}")
        if st.button("Excluir"):
            View.horario_excluir(op.get_id())
            st.success("Horário excluído com sucesso.")
            time.sleep(1)
            st.experimental_rerun()
