from modelos.cardapio.itemcardapio import Itemcardapio

class Pratos(Itemcardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05