from controller.ControllerPedidos import ControllerPedidos
class Facade():

    def exibir_menu():
        lista_nomes_pizza = []
        deseja_parar = False

        while deseja_parar == False:
            nome_pizza = input('Digite o nome do sabor desejado: ')
            lista_nomes_pizza.append(nome_pizza)

            deseja_parar_num = input('Digite 1 para continuar e 0 para parar: ')
            if int(deseja_parar_num) == 0:
                deseja_parar = True
        
        controller_pedidos = ControllerPedidos()
        pedido = controller_pedidos.criar_pedido(endereco = 'Rua Alice Vazami'
                                                , nome_pessoa = 'Victor'
                                                , pagto_credito = False
                                                , nomes_pizzas = lista_nomes_pizza
                                                )

        controller_pedidos.entregar_pedido(pedido)
        