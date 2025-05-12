# Atributos son variables que pertenecen a una clase

# Definición de la clase Celular
class Celular:
    
    # Método constructor que se ejecuta al crear una nueva instancia de la clase
    def __init__(self, marca, modelo, camara):
        # Asignación de los parámetros recibidos a atributos del objeto
        self.marca = marca      # Atributo para almacenar la marca del celular
        self.modelo = modelo    # Atributo para almacenar el modelo del celular
        self.camara = camara   # Atributo para almacenar la cámara del celular

# Creación de dos objetos (instancias) de la clase Celular con diferentes valores
celular_1 = Celular("Samsung", "s23", "48MP")
celular_2 = Celular("Apple", "Iphone 15 pro", "108MP")

# Imprime el atributo 'modelo' del objeto 'celular_2', que es "Iphone 15 pro"
print(celular_2.modelo)