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

import pygame
import math
import sys
from enum import Enum

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
            return True
        else:
            print("El barco no tiene munición")
            return False
    
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
    
    def actualizar_posicion(self):
        """Actualiza la posición según velocidad y rumbo"""
        radianes = math.radians(self.rumbo)
        self.posicionX += self.velocidad * math.cos(radianes) * 0.1
        self.posicionY -= self.velocidad * math.sin(radianes) * 0.1


class SimuladorBarcos:
    def __init__(self):
        pygame.init()
        self.ancho = 1200
        self.alto = 700
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Simulador de Barcos")
        self.reloj = pygame.time.Clock()
        self.fuente_grande = pygame.font.Font(None, 24)
        self.fuente_pequena = pygame.font.Font(None, 18)
        
        # sonido
        try:
            self.sonido_disparo = pygame.mixer.Sound("disparo.wav")
        except:
            print("Advertencia: No se encontró disparo.wav")
            self.sonido_disparo = None
        
        try:
            pygame.mixer.music.load("fondo.mp3")
            pygame.mixer.music.play(-1)
        except:
            print("Advertencia: No se encontró fondo.mp3")
        
        self.barcos = [
            Barco("b1", 100, 100, 5, 45, 50),
            Barco("B2", 300, 200, 8, 120, 75),
            Barco("b3", 500, 150, 3, 270, 100)
        ]
        self.barco_activo = 0
        self.ejecutando = True
    
    def dibujar_barco(self, barco, x, y, es_activo=False):
        """Dibuja un barco como un triángulo rotado"""
        radianes = math.radians(barco.rumbo)
        tamaño = 20
        
        
        puntos = [
            (0, -tamaño),
            (-tamaño//2, tamaño),
            (tamaño//2, tamaño)
        ]
        
    
        puntos_rotados = []
        for px, py in puntos:
            px_rot = px * math.cos(radianes) - py * math.sin(radianes)
            py_rot = px * math.sin(radianes) + py * math.cos(radianes)
            puntos_rotados.append((x + px_rot, y + py_rot))
        
        # Dibujar barco
        color = (0, 255, 0) if es_activo else (100, 150, 200)
        pygame.draw.polygon(self.pantalla, color, puntos_rotados)
        
        # Dibujar borde si está activo
        if es_activo:
            pygame.draw.polygon(self.pantalla, (255, 255, 0), puntos_rotados, 2)
    
    def dibujar_interfaz(self):
        """Dibuja los controles de la interfaz"""
        ancho_panel = 300
        self.pantalla.fill((30, 30, 30), (self.ancho - ancho_panel, 0, ancho_panel, self.alto))
        
        x = self.ancho - ancho_panel + 15
        y = 15
        
        
        titulo = self.fuente_grande.render("CONTROL DE BARCOS", True, (255, 255, 255))
        self.pantalla.blit(titulo, (x, y))
        y += 40
        
        # Selector de barco
        selector = self.fuente_grande.render(f"Barco Activo: {self.barco_activo + 1}", True, (100, 255, 100))
        self.pantalla.blit(selector, (x, y))
        y += 35
        
        barco = self.barcos[self.barco_activo]
        
        # Info del barco
        info_y = y
        info_textos = [
            f"Nombre: {barco.nombre}",
            f"Pos: ({barco.posicionX:.1f}, {barco.posicionY:.1f})",
            f"Velocidad: {barco.velocidad} km/h",
            f"Rumbo: {barco.rumbo}°",
            f"Munición: {barco.numeroMunicion}"
        ]
        
        for texto in info_textos:
            superficie = self.fuente_pequena.render(texto, True, (200, 200, 200))
            self.pantalla.blit(superficie, (x, info_y))
            info_y += 25
        
        y = info_y + 20
        
        # Botones
        self.botones = [
            ("◄ Anterior", x, y, ancho_panel - 30),
            ("Siguiente ►", x, y + 35, ancho_panel - 30),
            ("✚ Nuevo Barco", x, y + 70, ancho_panel - 30),
            ("➕ Velocidad", x, y + 105, ancho_panel - 30),
            ("➖ Velocidad", x, y + 140, ancho_panel - 30),
            ("↻ Rumbo +", x, y + 175, ancho_panel - 30),
            ("↺ Rumbo -", x, y + 210, ancho_panel - 30),
            ("d Disparar", x, y + 245, ancho_panel - 30),
            ("+10 Munición", x, y + 280, ancho_panel - 30)
        ]
        
        for texto, bx, by, ancho in self.botones:
            pygame.draw.rect(self.pantalla, (50, 100, 150), (bx, by, ancho, 30))
            superficie = self.fuente_pequena.render(texto, True, (255, 255, 255))
            self.pantalla.blit(superficie, (bx + 5, by + 7))
    
    def manejar_clicks(self, pos):
        """Maneja los clicks del ratón en los botones"""
        for i, (texto, x, y, ancho, *_) in enumerate(self.botones):
            if x <= pos[0] <= x + ancho and y <= pos[1] <= y + 30:
                if i == 0:  # Anterior
                    self.barco_activo = (self.barco_activo - 1) % len(self.barcos)
                elif i == 1:  # Siguiente
                    self.barco_activo = (self.barco_activo + 1) % len(self.barcos)
                elif i == 2:  # Nuevo barco
                    self.nuevo_barco()
                elif i == 3:  # Velocidad +
                    self.barcos[self.barco_activo].setVelocidad(self.barcos[self.barco_activo].velocidad + 1)
                elif i == 4:  # Velocidad -
                    self.barcos[self.barco_activo].setVelocidad(self.barcos[self.barco_activo].velocidad - 1)
                elif i == 5:  # Rumbo +
                    nuevo_rumbo = (self.barcos[self.barco_activo].rumbo + 10) % 360
                    self.barcos[self.barco_activo].setRumbo(nuevo_rumbo if nuevo_rumbo != 0 else 1)
                elif i == 6:  # Rumbo -
                    nuevo_rumbo = (self.barcos[self.barco_activo].rumbo - 10) % 360
                    self.barcos[self.barco_activo].setRumbo(nuevo_rumbo if nuevo_rumbo != 0 else 1)
                elif i == 7:  # Disparar
                    if self.barcos[self.barco_activo].disparar():
                        if self.sonido_disparo:
                            self.sonido_disparo.play()
                elif i == 8:  # Munición
                    self.barcos[self.barco_activo].numeroMunicion += 10
    
    def nuevo_barco(self):
        """Crea un nuevo barco con valores por defecto"""
        nombre = f"Barco_{len(self.barcos) + 1}"
        nuevo = Barco(nombre, 200, 200, 5, 90, 50)
        self.barcos.append(nuevo)
        self.barco_activo = len(self.barcos) - 1
    
    def actualizar(self):
        """Actualiza la posición de los barcos"""
        for barco in self.barcos:
            barco.actualizar_posicion()
            
            
            if barco.posicionX < 0 or barco.posicionX > self.ancho - 300:
                barco.rumbo = 360 - barco.rumbo
            if barco.posicionY < 0 or barco.posicionY > self.alto:
                barco.rumbo = 180 - barco.rumbo
    
    def ejecutar(self):
        """Loop principal"""
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_clicks(evento.pos)
            
            self.actualizar()
            
            
            self.pantalla.fill((20, 40, 60))
            
            # Área del mar
            for barco in self.barcos:
                es_activo = self.barcos.index(barco) == self.barco_activo
                self.dibujar_barco(barco, barco.posicionX, barco.posicionY, es_activo)
            
            # Interfaz
            self.dibujar_interfaz()
            
            pygame.display.flip()
            self.reloj.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    simulador = SimuladorBarcos()
    simulador.ejecutar()