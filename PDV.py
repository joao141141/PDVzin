import tkinter as tk
class PdvApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDV - Ponto de Venda")

        self.total_price = 0
        self.items = []

        self.create_widgets()

    def create_widgets(self):
        # Frame para os produtos
        products_frame = tk.Frame(self.root)
        products_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Adiciona alguns produtos de exemplo
        product_list = [
            {"name": "Produto 1", "price": 10.0},
            {"name": "Produto 2", "price": 15.0},
            {"name": "Produto 3", "price": 20.0},
        ]

        for product in product_list:
            btn = tk.Button(products_frame, text=f"{product['name']} - R${product['price']:.2f}", command=lambda p=product: self.add_to_cart(p))
            btn.pack(fill=tk.X, pady=5)

        # Frame para o carrinho
        cart_frame = tk.Frame(self.root)
        cart_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.cart_label = tk.Label(cart_frame, text="Carrinho de Compras")
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(cart_frame, height=10, width=40)
        self.cart_listbox.pack()

        self.total_label = tk.Label(cart_frame, text="Total: R$0.00")
        self.total_label.pack()

        # Botão para finalizar a compra
        checkout_btn = tk.Button(cart_frame, text="Finalizar Compra", command=self.checkout)
        checkout_btn.pack(pady=10)

    def add_to_cart(self, product):
        self.items.append(product)
        self.total_price += product["price"]

        self.cart_listbox.insert(tk.END, f"{product['name']} - R${product['price']:.2f}")
        self.update_total_label()

    def update_total_label(self):
        self.total_label.config(text=f"Total: R${self.total_price:.2f}")

    def checkout(self):
        # Implementar a lógica de pagamento aqui
        # Por exemplo, imprimir um recibo ou enviar uma confirmação de pagamento

        # Limpa o carrinho após o pagamento
        self.items = []
        self.total_price = 0

        self.cart_listbox.delete(0, tk.END)
        self.update_total_label()
        self.cart_label.config(text="Compra finalizada. Obrigado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PdvApp(root)
    root.mainloop()

    