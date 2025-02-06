from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Pratos
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
prato_nhoque = Pratos('Nhoque', 69.90, 'Gostoso')
bebida_limoneto = Bebida('Limoneto', 20.00, '300ml')
sobremesa_pudim = Sobremesa('Pudim', 50.00, 'Melhor pudim da cidade')

restaurante_praca.adicionar_item_no_cardapio(prato_nhoque)
prato_nhoque.aplicar_desconto()
restaurante_praca.adicionar_item_no_cardapio(sobremesa_pudim)
restaurante_praca.adicionar_item_no_cardapio(bebida_limoneto)
bebida_limoneto.aplicar_desconto()

restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('Rafael', 5)
restaurante_praca.receber_avaliacao('Sofia', 3)
restaurante_praca.receber_avaliacao('Etson', 4)

def main():
    restaurante_praca.listar_restaurantes()
    print()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()