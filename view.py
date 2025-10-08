from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horarios import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class Views:
    
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone, senha=""):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha=None):
        cliente = Cliente(id, nome, email, fone, senha if senha is not None else "")
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def autenticar_cliente(email, senha):
        return ClienteDAO.autenticar(email, senha)

    # Servico
    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)

    # Horario
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(0, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)
        HorarioDAO.inserir(horario)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(id, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario = HorarioDAO.listar_id(id)
        if horario:
            HorarioDAO.excluir(horario)

    # Profissional
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_inserir(nome, email, fone, senha=""):
        prof = Profissional(0, nome, email, fone, senha)
        ProfissionalDAO.inserir(prof)

    @staticmethod
    def profissional_atualizar(id, nome, email, fone, senha=None):
        prof = Profissional(id, nome, email, fone, senha if senha is not None else "")
        ProfissionalDAO.atualizar(prof)

    @staticmethod
    def profissional_excluir(id):
        prof = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(prof)

    @staticmethod
    def autenticar_profissional(email, senha):
        return ProfissionalDAO.autenticar(email, senha)
