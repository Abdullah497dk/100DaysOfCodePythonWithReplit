
import os
import time
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def clear_screen():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    pygame.mixer.pause()

def play():
    # Play the sound
    pygame.mixer.unpause()
    print("Playing audio. Press Enter to return to menu.")
    input()
    pause()
    
def display_menu():
    print("Audio Player Menu")
    print("1. Play audio")
    print("2. Pause audio")
    print("3. Exit")
    return input("Select an option: ")

# Pause by default on start
pause()

# Main program loop
while True:
    clear_screen()
    choice = display_menu()
    
    if choice == '1':
        play()
    elif choice == '2':
        pause()
        print("Audio paused. Press Enter to continue.")
        input()
    elif choice == '3':
        print("Exiting program...")
        pygame.quit()
        break
    else:
        print("Invalid option. Press Enter to try again.")
        input()
