class Estudiante:
    

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("estudiando...")

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
grado = input("Dime tu grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      El estudiante se llama: {estudiante.nombre}
      El estudiante tiene : {estudiante.edad} anios
      El estudiante esta: {estudiante.grado} grado
      """)

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        
    break