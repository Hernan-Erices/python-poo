class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self): # Método dunder para representar el objeto como una cadena
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    def __repr__(self): # Método dunder para representar el objeto de manera más detallada
        return f'Persona("{self.nombre}", {self.edad})'
    def __add__(self, otro): # Método dunder para sumar dos objetos Persona
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + " y " + otro.nombre, nuevo_valor)
        
jano = Persona("Jano", 20)
perdro = Persona("Pedro", 30)

resultado = jano + perdro  # Utiliza el método __add__ para sumar las edades
print(resultado)  # Imprime: Nombre: Jano y Pedro, Edad: 50
print(resultado.edad)  # Imprime: 50
print(resultado.nombre)  # Imprime: Jano y Pedro

#print(jano)  # Imprime: Nombre: Jano, Edad: 20

#repe = repr(jano)  # Obtiene la representación detallada del objeto
#resultado = eval(repe)  # Evalúa la representación para crear un nuevo objeto
#print(resultado)  # Imprime: Persona(Jano, 20)