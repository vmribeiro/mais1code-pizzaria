from model.Pizza import Pizza

class PizzaMista(Pizza):

    def __init__(self, nome_pizza, valor_pizza, tipo_brotinho):
        super().__init__(nome_pizza, valor_pizza, tipo_brotinho)

    #override
    def fazer_pizza(self):
        print('fazendo pizza mista')
        print('pizza mista feita')
