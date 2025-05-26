class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("estoy hablando")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

#herencia multiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print (f'hola soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en: {self.empresa}')





jano = EmpleadoArtista("Jano", 23, "chileno", "cantar", "1M", "gugul")

jano.presentarse()

#saber si se hereda o si se instancia True o False
herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(jano, EmpleadoArtista)

print(herencia)
print(instancia)