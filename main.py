# Programmer(s): Brennan, Kaleb
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import *
from ucc_sprite import Sprite

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((640, 360))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()
squares = pygame.sprite.Group()
# x_turns = pygame.sprite.Group()
# o_turns = pygame.sprite.Group()
win1 = pygame.sprite.Group()
win2 = pygame.sprite.Group()
win3 = pygame.sprite.Group()
win4 = pygame.sprite.Group()
win5 = pygame.sprite.Group()
win6 = pygame.sprite.Group()
win7 = pygame.sprite.Group()
win8 = pygame.sprite.Group()
turn_colour = pygame.sprite.Group()
### LOAD IMAGES AND FONTS
board_image = pygame.image.load("Tic-Tac-Toe-Board.png").convert_alpha()
board_image = pygame.transform.rotozoom(board_image, 0, 0.5)

pin_image = pygame.image.load("download.png").convert_alpha()
pin_image = pygame.transform.rotozoom(pin_image, 0, 0.4)

turn_background = pygame.image.load("White_full.png").convert_alpha()
turn_background = pygame.transform.rotozoom(turn_background, 0, 0.1)

Font = pygame.font.Font("DecarySans_PERSONAL_USE_ONLY.otf", 36)
Font_big = pygame.font.Font("DecarySans_PERSONAL_USE_ONLY.otf", 108)
score_font = pygame.font.Font("Decadence.ttf", 36)

black_line = pygame.image.load("1625.png").convert_alpha()
black_line = pygame.transform.rotozoom(black_line, 0, 0.085)

chart_image = pygame.image.load("t-chart-image.png").convert_alpha()
chart_image = pygame.transform.rotozoom(chart_image, 0, 0.3)

white_square = pygame.image.load("download-_2_.png").convert_alpha()
white_square = pygame.transform.rotozoom(white_square, 0, 0.3)


# Background image
background = pygame.image.load("corkboard-background-texture-brown-cork-board-surface-33440314.jpg").convert()
screen.blit(background, (0, 0))
# Replace ... with your image

turn = "X"


### CREATE SPRITES
board = Sprite(board_image)
board.center = (430, 180)
board.rotates = False
board.add(all_sprites)

pin1 = Sprite(pin_image)
pin1.center = (280, 305)
pin1.rotates = False
pin1.add(all_sprites)

pin2 = Sprite(pin_image)
pin2.center = (280, 60)
pin2.rotates = False
pin2.add(all_sprites)

pin3 = Sprite(pin_image)
pin3.center = (567, 60)
pin3.rotates = False
pin3.add(all_sprites)

pin4 = Sprite(pin_image)
pin4.center = (567, 305)
pin4.rotates = False
pin4.add(all_sprites)

turn_back = Sprite(turn_background)
turn_back.center = (120, 80)
turn_back.rotates = False
turn_back.add(all_sprites)

x_turn = Font.render("X", True, "red")
x_turn = Sprite(x_turn)
x_turn.center = (70, 80)
x_turn.add(all_sprites)

o_turn = Font.render("O", True, "black")
o_turn = Sprite(o_turn)
o_turn.center = (168, 80)
o_turn.add(all_sprites)

line = Sprite(black_line)
line.center = (120, 80)
line.rotates = False
line.add(all_sprites)

pin5 = Sprite(pin_image)
pin5.center = (120, 58)
pin5.rotates = False
pin5.add(all_sprites)

chart = Sprite(chart_image)
chart.center = (124, 250)
chart.rotates = False
chart.add(all_sprites)

square1 = Sprite(white_square)
square1.center = (340, 100)
square1.rotates = False
square1.add(all_sprites, squares, win1, win4, win7)
square1.value = None

square2 = Sprite(white_square)
square2.center = (435, 100)
square2.rotates = False
square2.add(all_sprites, squares, win1, win5)
square2.value = None

square3 = Sprite(white_square)
square3.center = (520, 100)
square3.rotates = False
square3.add(all_sprites, squares, win1, win6, win8)
square3.value = None

