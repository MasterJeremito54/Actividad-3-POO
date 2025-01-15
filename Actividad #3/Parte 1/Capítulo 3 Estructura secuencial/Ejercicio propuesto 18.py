import tkinter as tk
from tkinter import messagebox




class Empleado:
    def __init__(self, codigo, nombre, horas_trabajadas_mes, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas_mes = horas_trabajadas_mes
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente


    def salario(self):
        retencion_fuente = self.retencion_fuente / 100
        salario_bruto = self.horas_trabajadas_mes * self.valor_hora
        salario_neto = salario_bruto * (1 - retencion_fuente)
        return salario_bruto, salario_neto




def calcular_salario():
    try:
        codigo = int(entrada_codigo.get())
        nombre = entrada_nombre.get()
        horas_trabajadas_mes = float(entrada_horas.get())
        valor_hora = float(entrada_valor_hora.get())
        retencion_fuente = float(entrada_retencion.get())


        empleado = Empleado(codigo, nombre, horas_trabajadas_mes, valor_hora, retencion_fuente)
        salario_bruto, salario_neto = empleado.salario()


        messagebox.showinfo("Resultados", f"Código: {empleado.codigo}\n"
                                          f"Nombre: {empleado.nombre}\n"
                                          f"Salario Bruto: {salario_bruto:.2f}\n"
                                          f"Salario Neto: {salario_neto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "ingresa valores válidos en todos los campos.")




ventana = tk.Tk()
ventana.title("Cálculo de Salario de Empleados")


etiqueta_codigo = tk.Label(ventana, text="Código del empleado:")
etiqueta_codigo.grid(row=0, column=0, padx=10, pady=5)
entrada_codigo = tk.Entry(ventana)
entrada_codigo.grid(row=0, column=1, padx=10, pady=5)


etiqueta_nombre = tk.Label(ventana, text="Nombre del empleado:")
etiqueta_nombre.grid(row=1, column=0, padx=10, pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=1, column=1, padx=10, pady=5)


etiqueta_horas = tk.Label(ventana, text="Horas trabajadas al mes:")
etiqueta_horas.grid(row=2, column=0, padx=10, pady=5)
entrada_horas = tk.Entry(ventana)
entrada_horas.grid(row=2, column=1, padx=10, pady=5)


etiqueta_valor_hora = tk.Label(ventana, text="Valor por hora:")
etiqueta_valor_hora.grid(row=3, column=0, padx=10, pady=5)
entrada_valor_hora = tk.Entry(ventana)
entrada_valor_hora.grid(row=3, column=1, padx=10, pady=5)


etiqueta_retencion = tk.Label(ventana, text="Retención en la fuente (%):")
etiqueta_retencion.grid(row=4, column=0, padx=10, pady=5)
entrada_retencion = tk.Entry(ventana)
entrada_retencion.grid(row=4, column=1, padx=10, pady=5)


boton_calcular = tk.Button(ventana, text="Calcular Salario", command=calcular_salario)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)


ventana.mainloop()
