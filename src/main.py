import pygame as pg #gerenciador de janelas e eventos
from pygame.locals import * #possui algumas funções e eventos usados no pygame
from OpenGL.GL import *
import random as rand #gera variaveis ou numeros aleatorios
import constantes as c

#imports do jogo
import game.classes.player as pl
import game.classes.bullet as bl
from game.classes.inimigos import inimigo_base as ib
from game.classes.maps import fase1 as ce, fase2 as cs

#inicializando e obtendo informações da tela
pg.init()
info_tela = pg.display.Info()

#definindo tamalho janela principal
lado_quadrado = info_tela.current_h
largura, altura = info_tela.current_w, info_tela.current_h
largura_map, altura_map = lado_quadrado, lado_quadrado

#inicializando janela
pg.display.set_mode((largura, altura), DOUBLEBUF | OPENGL | FULLSCREEN)

# Configuração da câmera e zoom
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-largura_map / 0.8, largura_map / 0.8, -altura_map / 0.8, altura_map / 0.8, -1, 1)
glMatrixMode(GL_MODELVIEW)

def gameLoop():
    timer_disparo = 0
    inimigos = []
    disparos = []
    clock = pg.time.Clock()
    timer_piscada = 0
    intervalo_piscada = 5

    #player
    player = pl.Player(largura_map, altura_map)

    #mapas
    city_entry = ce.City_entry(largura_map, altura_map, c.MAP_1)
    city_square = cs.City_square(largura_map, altura_map)
    
    maps = [city_entry, city_square]
    mapa_atual = 0
    
    #duracao
    duracao_fase = maps[mapa_atual].duracao_map
    contador = duracao_fase

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        maps[mapa_atual].draw_map()
            
        for inimigo in inimigos:
            inimigo.draw()
            inimigo.update(player)

        for disparo in disparos:
            disparo.draw()
            disparo.update()
        
        if(contador <= 0 and len(inimigos) == 0):
            glColor3f(1.0, 0.0, 0.0) 
            glBegin(GL_TRIANGLES)
            glVertex2f(0.0, -altura_map)
            glVertex2f(-largura * 0.05, -altura_map + altura_map * 0.1)
            glVertex2f(largura * 0.05, -altura_map + altura_map * 0.1) 
            glEnd()
        
        player.barra_vida()

        if player.visivel:
            player.draw()
        
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(-largura_map * 1.0, altura_map * 1.10)
        glVertex2f(largura_map * 1.0, altura_map * 1.10)
        glVertex2f(largura_map * 1.0, altura_map * 1.02)
        glVertex2f(-largura_map * 1.0, altura_map * 1.02)
        glEnd()

        contador -= 1

        if contador >= 0:
            porcentagem = (duracao_fase - contador) / duracao_fase
            segmento_barra = largura_map * 2.0 * porcentagem
            glColor3f(0.0, 1.0, 0.0)
            glBegin(GL_QUADS)
            glVertex2f(-largura_map * 1.0, altura_map * 1.099)
            glVertex2f(largura_map - segmento_barra, altura_map * 1.099)
            glVertex2f(largura_map - segmento_barra, altura_map * 1.021)
            glVertex2f(-largura_map * 1.0, altura_map * 1.021)
            glEnd()

        if(contador <= 0 and len(inimigos) == 0) and (player.x > (-player.largura)) and (player.x < largura * 0.1) and (player.y > -altura_map) and(player.y < (-altura_map + altura_map * 0.1)):
            mapa_atual += 1
            inimigos.clear()
            disparos.clear()
            player.x = 0
            player.y = 0
            duracao_fase = maps[mapa_atual].duracao_map
            contador = duracao_fase
            

        pg.display.flip()
        clock.tick(60)

        keys = pg.key.get_pressed()
        player.move(keys)

        if player.timer_imune > 0:
            player.timer_imune -= 1
            timer_piscada += 1
            if timer_piscada >= intervalo_piscada:
                player.visivel = not player.visivel
                timer_piscada = 0
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        if timer_disparo <= 0:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and not keys[pg.K_RIGHT]:
                if keys[pg.K_UP] and not keys[pg.K_DOWN]:
                    disparos.append(bl.Bullet(player.x, player.y, "UP_LEFT", player.dano))
                elif keys[pg.K_DOWN] and not keys[pg.K_UP]:
                    disparos.append(bl.Bullet(player.x, player.y, "DOWN_LEFT", player.dano))
                else:
                    disparos.append(bl.Bullet(player.x, player.y, "LEFT", player.dano))
            elif keys[pg.K_RIGHT] and not keys[pg.K_LEFT]:
                if keys[pg.K_UP] and not keys[pg.K_DOWN]:
                    disparos.append(bl.Bullet(player.x, player.y, "UP_RIGHT", player.dano))
                elif keys[pg.K_DOWN] and not keys[pg.K_UP]:
                    disparos.append(bl.Bullet(player.x, player.y, "DOWN_RIGHT", player.dano))
                else:
                    disparos.append(bl.Bullet(player.x, player.y, "RIGHT", player.dano))
            elif keys[pg.K_UP] and not keys[pg.K_DOWN]:
                disparos.append(bl.Bullet(player.x, player.y, "UP", player.dano))
            elif keys[pg.K_DOWN] and not keys[pg.K_UP]:
                disparos.append(bl.Bullet(player.x, player.y, "DOWN", player.dano))

            timer_disparo = player.velocidade_ataque

        timer_disparo -= 1

        if pg.time.get_ticks() % 40 == 0:
            if contador > 0:
                inimigos.append(ib.inimigo_base(inimigos, largura_map, altura_map))
                
        
        for inimigo in inimigos:
            for outro_inimigo in inimigos:
                if inimigo != outro_inimigo:
                    dist_x = inimigo.x - outro_inimigo.x
                    dist_y = inimigo.y - outro_inimigo.y
                    dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5

                    if dist_total < inimigo.tamanho * 2:  # Ajuste o valor conforme necessário
                        mov_x = (dist_x / dist_total) * 5
                        mov_y = (dist_y / dist_total) * 5
                        inimigo.x += mov_x
                        inimigo.y += mov_y
        
        if player.timer_imune <= 0:
            for inimigo in inimigos:
                if abs(inimigo.x - player.x) < player.tamanho - 1 and abs(inimigo.y - player.y) < player.tamanho - 1:
                    if abs(inimigo.x - player.x) < abs(inimigo.y - player.y):
                        inimigo.x += rand.choice([-1, 1]) * 5
                    else:
                        inimigo.y += rand.choice([-1, 1]) * 5
                    player.vida -= inimigo.dano
                    if player.vida <= 0:
                        print("Game Over")
                        pg.quit()
                        quit()
                    player.timer_imune = 180
        
        for disparo in disparos:
            for inimigo in inimigos:
                if abs(disparo.x - inimigo.x) < 32 and abs(disparo.y - inimigo.y) < 32:
                    inimigo.vida -= disparo.dano
                    if inimigo.vida <= 0:
                        inimigos.remove(inimigo)
                    disparos.remove(disparo)
                    break

if __name__ == "__main__":
    gameLoop()