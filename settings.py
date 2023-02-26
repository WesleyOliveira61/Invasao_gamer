class Settings():
    """Uma classe para armazenar todas as configuração do jogo"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = '#f2f2f2'
        # Configuranção da espaçonave
        self.ship_speed_factor = 1.5

        # Configuração do da classe bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3