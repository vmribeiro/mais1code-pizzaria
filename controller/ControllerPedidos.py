from model.Pizza         import Pizza
from model.PizzaDoce     import PizzaDoce
from model.PizzaSalgada  import PizzaSalgada
from model.PizzaMista    import PizzaMista
from model.ItemPedido    import ItemPedido
from model.Pedido        import Pedido
class ControllerPedidos():

    def criar_pedido(self, endereco, nome_pessoa, pagto_credito, nomes_pizzas):
        
        pizza1 = PizzaSalgada(nome_pizza = nomes_pizzas[0]
                            , valor_pizza = 35
                            , tipo_brotinho = True)

        pizza2 = PizzaDoce(   nome_pizza = nomes_pizzas[1]
                            , valor_pizza = 35
                            , tipo_brotinho = True)

        pizza3 = PizzaMista(nome_pizza = nomes_pizzas[2]
                            , valor_pizza = 35
                            , tipo_brotinho = True)

        lista_pizzas = []
        lista_pizzas.append(pizza1)
        lista_pizzas.append(pizza2)
        lista_pizzas.append(pizza3)

        subtotal_pizzas = 0
        for pizza in lista_pizzas:
            subtotal_pizzas = subtotal_pizzas + pizza.valor_pizza

        item_pedido1 = ItemPedido(lista_pizzas = lista_pizzas
                                , quantidade_de_itens = len(lista_pizzas)
                                , subtotal = subtotal_pizzas)

        lista_itens_pedidos = []
        lista_itens_pedidos.append(item_pedido1)

        total_pedido = 0
        for item_pedido in lista_itens_pedidos:
            total_pedido = total_pedido + item_pedido.subtotal

        pedido = Pedido( lista_itens_pedidos = lista_itens_pedidos
                    , valor_total = total_pedido
                    , endereco = "Rua Juscelino Kubichek"
                    , nome_pessoa = "Otavio"
                    , pagto_credito = True  )
        print(pedido)

        return pedido

    def fazer_pedido(self, pedido):
        pedido.fazer_itens_pedido()

    def entregar_pedido(self, pedido):
        pedido.entregar_pedido()