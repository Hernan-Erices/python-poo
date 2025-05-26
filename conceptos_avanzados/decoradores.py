def decorador(funcion): 
    def funcion_modificada():
        print("Antes de llamar a la función") 
        funcion() # Llamada a la función original
        print("Después de llamar a la función") 
    return funcion_modificada 


# def saludo(): 
#     print("¡Hola, mundo!") 
    
# decorador_saludo = decorador(saludo)
# decorador_saludo()
 
@decorador # Decorador aplicado directamente
def saludo(): 
    print("¡Hola, mundo!")
    
saludo()

# Salida esperada:
# Antes de llamar a la función
# ¡Hola, mundo!