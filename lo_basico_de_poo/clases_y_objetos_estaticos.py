#para nombrar las clases en Python POO se usa pascal case (InicioDeCadaLetraDeCadaPalabraEnMayuscula)
class Celular():
    #estos son atributos estaticos
    marca = "Samsung" 
    modelo = "S23"
    camara = "48MP"
    
celular_1 = Celular() #ahora celular_1 es un objeto (también llamado instancia) de la clase Celular
print(celular_1.marca)