from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame


class Player:
    def __init__(self, largura_sc, altura_sc):
        self.x = 0
        self.y = 0
        self.largura = largura_sc
        self.altura = altura_sc
        self.tamanho = 32
        self.velocidade = 10 # pode ser mudado
        self.velocidade_diagonal = (self.velocidade - self.velocidade * 0.25) / (2 ** 1/2) # raiz de 2
        self.direcao = "DOWN"
        self.max_vida = 4 # pode ser mudada depois ou ser deixada infinita
        self.vida = self.max_vida # pode ser mudado depois
        self.timer_imune = 0
        self.visivel = True
        self.velocidade_ataque = 20 # maior = mais lento, menor = mais rapido!
        self.dano = 1

    def draw(self):
        # Desenhar o jogador sem textura
        if self.visivel:
            glColor3f(0.0, 0.0, 1.0)
            glBegin(GL_QUADS)
            glVertex2f(self.x - self.tamanho / 2, self.y - self.tamanho / 2)
            glVertex2f(self.x + self.tamanho / 2, self.y - self.tamanho / 2)
            glVertex2f(self.x + self.tamanho / 2, self.y + self.tamanho / 2)
            glVertex2f(self.x - self.tamanho / 2, self.y + self.tamanho / 2)
            glEnd()
    
    def barra_vida(self):
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glVertex2f(-self.largura + self.largura * 0.018, self.altura - self.altura * 0.023)
        glVertex2f(-self.largura + self.largura * 0.32, self.altura - self.altura * 0.023)
        glVertex2f(-self.largura + self.largura * 0.32, self.altura - self.altura * 0.055)
        glVertex2f(-self.largura + self.largura * 0.018, self.altura - self.altura * 0.055)
        glEnd()

        # Calcula a largura de cada segmento da barra de vida
        uma_barra = ((-self.largura + self.largura * 0.32) - (-self.largura + self.largura * 0.02)) / self.max_vida

        # Desenha os segmentos de vida
        for i in range(self.vida):
            glColor3f(0.0, 1.0, 0.0)
            glBegin(GL_QUADS)
            glVertex2f(-self.largura + self.largura * 0.02 + i * uma_barra, self.altura - self.altura * 0.023)
            glVertex2f(-self.largura + self.largura * 0.02 + (i + 1) * uma_barra, self.altura - self.altura * 0.023)
            glVertex2f(-self.largura + self.largura * 0.02 + (i + 1) * uma_barra, self.altura - self.altura * 0.055)
            glVertex2f(-self.largura + self.largura * 0.02 + i * uma_barra, self.altura - self.altura * 0.055)
            glEnd()
    
    def move(self, keys):
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.x = max(-self.largura + 10, self.x - self.velocidade_diagonal)
            self.y = min(self.altura + 10, self.y + self.velocidade_diagonal)
            self.direcao = "UP_LEFT"
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.x = min(self.largura + 10, self.x + self.velocidade_diagonal)
            self.y = min(self.altura + 10, self.y + self.velocidade_diagonal)
            self.direcao = "UP_RIGHT"
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.x = max(-self.largura + 10, self.x - self.velocidade_diagonal)
            self.y = max(-self.altura + 10, self.y - self.velocidade_diagonal)
            self.direcao = "DOWN_LEFT"
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.x = min(self.largura + 10, self.x + self.velocidade_diagonal)
            self.y = max(-self.altura + 10, self.y - self.velocidade_diagonal)
            self.direcao = "DOWN_RIGHT"
        elif keys[pygame.K_w]:
            self.y = min(self.altura + 10, self.y + self.velocidade)
            self.direcao = "UP"
        elif keys[pygame.K_s]:
            self.y = max(-self.altura + 10, self.y - self.velocidade)
            self.direcao = "DOWN"
        elif keys[pygame.K_a]:
            self.x = max(-self.largura + 10, self.x - self.velocidade)
            self.direcao = "LEFT"
        elif keys[pygame.K_d]:
            self.x = min(self.largura + 10, self.x + self.velocidade)
            self.direcao = "RIGHT"