#Versao 3 do projeto jogo ritmo com acessibilidade
#Alunos: Nicolas Alteia Telles 42010225
#Augusto Esteves Carrera - 32114842
#Gustavo Fernandes Costa - 32161093
#Raphael Ferrari - 32008422

import pygame
import sys

# função para mostrar o menu
def show_menu(music_options, selected_option):
    menu_font = pygame.font.Font(None, 36)
    menu_text = menu_font.render("Selecione a música:", True, BLACK)
    screen.blit(menu_text, (20, 50))

    for index, music in enumerate(music_options):
        text = menu_font.render(f"{index + 1}. {music}", True, BLACK)
        screen.blit(text, (20, 100 + index * 30))

    # destaca a opção selecionada
    highlight_text = menu_font.render(">", True, BLACK)
    screen.blit(highlight_text, (5, 100 + selected_option * 30))

    pygame.display.update()

# inicialização do Pygame
pygame.init()

# configurações da tela
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Jogo Rítmico")

# cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# lista de opções de música
music_options = ["musica1.mp3", "musica2.mp3", "musica3.mp3"]
selected_option = 0  # opção inicial selecionada no menu

# carregando as músicas
pygame.mixer.init()
bemvindo = pygame.mixer.Sound('bemvindo1.mp3') 
beat_tick = pygame.mixer.Sound('tickbeat.wav') 
beat_tick.set_volume(10)
acerto_tick = pygame.mixer.Sound('positivefeedback1.mp3') 
pressioneparajogar = pygame.mixer.Sound('pressioneparajogar.mp3') 
musica = pygame.mixer.Sound('musica1.mp3') 
musica2 = pygame.mixer.Sound('musica2.mp3') 
musica3 = pygame.mixer.Sound('musica3.mp3') 
musica_atual = pygame.mixer.Sound(music_options[selected_option])

# dimensões do retângulo
rect_width = 50
rect_height = 50

# posição inicial do retângulo
rect_x = 175
rect_y = 225

# velocidade do retângulo
rect_speed = 0.7

# pontuação
score = 0

# variáveis para controle de tempo
clock = pygame.time.Clock()
current_time = 0
last_beat_time = 0
lock = 0
h = 0

# variável para controlar se o jogo está no menu ou em execução
in_menu = True
bemvindo.play(0)
# loop principal do jogo
running = True
while running:
    current_time = pygame.time.get_ticks() / 1000 - h  # vira segundos
    x = int(current_time)

    if in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = 0
                    in_menu = False
                    musica_atual = pygame.mixer.Sound(music_options[selected_option])
                    musica_atual.play()
                    h = pygame.time.get_ticks() / 1000
                elif event.key == pygame.K_DOWN:
                    selected_option = 1
                    in_menu = False
                    musica_atual = pygame.mixer.Sound(music_options[selected_option])
                    musica_atual.play()
                    h = pygame.time.get_ticks() / 1000
                elif event.key == pygame.K_LEFT:
                    selected_option = 2
                    in_menu = False
                    musica_atual = pygame.mixer.Sound(music_options[selected_option])
                    musica_atual.play()
                    h = pygame.time.get_ticks() / 1000

        screen.fill(WHITE)
        show_menu(music_options, selected_option)

    else:
        # movimento do retângulo
        rect_x += rect_speed
        # volta pro começo
        if rect_x > 350:
            rect_x = 0

        screen.fill(WHITE)

        # desenha o retângulo
        pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

        # desenha a linha de batida
        pygame.draw.line(screen, BLACK, (0, 225), (400, 225), 2)

        # exibe a pontuação na tela
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Pontuação: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        current_time_text = font.render(f"Tempo: {current_time:.1f} s", True, BLACK)
        screen.blit(current_time_text, (10, 50))

        #last_beat_text = font.render(f"last_beat: {last_beat_time:.1f} s", True, BLACK)
        #screen.blit(last_beat_text, (10, 70))

        if x % 2 != 0:
            last_beat_time = 0
            lock = 0

        elif x % 2 == 0:
            last_beat_time = 1
            pygame.draw.rect(screen, GREEN, (rect_x, rect_y, rect_width, rect_height))

            if round(current_time, 1) == round(float(x), 1):
                beat_tick.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # barra
                if lock == 0:
                    if last_beat_time == 1:
                        acerto_tick.play(0)
                        score += 1
                        lock = 1

        pygame.display.update()
        clock.tick(30)  # limite de taxa de quadros para 60 FPS

pygame.quit()
sys.exit()
