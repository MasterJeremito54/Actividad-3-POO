import tkinter as tk
from tkinter import messagebox


class Matricula:
    def __init__(self, inscripcion, nombre, patrimonio, estrato):
        self.inscripcion = inscripcion
        self.nombre = nombre
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago(self):
        pago_base = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            pago_base += 0.03 * self.patrimonio
        return pago_base


def calcular():
    try:
        inscripcion = entrada_inscripcion.get()
        nombre = entrada_nombre.get()
        patrimonio = float(entrada_patrimonio.get())
        estrato = int(entrada_estrato.get())

        if patrimonio < 0 or estrato < 0:
            raise ValueError("El patrimonio y el estrato deben ser valores positivos.")

        estudiante = Matricula(inscripcion, nombre, patrimonio, estrato)
        pago = estudiante.calcular_pago()

        messagebox.showinfo("Resultado", f"Numero de Inscripcion: {inscripcion}\n"
                                         f"Nombre: {nombre}\n"
                                         f"Pago de Matricula: ${pago:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Calculo Pago Matricula")

tk.Label(ventana, text="Numero de Inscripcion:").grid(row=0, column=0, padx=10, pady=10)
entrada_inscripcion = tk.Entry(ventana)
entrada_inscripcion.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=10)
entrada_patrimonio = tk.Entry(ventana)
entrada_patrimonio.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Estrato:").grid(row=3, column=0, padx=10, pady=10)
entrada_estrato = tk.Entry(ventana)
entrada_estrato.grid(row=3, column=1, padx=10, pady=10)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()