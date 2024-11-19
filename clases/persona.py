
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} tengo {self.edad} años y soy {self.profesion}"
    
    def despedirse(self):
        return f"Adios, yo {self.nombre} con la edad {self.edad} me despido hasta la proxima"

saluda = Persona("Juan", 30, "Ingeniero")
print(saluda.saludar())

despide = Persona("Maria", 25, "Doctora")
print(despide.despedirse())