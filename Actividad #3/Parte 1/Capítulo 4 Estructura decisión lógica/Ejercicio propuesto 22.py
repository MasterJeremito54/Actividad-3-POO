import tkinter as tk
from tkinter import messagebox


class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_hora * self.horas_trabajadas


def calcular():
    try:
        nombre = entrada_nombre.get()
        salario_hora = float(entrada_salario_hora.get())
        horas_trabajadas = int(entrada_horas_trabajadas.get())

        if salario_hora < 0 or horas_trabajadas < 0:
            raise ValueError("El salario por hora y las horas trabajadas deben ser valores positivos.")

        empleado = Empleado(nombre, salario_hora, horas_trabajadas)
        salario_mensual = empleado.calcular_salario_mensual()

        if salario_mensual > 450000:
            messagebox.showinfo("Resultado", f"Empleado: {nombre}\nSalario Mensual: ${salario_mensual:.2f}")
        else:
            messagebox.showinfo("Resultado", f"Empleado: {nombre}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Cálculo Salario Mensual")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Salario por Hora:").grid(row=1, column=0, padx=10, pady=10)
entrada_salario_hora = tk.Entry(ventana)
entrada_salario_hora.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Horas Trabajadas:").grid(row=2, column=0, padx=10, pady=10)
entrada_horas_trabajadas = tk.Entry(ventana)
entrada_horas_trabajadas.grid(row=2, column=1, padx=10, pady=10)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()