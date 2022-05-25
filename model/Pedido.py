from model.ItemPedido import ItemPedido
import time

class Pedido():

    def __init__(self, lista_itens_pedidos, valor_total, endereco
                     , nome_pessoa, pagto_credito):
        self.lista_itens_pedidos = lista_itens_pedidos
        self.valor_total = valor_total
        self.endereco = endereco
        self.nome_pessoa = nome_pessoa 
        self.pagto_credito = pagto_credito
    
    def entregar_pedido(self):
        print('Entregando pedido...')
        time.sleep(10)
        print('Pedido entregue')

    def fazer_itens_pedido(self):
        for item in self.lista_itens_pedidos:
            item.fazer_pizzas()

    def __get_string_itens_pedido(self):
        string_itens_pedido = ""
        for item_pedido in self.lista_itens_pedidos:
            string_itens_pedido = string_itens_pedido + "\n" + str(item_pedido)

        return string_itens_pedido

    def __str__(self):
        return """
        Itens pedidos: {str_itens_pedidos}
        Total: {total_pedido}
        Tipo de pagto: {tipo_pagto}
        Endereço de entrega: {endereco}
        Nome destinatário: {nome_pessoa}
        """.format( str_itens_pedidos =  self.__get_string_itens_pedido()
                  , total_pedido = self.valor_total 
                  , tipo_pagto = 'Crédito' if self.pagto_credito == True else 'Dinheiro'
                  , endereco = self.endereco
                  , nome_pessoa = self.nome_pessoa )

    