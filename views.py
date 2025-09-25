from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, servicoDAO
from models.horario import Horario, HorarioDAO


class View:

    # Métodos para Cliente
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    # Métodos para Serviço
    @staticmethod
    def servico_listar():
        return servicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        servicoDAO.inserir(servico)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        servicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico = Servico(id, "", 0)
        servicoDAO.excluir(servico)

    # Métodos para Horário
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    @staticmethod
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
