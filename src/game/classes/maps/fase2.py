from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class City_square:
    def __init__(self, largura_sce, altura_sce):
        self.id = 2
        self.largura = largura_sce
        self.altura = altura_sce
        self.duracao_map = 600 # vai ser mudado

    #textura depois!


    def draw_map(self):
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_QUADS)
        glVertex2f(-self.largura, -self.altura)
        glVertex2f(self.largura, -self.altura)
        glVertex2f(self.largura, self.altura)
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