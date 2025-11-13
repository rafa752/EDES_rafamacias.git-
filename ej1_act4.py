class Barco:
    def __init__(self, nombre, posicionX, posicionY, velocidad, rumbo, numeroMunicion):
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.velocidad = velocidad if 0 <= velocidad <= 20 else 0
        self.rumbo = rumbo if 1 <= rumbo <= 359 else 1
        self.numeroMunicion = numeroMunicion
    
    def __str__(self):
        return f"Barco: {self.nombre} | Posición: ({self.posicionX}, {self.posicionY}) | Velocidad: {self.velocidad} km/h | Rumbo: {self.rumbo}° | Munición: {self.numeroMunicion}"
    
    def disparar(self):
        if self.numeroMunicion > 0:
            print("El barco ha disparado")
            self.numeroMunicion -= 1
        else:
            print("El barco no tiene munición")
    
    def setVelocidad(self, nueva_velocidad):
        if 0 <= nueva_velocidad <= 20:
            self.velocidad = nueva_velocidad
        else:
            print("La velocidad debe estar entre 0 y 20 km/h")
    
    def setRumbo(self, nuevo_rumbo):
        if 1 <= nuevo_rumbo <= 359:
            self.rumbo = nuevo_rumbo
        else:
            print("El rumbo debe estar entre 1 y 359 grados")


#3 Barco y probar sus métodos
barco1 = Barco("b1", 10, 20, 15, 45, 50)
barco2 = Barco("B2", 30, 40, 18, 120, 75)
barco3 = Barco("b3", 5, 15, 12, 270, 100)

print(" BARCO 1 ")
print("Antes:", barco1)
barco1.disparar()
barco1.setVelocidad(20)
barco1.setRumbo(90)
print("Después:", barco1)

print("\n BARCO 2 ")
print("Antes:", barco2)
barco2.disparar()
barco2.disparar()
barco2.setVelocidad(10)
barco2.setRumbo(200)
print("Después:", barco2)

print("\n BARCO 3 ")
print("Antes:", barco3)
barco3.disparar()
barco3.setVelocidad(5)
barco3.setRumbo(315)
print("Después:", barco3)