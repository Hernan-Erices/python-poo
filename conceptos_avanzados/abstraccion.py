class Auto():
    def __init__(self):
        self._estado = "apagado"
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido.")
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("El auto está en modo de conducción.")
            
mi_auto = Auto()
mi_auto.conducir()  # El auto se enciende y entra en modo de conducción

#abstracion es un concepto de programación orientada a objetos que permite ocultar los detalles de implementación y mostrar solo las características esenciales de un objeto.
# En este ejemplo, la clase Auto tiene un método encender que cambia el estado del auto a "encendido" y un método conducir que verifica el estado del auto antes de permitir la conducción.