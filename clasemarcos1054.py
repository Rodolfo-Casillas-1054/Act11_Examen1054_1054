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
        coloresmarcos = ["Negros", "Blancos", "Azules", "Dorados", "Rojos"]
        for x in coloresmarcos:
            print(x)

    def mi_Tupla(self):
        materialesmarcos = ("Madera", "Metalicos", "Plastico", "Aluminio", "oro")
        for y in materialesmarcos:
            print(y)

    def mi_Diccionario(self):
        diccionarioctamaños = {
            "20 x 20 cm: ": 1000,
            "20 x 40 cm: ": 1100,
            "40 x 40 cm: ": 1200,
            "60 x 20 cm: ": 1300,
            "80 x 350 cm: ": 1400
        }
        for x, y in diccionarioctamaños.items():
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