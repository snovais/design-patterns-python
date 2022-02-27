class Orcamento( object ):
    def __init__( self, valor ):
        self.__valor = valor

    # permite chamar objeto.valor sem ferir o encapsulamento, pois debaixo dos panos,
    # é chamado esse método
    @property
    def valor( self):
        return self.__valor
