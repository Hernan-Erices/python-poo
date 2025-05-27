from abc import ABC, abstractmethod

class Persona(ABC): # Clase abstracta
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.sexo}.")
        
#jano = Persona("Jano", 20, "masculino", "programador")  # Esto generará un error porque Persona es abstracta


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):  # Eliminar el método __init__ para evitar error de herencia
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando para mis exámenes: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):  # Eliminar el método __init__ para evitar error de herencia
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando como {self.actividad}")

jano = Estudiante("Jano", 20, "masculino", "programacion")  # Ahora no generará error
jano2 = Trabajador("Jano", 20, "masculino", "programador")  # Ahora no generará error

jano.presentarse()
jano.hacer_actividad()
jano2.presentarse()
jano2.hacer_actividad()