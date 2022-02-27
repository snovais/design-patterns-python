# -*- coding: UTF-8 -*-

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos( object ):
    def calcula( self, orcamento ):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcula(orcamento)
        
        return desconto

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))


    print(orcamento.valor)

    calcudor = Calculador_de_descontos()
    desconto = calcudor.calcula(orcamento)

    print('Desconto calculado %s' % (round(desconto, 2)))