print("Act 11 Examen")
print("Rodolfo Casillas 22308051281054\n")

# Zona de clases
class Alumno1054:
    # Zona de atributos
    aidi = 0
    medidas = " "
    material = " "
    diseño = " "
    precio = 0
    tiempo = 0
    proteccion = " "

    # Zona de funciones dentro de la clase
    def mi_Lista(self):
        lista_alumnos = ["Rodolfo", "Diana", "Najera", "Azul", "Andy"]
        for x in lista_alumnos:
            print(x)

    def mi_Tupla(self):
        Tupla_Edadperros = ("Nava", "Meza", "Tontolin", "Aldahir", "Bena")
        for y in Tupla_Edadperros:
            print(y)

    def mi_Diccionario(self):
        diccionariocolor = {
            "Sociales: ": 9,
            "Fisica: ": 9,
            "Programacion: ": 9,
            "Calculo: ": 9,
            "Ingles: ": 9
        }
        for x, y in diccionariocolor.items():
            print(x, y)

    def mostrardatos(self):
        print(f"Id del producto: {self.aidi}")
        print(f"Medidas en centimetros cuadrados: {self.medidas}")
        print(f"Material: {self.material}")
        print(f"Diseño: {self.diseño}")
        print(f"Precio en pesos: {self.precio}")
        print(f"Tiempo en dias: {self.tiempo}")
        print(f"Protección: {self.proteccion}")

    def altas(self):
        print("El registro se realizo correctamente")
        
    def bajas(self):
        print("El registro no se realizo correctamente")
        
# Zona de creación de objetos
Rodolfo = Alumno1054()

# Asignación de valores a los atributos del objeto Rodolfo
Rodolfo.aidi = 16
Rodolfo.medidas = 150
Rodolfo.material = "Madera"
Rodolfo.diseño = "Grabado"
Rodolfo.precio = 1200
Rodolfo.tiempo = 2
Rodolfo.proteccion = "Barniz"

# Usando el objeto Rodolfo para mostrar la información
print("\nListado de alumnos")
Rodolfo.mi_Lista()
print("\nListado de materias")
Rodolfo.mi_Diccionario()
print("\nListado de maestros")
Rodolfo.mi_Tupla()
print("\nResultados")
Rodolfo.mostrardatos()
print("  ")
Rodolfo.altas()
print("  ")
Rodolfo.bajas()