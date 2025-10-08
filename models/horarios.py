import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_profissional(0)

    def __str__(self):
        return f"{self._id} - {self._data.strftime('%d/%m/%Y %H:%M')} - {'Sim' if self._confirmado else 'Não'}"

    def get_id(self): return self._id
    def get_data(self): return self._data
    def get_confirmado(self): return self._confirmado
    def get_id_cliente(self): return self._id_cliente
    def get_id_servico(self): return self._id_servico
    def get_id_profissional(self): return self._id_profissional

    def set_id(self, id): self._id = id
    def set_data(self, data): self._data = data
    def set_confirmado(self, confirmado): self._confirmado = confirmado
    def set_id_cliente(self, id_cliente): self._id_cliente = id_cliente
    def set_id_servico(self, id_servico): self._id_servico = id_servico
    def set_id_profissional(self, id_profissional): self._id_profissional = id_profissional

    def to_json(self):
        return {
            "id": self._id,
            "data": self._data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self._confirmado,
            "id_cliente": self._id_cliente,
            "id_servico": self._id_servico,
            "id_profissional": self._id_profissional
        }

    @staticmethod
    def from_json(dic):
        try:
            data = datetime.strptime(dic.get("data", datetime.now().strftime("%d/%m/%Y %H:%M")), "%d/%m/%Y %H:%M")
        except Exception:
            data = datetime.now()
        h = Horario(dic.get("id", 0), data)
        h.set_confirmado(dic.get("confirmado", False))
        h.set_id_cliente(dic.get("id_cliente", 0))
        h.set_id_servico(dic.get("id_servico", 0))
        h.set_id_profissional(dic.get("id_profissional", 0))
        return h

class HorarioDAO:
    objetos = []
    carregado = False
    arquivo = "horarios.json"

    @classmethod
    def abrir(cls):
        if cls.carregado: return
        cls.objetos = []
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as f:
                list_dic = json.load(f)
                for dic in list_dic:
                    cls.objetos.append(Horario.from_json(dic))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Erro ao abrir {cls.arquivo}: {e}")
        cls.carregado = True

    @classmethod
    def salvar(cls):
        try:
            with open(cls.arquivo, "w", encoding="utf-8") as f:
                list_dic = [o.to_json() for o in cls.objetos]
                json.dump(list_dic, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar {cls.arquivo}: {e}")

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        novo_id = 0
        for aux in cls.objetos:
            if aux.get_id() > novo_id:
                novo_id = aux.get_id()
        obj.set_id(novo_id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()
