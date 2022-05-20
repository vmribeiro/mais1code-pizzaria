class Pizza(object):

    def __init__(self, nome_pizza, valor_pizza, tipo_brotinho):
        self.nome_pizza = nome_pizza
        self.valor_pizza = valor_pizza
        self.tipo_brotinho = tipo_brotinho

    def fazer_pizza(self):
        print('fazendo pizza')
        print('pizza feita')

    def __str__(self):
        return """
        *******************
        Sabor: {nome_pizza}
        Valor: {valor_pizza}
        Tipo da pizza: {tipo_pizza}
        *******************
        """.format(  nome_pizza  = self.nome_pizza
                   , valor_pizza = self.valor_pizza 
                   , tipo_pizza  = 'Brotinho' if self.tipo_brotinho else 'Tamanho Normal' )