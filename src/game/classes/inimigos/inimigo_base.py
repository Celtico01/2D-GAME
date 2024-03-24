from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rand

class inimigo_base:
    def __init__(self, inimigos, largura, altura):
        self.largura = largura
        self.altura = altura
        self.velocidade = 2.5
        self.inimigos = inimigos
        self.tamanho = 20
        self.vida = 1
        self.dano = 1

        side = rand.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.x = rand.uniform(-self.largura * 0.2, self.largura * 0.2)
            self.y = self.altura + 20
        elif side == "bottom":
            self.x = rand.uniform(-self.largura * 0.2, self.largura * 0.2)
            self.y = -self.altura - 20
        elif side == "left":
            self.x = -self.largura - 20
            self.y = rand.uniform(-self.altura * 0.2, self.altura * 0.2)
        else: #right
            self.x = self.largura + 20
            self.y = rand.uniform(-self.altura * 0.2, self.altura * 0.2)

    def draw(self):
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - self.tamanho / 2, self.y - self.tamanho / 2)
        glVertex2f(self.x + self.tamanho / 2, self.y - self.tamanho / 2)
        glVertex2f(self.x + self.tamanho / 2, self.y + self.tamanho / 2)
        glVertex2f(self.x - self.tamanho / 2, self.y + self.tamanho / 2)
        glEnd()


    #implementar essa e waypoint depois
    def update(self, player):
        if self.x < player.x:
            self.x += self.velocidade
        elif self.x > player.x:
            self.x -= self.velocidade
        if self.y < player.y:
            self.y += self.velocidade
        elif self.y > player.y:
            self.y -= self.velocidade

        