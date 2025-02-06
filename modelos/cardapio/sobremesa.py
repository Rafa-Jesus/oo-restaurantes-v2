from modelos.cardapio.itemcardapio import Itemcardapio

class Sobremesa(Itemcardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.10