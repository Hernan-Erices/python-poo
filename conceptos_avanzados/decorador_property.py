class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property #decorador property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #decorador setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter #decorador deleter
    def nombre(self):
        del self.__nombre
        
jano = Persona("Jano", 20)

nombre = jano.nombre # Llamamos al método nombre (sigue siendo un getter) para obtener el nombre de la persona
# Nota: No se usa paréntesis porque es un decorador property, no un método normal
print(nombre)

#jano.nombre = "Jano2" # Llamamos al método nombre (sigue siendo un setter) para cambiar el nombre de la persona

del jano.nombre # Llamamos al método deleter para eliminar el nombre de la persona


nombre = jano.nombre # Llamamos al método nombre (sigue siendo un setter) para cambiar el nombre de la persona
print(nombre)
