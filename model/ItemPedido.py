from model.Pizza import Pizza
import time

class ItemPedido():

    def __init__(self, lista_pizzas, quantidade_de_itens, subtotal):
        self.lista_pizzas = lista_pizzas
        self.quantidade_de_itens = quantidade_de_itens
        self.subtotal = subtotal

    def __get_sabores_pizza(self):
        string_sabores = ""
        for pizza in self.lista_pizzas:
            string_sabores = string_sabores + "\n" + pizza.nome_pizza

        return string_sabores

    def fazer_pizzas(self):
        for pizza in self.lista_pizzas:
            print('Fazendo: ' + pizza.nome_pizza)
            time.sleep(5)
            print('Pizza finalizada.')


    def __str__(self):
        return """ 
        Qtd de pizzas: {qtd_pizzas}
        Subtotal: {subtotal}
        Sabores: {sabores}
        """.format(   qtd_pizzas = self.quantidade_de_itens
                    , subtotal = self.subtotal 
                    , sabores = self.__get_sabores_pizza())