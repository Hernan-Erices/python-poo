#encapsulamiento

#El encapsulamiento es un principio de la POO que consiste en ocultar los detalles
# internos de un objeto y restringir el acceso directo a sus atributos o métodos, 
# permitiendo la interacción solo a través de una interfaz definida (como métodos públicos).


class MiClase:
    def __init__(self):
        self._atributo_privado = "valor" #definimos un atributo privado con un guion bajo "_"al inicio del nombre del atributo
        self.__atributo_muy_privado = "valo2" #definimos un atributo muy privado con 2 guiones bajo "__" al inicio del nombre atributo 


objecto = MiClase()
print(objecto._atributo_privado)
print(objecto.__atributo_muy_privado)