from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

class City_entry:
    def __init__(self, largura_sce, altura_sce, path_textura):
        self.id = 1
        self.largura = largura_sce
        self.altura = altura_sce
        self.duracao_map = 600 # vai ser mudado
        self.textura_path = path_textura

        self.textura = pygame.image.load(self.textura_path).convert_alpha()
        self.dados_textura = pygame.image.tostring(self.textura, "RGBA", 1)

        self.texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.textura.get_width(), self.textura.get_height(), 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.dados_textura)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    def draw_map(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glEnable(GL_BLEND)  # Habilitar blending para processar a transparência
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # Configuração do blend para processar a transparência


        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(-self.largura, -self.altura)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(self.largura, -self.altura)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(self.largura, self.altura)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(-self.largura, self.altura)
        glEnd()

        glColor3f(0.0, 0.0, 1.0)
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex2f(-self.largura, -self.altura)
        glVertex2f(self.largura, -self.altura)
        glVertex2f(self.largura, -self.altura)
        glVertex2f(self.largura, self.altura)
        glVertex2f(self.largura, self.altura)
        glVertex2f(-self.largura, self.altura)
        glVertex2f(-self.largura, self.altura)
        glVertex2f(-self.largura, -self.altura)
        glEnd()

        glDisable(GL_BLEND)  # Desabilitar blending após renderização
        glDisable(GL_TEXTURE_2D)