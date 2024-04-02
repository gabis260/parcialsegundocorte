from abc import ABC, abstractmethod
from typing import List, Dict
from colorama import Fore, Style,Back
from tabulate import tabulate

class Product(ABC):
    """
    Clase base abstracta para productos.
    """

    def __init__(self, name: str, description: str, price: float, category: str):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    @abstractmethod
    def display(self):
        """
        Muestra detalles del producto.
        """
        pass

class PhysicalProduct(Product):
    """
    Clase para productos físicos.
    """

    def display(self):
        print(Fore.GREEN + Style.BRIGHT + f"Nombre: {self.name}")
        print(Fore.YELLOW + f"Descripción: {self.description}")
        print(Fore.BLUE + f"Precio: ${self.price:,.3f}")
        print(Fore.CYAN + f"Categoría: {self.category}" + Style.RESET_ALL)

class DigitalProduct(Product):
    """
    Clase para productos digitales.
    """

    def display(self):
        print(Fore.MAGENTA + Style.BRIGHT + f"Nombre: {self.name}")
        print(Fore.WHITE + f"Descripción: {self.description}")
        print(Fore.RED + f"Precio: ${self.price:,.3f}")
        print(Fore.BLACK+ f"Categoría: {self.category}" + Style.RESET_ALL)

class ProductCatalog:
    """
    Catálogo de productos.
    """

    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.categories: Dict[str, List[Product]] = {}

    def add_product(self, product: Product):
        self.products[product.name] = product
        category = self.categories.get(product.category, [])
        category.append(product)
        self.categories[product.category] = category

    def get_products(self) -> List[Product]:
        return list(self.products.values())

    def get_product(self, name: str) -> Product:
        return self.products.get(name)

    def get_products_by_category(self, category: str) -> List[Product]:
        return self.categories.get(category, [])

class ShoppingCart:
    """
    Carrito de compras.
    """

    def __init__(self):
        self.items: Dict[Product, int] = {}

    def add_item(self, product: Product, quantity: int):
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_item(self, product: Product):
        if product in self.items:
            del self.items[product]

    def get_total(self) -> float:
        total = 0.0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def display(self):
        print(Fore.GREEN + Style.BRIGHT + "Carrito de Compras")
        for product, quantity in self.items.items():
            print(f"{quantity} x {product.name} = ${product.price * quantity:.3f}")
        print(Fore.RED + f"Total: ${self.get_total():,.3f}" + Style.RESET_ALL)

    def discount(self):
        percentage= 5 / 100
        can_discount = self.get_total() - (self.get_total() * percentage)
        discount2= print(Fore.GREEN + f"Su descuento de 5% por ser el mejor profesor fue aplicado con éxito,\nAhora su total a pagar es: ${can_discount:,.03f} "+ Fore.RESET)
        return discount2

