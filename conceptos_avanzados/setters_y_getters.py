class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self): #aqui definimos un getter con 'get_'xxxxxx podemos acceder a datos privados "_" y muy privados "__"
        return self.__nombre

    def set_nombre(self, new_nombre): #esto es un setter lo definimos con 'set_'
        self.__nombre = new_nombre
    

jano = Persona("Jano", 23)

nombre = jano.get_nombre()
print(nombre)

jano.set_nombre("Janitro")
nombre = jano.get_nombre()
print(nombre)


#Getter: método que devuelve el valor de un atributo.
#Setter: método que asigna un nuevo valor a un atributo, usualmente con validación.