import tkinter as tk
from tkinter import messagebox

class Comparador:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Valores")

        tk.Label(root, text="Valor A:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_a = tk.Entry(root)
        self.entrada_a.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Valor B:").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_b = tk.Entry(root)
        self.entrada_b.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Comparar", command=self.comparar_numeros).grid(row=2, column=0, columnspan=2, pady=10)

    def comparar_numeros(self):
        try:
            A = int(self.entrada_a.get())
            B = int(self.entrada_b.get())

            if A > B:
                resultado = "A es mayor que B"
            elif A == B:
                resultado = "A es igual a B"
            else:
                resultado = "A es menor que B"

            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Comparador(root)
    root.mainloop()