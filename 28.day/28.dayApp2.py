import pygame
import random

def diceRoll6():
    return random.randint(1, 6)

def diceRoll8():
    return random.randint(1, 8)

def diceRoll12():
    return random.randint(1, 12)

def diceRoll3():
    return random.randint(1, 3)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Character Builder Fight")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    pygame.mixer.music.load("27.day/tokyo_ghoul_ac.mp3")
    pygame.mixer.music.play(-1)
    
    input_text = ""
    phase = "name1"
    player1name, player1type, player2name, player2type = "", "", "", ""
    player1strong, player1health, player2strong, player2health = 0, 0, 0, 0
    round_count = 1
    fighting = False
    winner = ""
    
    questions = {
        "name1": "Enter Player 1's name:",
        "type1": "Enter Player 1's type (Human, Elf, Wizard, Orc):",
        "name2": "Enter Player 2's name:",
        "type2": "Enter Player 2's type (Human, Elf, Wizard, Orc):"
    }
    
    while True:
        screen.fill((0, 0, 0))
        
        if phase in questions:
            draw_text(screen, questions[phase], font, (255, 255, 255), 50, 50)
            draw_text(screen, input_text, font, (255, 255, 255), 50, 100)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if phase == "name1":
                        player1name = input_text
                        phase = "type1"
                    elif phase == "type1":
                        player1type = input_text
                        player1strong = (diceRoll6() * diceRoll8()) / 2 + 12
                        player1health = (diceRoll6() * diceRoll12()) / 2 + 10
                        phase = "name2"
                    elif phase == "name2":
                        player2name = input_text
                        phase = "type2"
                    elif phase == "type2":
                        player2type = input_text
                        player2strong = (diceRoll6() * diceRoll8()) / 2 + 12
                        player2health = (diceRoll6() * diceRoll12()) / 2 + 10
                        phase = "fight"
                        fighting = True
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        if fighting:
            screen.fill((0, 0, 0))
            draw_text(screen, f"Round {round_count}", font, (255, 255, 255), 350, 50)
            attack1 = diceRoll3() * player1strong / 25
            attack2 = diceRoll3() * player2strong / 25
            player2health -= attack1
            player1health -= attack2
            
            draw_text(screen, f"{player1name} attacks {player2name} with {attack1:.2f} damage", font, (255, 0, 0), 100, 150)
            draw_text(screen, f"{player2name} attacks {player1name} with {attack2:.2f} damage", font, (0, 0, 255), 100, 200)
            draw_text(screen, f"{player1name} Health: {player1health:.2f}", font, (255, 255, 255), 100, 300)
            draw_text(screen, f"{player2name} Health: {player2health:.2f}", font, (255, 255, 255), 100, 350)
            pygame.display.flip()
            
            pygame.time.delay(2000)
            
            if player1health <= 0 or player2health <= 0:
                winner = player1name if player2health <= 0 else player2name
                fighting = False
                phase = "gameover"
            round_count += 1
        
        if phase == "gameover":
            screen.fill((0, 0, 0))
            draw_text(screen, f"{winner} wins! Press 'R' to restart or 'Q' to quit", font, (0, 255, 0), 150, 300)
            pygame.display.flip()
            restart = False
            while not restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            return
                        elif event.key == pygame.K_r:
                            restart = True
                            main()
                            return
                        
        
        clock.tick(60)

if __name__ == "__main__":
    main()