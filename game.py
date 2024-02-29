import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The big canionm")

# Variables para el jugador
player_x = 400
player_y = 500
player_speed = 5
player_image = pygame.image.load("player.png")

# Variables para los enemigos
enemy_x = 400
enemy_y = 100
enemy_speed = 2
enemy_image = pygame.image.load("enemy.png")

# Función principal del juego
def game():
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        # Mover al jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        
        # Mover al enemigo
        enemy_y += enemy_speed
        
        # Dibujar los elementos en la pantalla
        screen.fill((0, 0, 0))
        screen.blit(player_image, (player_x, player_y))
        screen.blit(enemy_image, (enemy_x, enemy_y))
        
        # Actualizar la pantalla
        pygame.display.update()        

# Ejecutar el juego
game()

# Finalizar Pygame
pygame.quit()