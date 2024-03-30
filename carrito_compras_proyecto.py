from random import randint

class CarritoCompras:
    def __init__(self):
        self.items = []
        self.archivcarr = "tienda.txt"
        self.forma_pago = None

    def agreCarrito(self, item, cantidad=1):
        for i, cart_item in enumerate(self.items):
            if cart_item.nombre == item.nombre:
                if tienda[i].cantidad_disponible >= cantidad:  # Verificar si hay suficiente cantidad disponible
                    self.items[i].cantidad += cantidad
                    tienda[i].cantidad_disponible -= cantidad  # Actualizar la cantidad disponible en la tienda
                    return
                else:
                    print(f"No hay suficiente cantidad disponible de {item.nombre}")
                    return

        item.cantidad = cantidad
        self.items.append(item)
        tienda[item.item_id].cantidad_disponible -= cantidad  # Actualizar la cantidad disponible en la tienda

    def eliminarDeCarrito(self, itemId, cantidad=1):
        if 0 <= itemId < len(self.items):
            if self.items[itemId].cantidad > cantidad:
                self.items[itemId].cantidad -= cantidad
                tienda[self.items[itemId].item_id].cantidad_disponible += cantidad  # Devolver la cantidad a la tienda
            else:
                tienda[self.items[itemId].item_id].cantidad_disponible += self.items[itemId].cantidad  # Devolver toda la cantidad a la tienda
                self.items.pop(itemId)
        else:
            print("ID de artículo no válido")

    def ValorCompra(self):
        precio = 0
        for x in self.items:
            precio += x.precio * x.cantidad
        return precio

    def itemsComprados(self):
        print("Carrito Items:")
        for i, x in enumerate(self.items):
            print(f"{x.nombre} $ {x.precio} - Cantidad: {x.cantidad} - Pedido: {i}")
        print("")
        print("Forma de Pago:", self.forma_pago)

    def elegirFormaPago(self, forma_pago):
        self.forma_pago = forma_pago

class Item:
    def __init__(self, precio, nombre, cantidad_disponible, item_id):
        self.precio = precio
        self.nombre = nombre
        self.cantidad = 0
        self.cantidad_disponible = cantidad_disponible
        self.item_id = item_id

tienda = []
itemNombre = ["Gafas", "Sombrero", "Sombrilla", "Boligrafo"]

def CrearItemsTienda(cant):
    for item_id in range(cant):
        cantidad_disponible = randint(5, 20)  # Cantidad aleatoria disponible para cada artículo
        nItem = Item(randint(10, 50), itemNombre[item_id], cantidad_disponible, item_id)
        tienda.append(nItem)

def CrearTienda(tiendaInv):
    try:
        fx = open(tiendaInv, "r")
        str1 = fx.read()
    except IOError:
        print("\nLista de artículos para la venta:")
        CrearItemsTienda(len(itemNombre))

def listaTienda():
    print('\nItemID\t Precio\t Nombre\t Cantidad Disponible')
    for item in tienda:
        print(item.item_id, '\t   $', item.precio, '\t ', item.nombre, '\t\t', item.cantidad_disponible)

def Instrucciones():
    print("\nDigite C para chequear los items en el carrito")
    print("Digite R para remover items del carrito")
    print("Digite P para ver el valor total de la compra en el carrito") 
    print("Digite F para elegir la forma de pago")
    print("Digite X para salir del programa")
    
def removerItems(carr):
    input1 = int(input("Escriba el Pedido (si no lo sabe digite C) del item a remover: "))
    cantidad = int(input("Escriba la cantidad a remover: "))
    carr.eliminarDeCarrito(input1, cantidad)
    
def elegirFormaPago(carr):
    forma_pago = input("Elija la forma de pago (Efectivo, Tarjeta, Transferencia): ")
    carr.elegirFormaPago(forma_pago)

def comandos(in_var, carr):
    char_inputs = ["C", "R", "P", "F", "X"]
    if in_var == "C":
        carr.itemsComprados()
    elif in_var == "R":
        removerItems(carr)
    elif in_var == "P":
        print("El valor de la compra es ")
        print(carr.ValorCompra())
    elif in_var == "F":
        elegirFormaPago(carr)
    elif in_var == "X":
        global hecho
        hecho = True
    else:
        try:
            item_id, cantidad = map(int, in_var.split())
            if item_id < len(itemNombre) and cantidad > 0:
                carr.agreCarrito(tienda[item_id], cantidad)
            else:
                print("Comando no válido")
        except:
            print("Comando no válido")

cart1 = CarritoCompras()
CrearTienda(cart1.archivcarr)
hecho = False
while not hecho:
    listaTienda()
    Instrucciones()
    input_var = input("\nDigite el número del artículo y la cantidad a comprar (ejemplo: '0 2'): ")
    comandos(input_var, cart1)