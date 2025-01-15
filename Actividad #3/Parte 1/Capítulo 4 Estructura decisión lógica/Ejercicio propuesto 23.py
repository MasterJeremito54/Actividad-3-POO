import tkinter as tk
from tkinter import messagebox
import math

class EcuacionCuadratica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Ecuaciones Cuadráticas")

        self.entrada_A = tk.Entry(ventana)
        self.entrada_A.grid(row=0, column=1)
        tk.Label(ventana, text="A:").grid(row=0, column=0)

        self.entrada_B = tk.Entry(ventana)
        self.entrada_B.grid(row=1, column=1)
        tk.Label(ventana, text="B:").grid(row=1, column=0)

        self.entrada_C = tk.Entry(ventana)
        self.entrada_C.grid(row=2, column=1)
        tk.Label(ventana, text="C:").grid(row=2, column=0)

        tk.Button(ventana, text="Calcular", command=self.calcular).grid(row=3, column=0, columnspan=2)

    def calcular(self):
        try:
            A = float(self.entrada_A.get())
            B = float(self.entrada_B.get())
            C = float(self.entrada_C.get())

            if A == 0:
                raise ValueError("El valor de A no puede ser 0. Esto no es una ecuacion de segundo grado.")

            discriminante = B**2 - 4*A*C

            if discriminante > 0:
                x1 = (-B + math.sqrt(discriminante)) / (2 * A)
                x2 = (-B - math.sqrt(discriminante)) / (2 * A)
                messagebox.showinfo("Resultado", f"Las soluciones son reales y distintas:\n x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif discriminante == 0:
                x = -B / (2 * A)
                messagebox.showinfo("Resultado", f"Las soluciones son reales e iguales:\n x1 = x2 = {x:.2f}")
            else:
                real = -B / (2 * A)
                imaginaria = math.sqrt(abs(discriminante)) / (2 * A)
                messagebox.showinfo("Resultado", f"Las soluciones son complejas:\n x1 = {real:.2f} + {imaginaria:.2f}i\n x2 = {real:.2f} - {imaginaria:.2f}i")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    ventana = tk.Tk()
    app = EcuacionCuadratica(ventana)
    ventana.mainloop()