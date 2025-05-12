# un método es una función que está definida dentro de una clase y 
# que actúa sobre los objetos (instancias) de esa clase.

# Un método es una acción o comportamiento que puede realizar un objeto, 
# y tiene acceso a los atributos (datos) de ese objeto.

class Celular:
    

    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'estas haciendo un llamado desde un: {self.modelo}')
        
    def cortar(self):
        print("cortaste la llamada")

celular_1 = Celular("Samsung", "s23", "48MP")
celular_2 = Celular("Apple", "Iphone 15 pro", "108MP")


celular_1.llamar()