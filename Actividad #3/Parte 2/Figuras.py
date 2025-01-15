import math
from tkinter import *

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Circulo:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.radio = DoubleVar()
        Label(frame, text="Radio del circulo:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")
        Entry(frame, textvariable=self.radio).grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        area = math.pi * self.radio.get() ** 2
        perimetro = 2 * math.pi * self.radio.get()
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")

class Rectangulo:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.base = DoubleVar()
        self.altura = DoubleVar()
        Label(frame, text="Base del rectangulo:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.base).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Altura del rectangulo:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.altura).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        area = self.base.get() * self.altura.get()
        perimetro = 2 * (self.base.get() + self.altura.get())
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")

class Cuadrado:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.lado = DoubleVar()
        Label(frame, text="Lado del cuadrado:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.lado).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        area = self.lado.get() ** 2
        perimetro = 4 * self.lado.get()
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")

class TrianguloRectangulo:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.base = DoubleVar()
        self.altura = DoubleVar()
        Label(frame, text="Base del triangulo:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.base).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Altura del triangulo:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.altura).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        base = self.base.get()
        altura = self.altura.get()
        hipotenusa = math.sqrt(base ** 2 + altura ** 2)
        area = (base * altura) / 2
        perimetro = base + altura + hipotenusa
        tipo_triangulo = self.determinar_tipo_de_triangulo(base, altura, hipotenusa)
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"El triangulo es: {tipo_triangulo}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=5, column=0, columnspan=2, sticky="nsew")

    def determinar_tipo_de_triangulo(self, base, altura, hipotenusa):
        if math.isclose(base, altura) and math.isclose(base, hipotenusa):
            return "Equilátero"
        elif not math.isclose(base, altura) and not math.isclose(base, hipotenusa) and not math.isclose(altura, hipotenusa):
            return "Escaleno"
        else:
            return "Isósceles"
        
class Rombo:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.diagonal_1 = DoubleVar()
        self.diagonal_2 = DoubleVar()
        Label(frame, text="Diagonal 1:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.diagonal_1).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Diagonal 2:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.diagonal_2).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        area = (self.diagonal_1.get() * self.diagonal_2.get()) / 2
        lado = math.sqrt((self.diagonal_1.get() / 2) ** 2 + (self.diagonal_2.get() / 2) ** 2)
        perimetro = 4 * lado
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")

class Trapecio:
    def __init__(self, frame):
        limpiar_frame(frame)
        self.base_1 = DoubleVar()
        self.base_2 = DoubleVar()
        self.altura = DoubleVar()
        self.lado_1 = DoubleVar()
        self.lado_2 = DoubleVar()
        Label(frame, text="Base 1:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.base_1).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Base 2:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.base_2).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Altura:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.altura).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Lado 1:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.lado_1).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        Label(frame, text="Lado 2:", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        Entry(frame, textvariable=self.lado_2).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Calcular", command=self.calcular, bg="#800000", fg="#ffffff").grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular(self):
        area = ((self.base_1.get() + self.base_2.get()) * self.altura.get()) / 2
        perimetro = self.base_1.get() + self.base_2.get() + self.lado_1.get() + self.lado_2.get()
        Label(frame2, text=f"Area: {area:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        Label(frame2, text=f"Perimetro: {perimetro:.2f}", bg="#ffdab9", fg="#800000", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="nsew")

        
ventana = Tk()
ventana.title("Figuras Geometricas")
ventana.geometry("600x400")
ventana.configure(bg="#ffdab9")

frame1 = Frame(ventana, bg="#ffdab9", relief="sunken", borderwidth=2)
frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

frame2 = Frame(ventana, bg="#ffdab9", relief="sunken", borderwidth=2)
frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

Label(frame1, text="Seleccione la figura a calcular:", bg="#ffdab9", fg="#800000", font=("Arial", 14, "bold")).pack(pady=10)

def mostrar_circulo():
    Circulo(frame2)

def mostrar_rectangulo():
    Rectangulo(frame2)

def mostrar_cuadrado():
    Cuadrado(frame2)

def mostrar_triangulo_rectangulo():
    TrianguloRectangulo(frame2)

def mostrar_rombo():
    Rombo(frame2)

def mostrar_trapecio():
    Trapecio(frame2)

Button(frame1, text="Circulo", command=mostrar_circulo, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)
Button(frame1, text="Rectangulo", command=mostrar_rectangulo, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)
Button(frame1, text="Cuadrado", command=mostrar_cuadrado, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)
Button(frame1, text="Triangulo Rectangulo", command=mostrar_triangulo_rectangulo, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)
Button(frame1, text="Rombo", command=mostrar_rombo, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)
Button(frame1, text="Trapecio", command=mostrar_trapecio, bg="#800000", fg="#ffffff", font=("Arial", 12)).pack(fill=X, padx=10, pady=5)

ventana.mainloop()
