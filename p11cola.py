"""Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
b. indicar el plantea natal de Luke Skywalker y Han Solo
c. insertar un nuevo personaje antes del maestro Yoda
d. eliminar el personaje ubicado después de Jar Jar Binks"""

class Personaje:
    def _init_(self, nombre, planeta_natal):
        self.nombre = nombre
        self.planeta_natal = planeta_natal

class Cola:
    def _init_(self):
        self.items = []

    def encolar(self, personaje):
        self.items.append(personaje)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]
        
    def insertar_en_posicion(self, personaje, posicion):
        self.items.insert(posicion, personaje)

    def eliminar_en_posicion(self, posicion):
        if 0 <= posicion < self.tamanio():
            self.items.pop(posicion)

    def mostrar(self):
        for personaje in self.items:
            print(f"Nombre: {personaje.nombre}, Planeta: {personaje.planeta_natal}")

def mostrar_personajes_por_planeta(cola, planetas):
    for personaje in cola.items:
        if personaje.planeta_natal in planetas:
            print(f"Nombre: {personaje.nombre}, Planeta: {personaje.planeta_natal}")

def mostrar_planeta_personajes(cola, nombres):
    for personaje in cola.items:
        if personaje.nombre in nombres:
            print(f"{personaje.nombre} es de {personaje.planeta_natal}")

def insertar_antes_de(cola, nombre_objetivo, nuevo_personaje):
    for i, personaje in enumerate(cola.items):
        if personaje.nombre == nombre_objetivo:
            cola.insertar_en_posicion(nuevo_personaje, i)
            break

def eliminar_despues_de(cola, nombre_objetivo):
    for i, personaje in enumerate(cola.items):
        if personaje.nombre == nombre_objetivo and i + 1 < cola.tamanio():
            cola.eliminar_en_posicion(i + 1)
            break

cola = Cola()

cola.encolar(Personaje('Luke Skywalker', 'Tatooine'))
cola.encolar(Personaje('Leia Organa', 'Alderaan'))
cola.encolar(Personaje('Han Solo', 'Corellia'))
cola.encolar(Personaje('Yoda', 'Dagobah'))
cola.encolar(Personaje('Jar Jar Binks', 'Naboo'))

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("\nPersonajes de Alderaan, Endor y Tatooine:")
mostrar_personajes_por_planeta(cola, ['Alderaan', 'Endor', 'Tatooine'])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("Planeta de Luke Skywalker y Han Solo:")
mostrar_planeta_personajes(cola, ['Luke Skywalker', 'Han Solo'])

# c. Insertar un nuevo personaje antes de Yoda
print("Insertar nuevo personaje antes de Yoda:")
nuevo_personaje = Personaje('Nuevo Personaje', 'Nuevo Planeta')
insertar_antes_de(cola, 'Yoda', nuevo_personaje)

# d. Eliminar el personaje después de Jar Jar Binks
print("Eliminar personaje después de Jar Jar Binks:")
eliminar_despues_de(cola, 'Jar Jar Binks')

# Mostrar la cola final
print("Cola final de personajes:")
cola.mostrar()