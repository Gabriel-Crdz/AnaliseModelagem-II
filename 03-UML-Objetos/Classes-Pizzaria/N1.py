# Implementação em Python
from datetime import datetime

class Usuario:
    def __init__ (self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Cliente(Usuario):
    def __init__ (self, nome, telefone, email, endereco):
        super().__init__(nome, telefone, email)
        self.endereco = endereco

class Atendente(Usuario):
    pass

class Pizzaiolo(Usuario):
    pass

class Entregador(Usuario):
    def __init__ (self, nome, telefone, email, veiculo):
        super().__init__(nome, telefone, email)
        self.veiculo = veiculo

class Administrador(Usuario):
    pass

class Sabor:
    def __init__ (self, nome, descricao, preco_adicional=0):
        self.nome = nome
        self.descricao = descricao
        self.preco_adicional = preco_adicional

class Pizza:
    def __init__ (self, tamanho, preco_base):
        self.tamanho = tamanho
        self.preco_base = preco_base
        self.sabores = []

    def adicionar_sabor(self, sabor):
        if len(self.sabores) < 2:
            self.sabores.append(sabor)
        else:
            print("A pizza tem o limite de 2 sabores!")

    def calcular_preco(self):
        total = self.preco_base

        for sabor in self.sabores:
            total += sabor.preco_adicional

        return total

class Pedido:
    def __init__ (self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.data = datetime.now()
        self.pizzas = []
        self.status = "Recebido"

        self.atendente = None
        self.pizzaiolo = None
        self.entregador = None

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total (self):
        total = 0

        for pizza in self.pizzas:
            total += pizza.calcular_preco()

        return total

    def alterar_status (self, novo_status):
        self.status = novo_status

# Exemplo
cliente = Cliente("Jorge Almado", "45-9999-9999", "jorge_almado@bol.com.br", "Rua Ali do Lado, 12")

sabor_calabresa = Sabor("Calabresa", "Calabresa com cebola")
pizza = Pizza ("Grande", 50)
pizza.adicionar_sabor(sabor_calabresa)

pedido = Pedido (1, cliente)
pedido.adicionar_pizza(pizza)

print(f"Cliente: {pedido.cliente.nome}, Total: {pedido.calcular_total()}")