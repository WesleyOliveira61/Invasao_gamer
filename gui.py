import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão
    play_button = Button(ai_settings, screen, "Play")
    
    # Cria uma instância  para armazenar dados estatístico do jogo
    stats = GameStats(ai_settings)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,  aliens, bullets)
        if stats.game_active:        
            ship.update()        
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)        
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)  
        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                         bullets, play_button)    
        

# Chamando o Objeto do jogo
run_game() 