square4 = Sprite(white_square)
square4.center = (340, 183)
square4.rotates = False
square4.add(all_sprites, squares, win2, win4)
square4.value = None

square5 = Sprite(white_square)
square5.center = (435, 180)
square5.rotates = False
square5.add(all_sprites,squares, win2, win5, win7, win8)
square5.value = None

square6 = Sprite(white_square)
square6.center = (520, 183)
square6.rotates = False
square6.add(all_sprites, squares, win2, win6)
square6.value = None

square7 = Sprite(white_square)
square7.center = (340, 263)
square7.rotates = False
square7.add(all_sprites, squares, win3, win4, win8)
square7.value = None

square8 = Sprite(white_square)
square8.center = (435, 263)
square8.rotates = False
square8.add(all_sprites, squares, win3, win5)
square8.value = None

square9 = Sprite(white_square)
square9.center = (520, 263)
square9.rotates = False
square9.add(all_sprites, squares, win3, win6, win7)
square9.value = None

x_wins = Font_big.render("X WINS!", True, "red")
x_wins = Sprite(x_wins)
x_wins.center = (320, 190)

o_wins = Font_big.render("O WINS!", True, "red")
o_wins = Sprite(o_wins)
o_wins.center = (320, 190)

draw = Font_big.render("DRAW!", True, "red")
draw = Sprite(draw)
draw.center = (320, 190)


NEW_GAME_EVENT = pygame.event.custom_type()


### CREATE TIMER
turn_number = 0
o_score = 0
x_score = 0

x_score_text_image = score_font.render(f"{x_score}", True, "black")
x_score_text = Sprite(x_score_text_image)
x_score_text.center = (65, 165)
x_score_text.add(all_sprites)

o_score_text_image = score_font.render(f"{o_score}", True, "black")
o_score_text = Sprite(o_score_text_image)
o_score_text.center = (160, 165)
o_score_text.add(all_sprites)



# Main Loop
while True:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    # Draw the background
    all_sprites.clear(screen, background)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        ### HANDLE EVENTS
        elif event.type == MOUSEBUTTONDOWN:
            for square in squares:
                if square.contains_point(event.pos):
                    square.image = Font.render(turn, True, "black")
                    square.value = turn
                    turn_number += 1

                    for win_group in [win1, win2, win3, win4, win5, win6, win7, win8]:
                        count_x = 0
                        count_o = 0
                        for square in win_group:
                            if square.value == "X":
                                count_x += 1
                                
                            elif square.value == "O":
                                count_o += 1
                               
                        if count_x == 3:
                            x_wins.add(all_sprites)
                            pygame.time.set_timer(NEW_GAME_EVENT, 3000, 1)
                            x_score += 1
                            x_score_text.image = score_font.render(f"{x_score}", True, "black")
                            
                        elif count_o == 3:
                            o_wins.add(all_sprites)
                            pygame.time.set_timer(NEW_GAME_EVENT, 3000, 1)
                            o_score += 1
                            o_score_text.image = score_font.render(f"{o_score}", True, "black")
                            
                        elif turn_number == 9:
                            draw.add(all_sprites)
                            pygame.time.set_timer(NEW_GAME_EVENT, 3000, 1)
                        
                        

                    # Check for draw
    
                    
                    if turn == "X":
                        o_turn.image = Font.render("O", True, "red")
                        x_turn.image = Font.render("X", True, "black")
                        turn = "O"
                    elif turn == "O":
                        x_turn.image = Font.render("X", True, "red")
                        o_turn.image = Font.render("O", True, "black")
                        turn = "X"   

               

        elif event.type == NEW_GAME_EVENT:
            turn = "X"
            x_turn.image = Font.render("X", True, "red")
            o_turn.image = Font.render("O", True, "black")
            x_wins.kill()
            o_wins.kill()
            draw.kill()
            turn_number = 0
            for square in squares:
                square.image = white_square
                square.value = None
            
    # Update the sprites' locations
    all_sprites.update()

    ### COLLISION DETECTION, ETC.
    

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()