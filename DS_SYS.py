class Pedido:
    def __init__(self, codigo, cliente, producto, cantidad, precio_unitario, fecha_entrega):
        if not cliente.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if not producto.strip():
            raise ValueError("El producto no puede estar vacío.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if precio_unitario <= 0:
            raise ValueError("El precio unitario debe ser mayor a cero.")

        self.codigo = codigo
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha_entrega = fecha_entrega
        self.estado = "Pendiente"

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def mostrar(self):
        return (
            f"Código: {self.codigo} | Cliente: {self.cliente} | Producto: {self.producto} | "
            f"Cantidad: {self.cantidad} | Precio: S/ {self.precio_unitario:.2f} | "
            f"Total: S/ {self.calcular_total():.2f} | Fecha entrega: {self.fecha_entrega} | "
            f"Estado: {self.estado}"
        )


class PasteleriaApp:
    def __init__(self):
        self.pedidos = []
        self.contador = 1

    def generar_codigo(self):
        codigo = f"P{self.contador:03}"
        self.contador += 1
        return codigo

    def registrar_pedido(self):
        try:
            cliente = input("Ingrese el nombre del cliente: ").strip()
            producto = input("Ingrese el producto: ").strip()
            cantidad = int(input("Ingrese la cantidad: "))
            precio_unitario = float(input("Ingrese el precio unitario: "))
            fecha_entrega = input("Ingrese la fecha de entrega: ").strip()

            codigo = self.generar_codigo()
            pedido = Pedido(codigo, cliente, producto, cantidad, precio_unitario, fecha_entrega)
            self.pedidos.append(pedido)

            print("\nPedido registrado correctamente.")
            print(pedido.mostrar())

        except ValueError as e:
            print(f"\nError de validación: {e}")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

    def listar_pedidos(self):
        if not self.pedidos:
            print("\nNo hay pedidos registrados.")
            return

        print("\n--- Lista de Pedidos ---")
        for pedido in self.pedidos:
            print(pedido.mostrar())

    def buscar_por_cliente(self):
        nombre = input("Ingrese el nombre del cliente a buscar: ").strip().lower()
        encontrados = [p for p in self.pedidos if p.cliente.lower() == nombre]

        if encontrados:
            print("\nPedidos encontrados:")
            for pedido in encontrados:
                print(pedido.mostrar())
        else:
            print("\nNo se encontraron pedidos para ese cliente.")

    def cambiar_estado(self):
        codigo = input("Ingrese el código del pedido: ").strip().upper()
        for pedido in self.pedidos:
            if pedido.codigo == codigo:
                nuevo_estado = input("Ingrese el nuevo estado (Pendiente/En proceso/Entregado): ").strip()
                if not nuevo_estado:
                    print("El estado no puede estar vacío.")
                    return
                pedido.estado = nuevo_estado
                print("\nEstado actualizado correctamente.")
                print(pedido.mostrar())
                return

        print("\nPedido no encontrado.")

    def menu(self):
        while True:
            print("\n=== SISTEMA DE PEDIDOS DE PASTELERÍA ===")
            print("1. Registrar pedido")
            print("2. Listar pedidos")
            print("3. Buscar pedido por cliente")
            print("4. Cambiar estado de pedido")
            print("5. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_pedido()
            elif opcion == "2":
                self.listar_pedidos()
            elif opcion == "3":
                self.buscar_por_cliente()
            elif opcion == "4":
                self.cambiar_estado()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    app = PasteleriaApp()
    app.menu()