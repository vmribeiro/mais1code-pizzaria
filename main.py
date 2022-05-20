from model.Pizza import Pizza
from model.PizzaDoce     import PizzaDoce
from model.PizzaSalgada  import PizzaSalgada
from model.PizzaMista    import PizzaMista

pizza1 = PizzaSalgada(nome_pizza = 'Pizza de Calabresa'
                    , valor_pizza = 35
                    , tipo_brotinho = True)
print(pizza1)
pizza1.fazer_pizza()

pizza2 = PizzaDoce(nome_pizza = 'Pizza de Chocolate'
                    , valor_pizza = 35
                    , tipo_brotinho = True)
print(pizza2)
pizza2.fazer_pizza()

pizza3 = PizzaMista(nome_pizza = 'Pizza 1/2 Calabresa 1/2 Frango'
                    , valor_pizza = 35
                    , tipo_brotinho = True)
print(pizza3)
pizza3.fazer_pizza()