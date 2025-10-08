import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha=""):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self): return self._id
    def get_nome(self): return self._nome
    def get_email(self): return self._email
    def get_fone(self): return self._fone
    def get_senha(self): return self._senha

    def set_id(self, id): self._id = id
    def set_nome(self, nome): self._nome = nome
    def set_email(self, email): self._email = email
    def set_fone(self, fone): self._fone = fone
    def set_senha(self, senha): self._senha = senha

    def to_json(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "fone": self._fone,
            "senha": self._senha
        }

    @staticmethod
    def from_json(dic):
        return Cliente(dic.get("id", 0), dic.get("nome", ""), dic.get("email", ""), dic.get("fone", ""), dic.get("senha", ""))

    def __str__(self):
        return f"{self._id} - {self._nome}"

class ClienteDAO:
    objetos = []
    carregado = False
    arquivo = "clientes.json"

    @classmethod
    def abrir(cls):
        if cls.carregado: 
            return
        cls.objetos = []
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as f:
                list_dic = json.load(f)
                for dic in list_dic:
                    cls.objetos.append(Cliente.from_json(dic))
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

    @classmethod
    def autenticar(cls, email, senha):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_email() == email and obj.get_senha() == senha:
                return obj
        return None
