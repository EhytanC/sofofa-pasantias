#Metodo constructor

class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {} años\n'.format(self.nombre,self.año)
    
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)

doctor = Persona('Jose',25)
print(doctor.descripcion(), doctor.comentario('Hola esta es una prueba para entender la programacion orientada a objetos'))

print('#'*50)
#Cambiar un atributo

class Email:
    pass
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

print('Antes de modificar: ', mi_correo.enviado)
mi_correo.enviar_correo()
print('Despues de modificar: ', mi_correo.enviado)

print('#'*50)
#Herencia

class Pokemon:
    pass
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre #str
        self.tipo = tipo #str
    
    def descripcion(self):
        return '{} es un pokemon tipo: {}'.format(self.nombre, self.tipo)

    def dar_opinion(self, opinion):
        return '{} opina que: {}'.format(self.nombre, opinion)

#Son hijos de la clase pokemon:

class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} Ataco con: {}'.format(self.nombre, tipo_ataque)

class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} Ataco con: {}'.format(self.nombre, tipo_ataque)

nuevo_pokemon = Pikachu('Slowpoke', 'Agua, Psiquico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Chorro de agua'))
print(nuevo_pokemon.dar_opinion('Le quiten los derechos a los negros'))