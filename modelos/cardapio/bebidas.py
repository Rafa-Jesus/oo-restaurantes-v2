from modelos.cardapio.itemcardapio import Itemcardapio

class Bebida(Itemcardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.08