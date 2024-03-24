from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Bullet:
    def __init__(self, x, y, direcao, dano):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.velocidade = 5 # pode ser mudado!
        self.tamanho = 5 # pode ser mudado!
        self.dano = dano
    
    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - self.tamanho / 2, self.y - self.tamanho / 2)
        glVertex2f(self.x + self.tamanho / 2, self.y - self.tamanho / 2)
        glVertex2f(self.x + self.tamanho / 2, self.y + self.tamanho / 2)
        glVertex2f(self.x - self.tamanho / 2, self.y + self.tamanho / 2)
        glEnd()

    def update(self):
        if self.direcao == "UP":
            self.y += self.velocidade
        elif self.direcao == "DOWN":
            self.y -= self.velocidade
        elif self.direcao == "LEFT":
            self.x -= self.velocidade
        elif self.direcao == "RIGHT":
            self.x += self.velocidade
        elif self.direcao == "UP_LEFT":
            self.x -= self.velocidade
            self.y += self.velocidade
        elif self.direcao == "UP_RIGHT":
            self.x += self.velocidade
            self.y += self.velocidade
        elif self.direcao == "DOWN_LEFT":
            self.x -= self.velocidade
            self.y -= self.velocidade
        elif self.direcao == "DOWN_RIGHT":
            self.x += self.velocidade
            self.y -= self.velocidade