class OnlineStore:
    """
    Tienda en línea.
    """

    def __init__(self):
        self.catalog = ProductCatalog()
        self.cart = ShoppingCart()

    def run(self):
        self.setup_products()
        while True:
            self.display_menu()
            choice = input(Style.BRIGHT+"Ingrese su opción:")
            self.handle_choice(choice)

    def setup_products(self):
        self.catalog.add_product(PhysicalProduct("Libro de aventuras", "Don quijote de la mancha.", 150.850, "Libros"))
        self.catalog.add_product(DigitalProduct("Curso en línea ", "Curso de programación en Python.", 220.000, "Aprendizaje"))
        self.catalog.add_product(PhysicalProduct("Laptop", "Asus TUF GAMING F15.", 4000.215 , "Tecnología"))
        self.catalog.add_product(PhysicalProduct("Comida enlatada", "Lata de atún Vancamps.", 21.000, "Comida"))
        self.catalog.add_product(PhysicalProduct("Vino", "Bebida sumamente alcoholizada para +18. ", 133.000 , "bebida"))
        self.catalog.add_product(PhysicalProduct("Iphone 15 pro max", "Celular Iphone 15 pro max 512GB.", 6780.000, "Tecnología"))
        self.catalog.add_product(PhysicalProduct("Jabón de baño", "Jabón líquido con aroma a vainilla.", 20.000 , "Aseo"))
        self.catalog.add_product(DigitalProduct("Curso de ingles","Aprende ingles b2 con nosotros x 12 meses.",4500.000, "Aprendizaje"))
        self.catalog.add_product(DigitalProduct("Targeta de regalo","Targeta de regalo membresia 1 mes de Netlix - 2 pantallas.", 38.000, "Tecnología"))
        self.catalog.add_product(PhysicalProduct("Libro de terror", "La casa de las sombras.",65.000, "Libros"))
        self.catalog.add_product(PhysicalProduct("Crema dental", "Crema de dientas con triple acción.",6.500, "Aseo"))
        self.catalog.add_product(PhysicalProduct("Pestañina", "Pestañina a prueba de agua 3 días de duración.",22.000, "Belleza"))
        self.catalog.add_product(PhysicalProduct("Labial", "Labial rojo mate.", 8.500, "Belleza"))
        self.catalog.add_product(PhysicalProduct("Pasta", "pasta en fideos 500g.", 4.110, "Comida"))
        self.catalog.add_product(PhysicalProduct("Coca-cola", "Gaseosa COCA COLA Sabor Original x 2 Unds 6000 ml.", 16.500, "Bebida"))
        self.catalog.add_product(PhysicalProduct("Cerveza", "Cerveza Lata Sixpack AGUILA 1980 ml.", 18.000 , "Bebida"))
        self.catalog.add_product(PhysicalProduct("Iluminador", "Ilumina y resalta tu belleza con el iluminador.",35.000, "Belleza"))
        self.catalog.add_product(PhysicalProduct("Acetaminofén", " alivia el dolor leve o moderado de las cefaleas, dolores musculares y colicos x 500mg.", 11.000 , "Medicamento"))
        self.catalog.add_product(PhysicalProduct("Ibuprofeno", "para aliviar el dolor, la sensibilidad, la inflamación y la rigidez.", 15.000, "Medicamento"))




    def display_menu(self):
        print(Back.RESET + Fore.RESET+ Back.MAGENTA+ Fore.CYAN+ Style.BRIGHT +"\nBIENVENIDO A TIENDAS GABS \U0001F600  \n"+Back.RESET)
        print(Fore.WHITE + "1. Ver catálogo de productos")
        print("2. Ver carrito de compras")
        print("3. Agregar producto al carrito")
        print("4. Remover producto del carrito")
        print("5. Realizar pedido")
        print("6. Buscar productos por categoría")
        print("7. Realizar busqueda de productos")
        print("8. Salir" + Style.RESET_ALL)

    def handle_choice(self, choice: str):

        
        if choice == "1":
            self.display_catalog()
        elif choice == "2":
            self.cart.display()
        elif choice == "3":
            self.add_to_cart()
        elif choice == "4":
            self.remove_from_cart()
        elif choice == "5":
            self.checkout()
        elif choice == "6":
        
            self.search_by_category()

        elif choice == "7":
            self.search_products()
        elif choice == "8":
        
            print( Back.MAGENTA+ Fore.CYAN+ Style.BRIGHT+ "¡Gracias por visitar nuestra tienda!, Vuelva pronto. " +Back.RESET)
            exit()
        else:
            print("Opción inválida. Intente de nuevo.")

    def display_catalog(self):
        products = self.catalog.get_products()
        if not products:
            print("No hay productos disponibles.")
        else:
            table_data = [(Fore.RESET + p.name, p.description, f"${p.price:,.3f}" , p.category ) for p in products]
            table_headers =[Fore.YELLOW+ "Nombre", "Descripción", "Precio", "Categoría" ]

            print("\033[4;35m"+"CATÁLOGO DE PRODUCTOS"+'\033[0;m')
            print(tabulate( table_data, headers=table_headers, tablefmt="fancy_grid"))

    def add_to_cart(self):
        name = input("Ingrese el nombre del producto: ")
        product = self.catalog.get_product(name)
        if product:
            quantity = int(input("Ingrese la cantidad: "))
            self.cart.add_item(product, quantity)
            print(Fore.GREEN + Style.BRIGHT+  "Producto agregado al carrito." + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT +"Producto no encontrado." + Style.RESET_ALL)

    def remove_from_cart(self):
        if not self.cart.items:
                print(Fore.RED + Style.BRIGHT+ "El carrito está vacío, no puedes remover nada" + Style.RESET_ALL)
        else:
            name = input("Ingrese el nombre del producto que deseas remover: ")
            product = self.catalog.get_product(name)
            if product in self.cart.items:
                self.cart.remove_item(product)
                print(Fore.GREEN + "Producto removido del carrito." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Producto no encontrado en el carrito." + Style.RESET_ALL)


    def checkout(self):
            if not self.cart.items:
                print(Fore.RED + "El carrito está vacío." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + Style.BRIGHT + "Realizar Pedido")
                self.cart.display()
                confirm = input(Style.BRIGHT + "¿Confirmar pedido? (s/n): ")
                if confirm.lower() == "s":
                    discount = input("¿Usted es el profesor? (s/n):")
                    if discount == "s":
                        self.cart.discount()
                    elif discount == "n":
                        print(Fore.RED + "No hay descuento para ti:(")
                    m_payment = input(Fore.RESET +Style.BRIGHT + "Ingrese el método de pago (efectivo/tarjeta): ")
                    if m_payment.lower() == "efectivo":
                        print(Fore.YELLOW+ Style.BRIGHT + "Se realizará el pago en efectivo al recibir el pedido.")
                    elif m_payment.lower() == "tarjeta":
                            print(Fore.GREEN+Style.BRIGHT + "Se realizará el cargo a su tarjeta de crédito o débito.")
                    else:
                        print(Fore.RED + "Método de pago inválido." + Style.RESET_ALL)
                        return
                    
                
                    user = input(Fore.RESET + Style.BRIGHT + "Ingrese el nombre del destinatario: ")
                    address = input(Style.BRIGHT + "Ingrese la dirección de envío: ")

                    print(Fore.YELLOW + Style.BRIGHT + f"\nApreciado/a {user} sus datos de pedido son : ")
                    print(Fore.BLACK+ Style.BRIGHT + f"Destinatario: {user}")
                    print(Style.BRIGHT + f"Dirección de envío: {address}")
                    print(Style.BRIGHT + f"Método de pago: {m_payment.capitalize()}")
                    print(Fore.GREEN + "Pedido realizado con éxito." + Style.RESET_ALL)

                    self.cart = ShoppingCart()
                else:
                    print(Fore.RED+ "Pedido cancelado.")    

 
    def search_by_category(self):
        category = input("Ingrese la categoría a buscar: ")
        products = self.catalog.get_products_by_category(category)
        if not products:
            print(Fore.RED + f"No se encontraron productos en la categoría '{category}'." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + Style.BRIGHT + f"Productos en la categoría '{category}'")
            for product in products:
                product.display()
                print()
                
    def search_products(self):
        search_term = input("Ingrese el término de búsqueda para realizar los filtros (se buscara cualquier coincidencia mas no se filtrara por Categoría): ")
        products = [
            p for p in self.catalog.get_products()
            if search_term.lower() in p.name.lower() or search_term.lower() in p.description.lower()
        ]

        if not products:
            print(Fore.RED + f"No se encontraron productos que coincidan con '{search_term}'." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + Style.BRIGHT + f"Productos que coinciden con '{search_term}'")
            for product in products:
                product.display()
                print()

if __name__ == "__main__":
    store = OnlineStore()
    store.run()