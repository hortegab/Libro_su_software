# Este es un ejemplo solo para practicar objetos
# Este codigo esta guardodo como objeto_ej2.py en:
# https://sites.google.com/saber.uis.edu.co/comdig/sw

class A:
    def __init__(self, in0, in1):

        # use "self" cuando una variable sea global (se puede invocar desde fuera de la funcion)
        self.in0=in0  
        self.in1=in1
        print("soy el constructor de la clase y aparezco cada vez que se crea un nuevo objeto")

    print ('Yo soy la clase y me ejecuto solo una vez.')
    
    # Las funciones dentro de una clase pueden tener el parametro self para permitir
    # definir variables globales
    def funcionb(self):
        print 'soy una funcion del objeto. Aparezco todas las veces que me llamen'

miprimerobjeto = A(3,7)
miprimerobjeto.funcionb()
miprimerobjeto.funcionb()
miprimerobjeto.funcionb()
miprimerobjeto.funcionb()

misegundoobjeto = A(3,7)
misegundoobjeto.funcionb()