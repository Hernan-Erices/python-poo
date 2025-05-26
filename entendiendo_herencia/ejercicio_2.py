#Herencia ejercicio 2
# Ejercicio de herencia y uso de super:
# Crear un sistema para una escuela. En este sistema, vamos atener dos clases
# principales: Persona y Estudiante. La clase Persona tendra los atributos de
# nombre y edad y un metodo que imprima el nombre y la edad de la persona. La
# clase Estudiante heredara de la clase Persona y tambien tendra un atributo
# adicional: grado y un metodo que imprima el grado del estudiante.

# Deberas utilizar super en el motodo de inicializacion (init) para reutilizar
# el codigo de la clase padre (Persona). Luego crea una instancia de clase Estudiante
# e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funciona correctamente.


class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def metodo(self):
        print(f"tu edad es {self.edad} y tu nombre es: {self.nombre}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def grado_estudiante(self):
        print(f"el grado del estudiante es: {self.grado}")
        

Jano = Estudiante("Jano", "25", "4to grado")

Jano.grado_estudiante()



#Ejercicio de herencia multiple y MRO:
# Imagina que estas modelando animales en un zoologico. Crea tres clases:
# "Animal", "Mamifero" y "Ave". La clase "Animal" debe tener un metodo llamado
# "comer". La clase "Mamifero" debe tener un metodo llamado "amamantar" y la clase
# "Ave" un metodo llamado "volar"
#
# Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave". en ese orden
# y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer"

# Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa como
# cambia el MRO y el comportamineto de los metodos al usar super().


class Animal():
    def comer(self):
        print("comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("amamantando...")

class Ave(Animal):
    def volar(self):
        print("volando...")
        
        
class Murcielago(Mamifero, Ave):
    def __init__(self):
        pass
    
    
Murcielado_1 = Murcielago()
Murcielado_1.amamantar()
Murcielado_1.comer()
Murcielado_1.volar()


print(Murcielago.mro())