#Importing modules to be used in the code
import pygame, sys
from pygame.locals import *
    #from pygame import mixer
import random

#Initializing pygame module
pygame.init()
    #pygame.mixer.init()

#Setting up window screen with a heading
pygame.display.set_caption('MAIN MENU')
screen = pygame.display.set_mode((500, 600))

    #pygame.mixer.music.load("SS_BGMusic.mp3")
    #pygame.mixer.music.play()

#Initializing clock method
mainClock = pygame.time.Clock()

#Declaring variables for each color
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)

#Counters for checking whether music is ON or OFF
music_counter = 0
m_chk = True

#Function to insert image in the pygame window
def insert_img(IMAGE, size, x, y):

    #Loading image
    img = pygame.image.load(IMAGE)
    #Transforming image based on specific dimensions
    rimg = pygame.transform.scale(img, size)
    #Inserting image
    screen.blit(rimg, (x,y))

#Function to insert text in the pygame window
def draw_text(text, fnt, f_size, color, surface, x, y, r_size):

    #Initializing font to be used
    font = pygame.font.SysFont(fnt, f_size)
    #Loading text of specific color
    txt = font.render(text, True, color)
    #Transforming text
    rtxt = pygame.transform.scale(txt, r_size)
    #Inserting text
    screen.blit(rtxt, (x, y))

#Function executing the logic of the Game
def G_logic(bttn1, bttn2, running, i, ques, ans):

    #Variable declaring the starting point of answer box
    x_box = 90

    #Checking if user-inputted answer is equal to given answer
    if i == 8:
        pygame.draw.rect(screen, black, pygame.Rect(60, 390, 380, 180))
        draw_text("YOU WON!!", "comicsans", 210, aqua, screen, 100, 425, (310, 100))
        running = False

    #Checking when user-inputted answer is not equal to given answer
    #If last choice given to user is also wrong
    elif i == 7:
        pygame.draw.rect(screen, black, pygame.Rect(70, 390, 380, 180))
        draw_text("GAME OVER!!", "comicsans", 200, aqua, screen, 100, 385, (300, 80))
        draw_text("Answer ->", None, 100, white, screen, 85, 470, (150, 50))
        #If ans contains one/two digits only
        if ans[0] in "1234567890":
            draw_text(ans, "comicsans", 100, yellow, screen, 250, 500, (70, 60))
        #If ans contains characters
        else:
            draw_text(ans, "comicsans", 100, yellow, screen, 250, 500, (135, 65))
        running = False

    #To display question and type in answer
    else:
        draw_text(ques, None, 100, black, screen, 70, 390, (370, 50))
        #Displaying HINT only if first letter of answer is a character
        if ans[0] not in "1234567890":
            draw_text("HINT: First letter Capital", "comicsans", 100, black, screen, 80, 540, (250, 30))
        #Creating boxes for each character
        #Number of boxes determine the number of letters of the answer
        for char in ans:
            pygame.draw.rect(screen, white, pygame.Rect(x_box, 470, 32, 40))
            pygame.draw.rect(screen, black, pygame.Rect(x_box, 470, 32, 40), 3)
            x_box += 37

    #Starting point to type in character
    x_char = 100
    #List which will store alphanumeral of user typed character
    w = []

    #Loop to execute the game logic code
    while running:
        pygame.display.set_caption("GAME")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Checking of the mouse cursor is over a box and clicking within its dimensions
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Getting the positions of the mouse cursor on the screen
                mx1, my1 = pygame.mouse.get_pos()
                mx2, my2 = pygame.mouse.get_pos()
                #If mouse collides with the box redirecting to the main menu screen
                if bttn1.collidepoint((mx1, my1)):
                    main_menu()
                # If mouse collides with the box opening a new game screen
                if bttn2.collidepoint((mx2, my2)):
                    game()
            #Inputting and inserting characters on the screen
            if event.type == pygame.KEYDOWN:
                #If character typed in is alphanumeric or space then display
                if event.unicode.isalnum() or event.unicode == " ":
                    char = event.unicode
                    #Storing each character in a list
                    w += [char]
                    #If capslock is clicked then ignore space acquired by it on the screen
                    if event.key == pygame.K_CAPSLOCK:
                        x_char -= 37
                    #To display each character within each individual box
                    if x_char <= x_box:
                        f = pygame.font.Font(None, 40)
                        txt = f.render(char, True, black)
                        screen.blit(txt, (x_char-4, 478))
                        x_char += 37
                #To delete individual character
                elif event.key == pygame.K_BACKSPACE:
                    w.pop()
                    x1_char = x_char
                    if x1_char >= 125:
                        x_char -= 37
                        x1_char -= 47
                        pygame.draw.rect(screen, white, pygame.Rect(x1_char, 470, 32, 40))
                        pygame.draw.rect(screen, black, pygame.Rect(x1_char, 470, 32, 40), 3)
                        x1_char += 12
                #When user presses the Enter key
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    #This variable will store the characters of the list to checked with the actual answer
                    word = ""
                    for ltr in w:
                        word += ltr
                    #If the user's answer is not equal to actual answer
                    if word != ans:
                        #If the answer was inputted wrong for the first time
                        if i == 1:
                            insert_img(r"Hangman\Hangman\Frames\Head.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 2, ques, ans)
                        elif i == 2:
                            insert_img(r"Hangman\Hangman\Frames\Torso.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 3, ques, ans)
                        elif i == 3:
                            insert_img(r"Hangman\Hangman\Frames\LHand.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 4, ques, ans)
                        elif i == 4:
                            insert_img(r"Hangman\Hangman\Frames\RHand.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 5, ques, ans)
                        elif i == 5:
                            insert_img(r"Hangman\Hangman\Frames\LLeg.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 6, ques, ans)
                        elif i == 6:
                            insert_img(r"Hangman\Hangman\Frames\RLeg.jpg", (330, 330), 80, 30)
                            G_logic(bttn1, bttn2, running, 7, ques, ans)
                    else:
                        G_logic(bttn1, bttn2, running, 8, ques, ans)
        pygame.display.update()
        mainClock.tick(60)

def game():

    #Removing the contents of main menu window to insert new contents
    screen.fill(black)
    insert_img(r"Hangman\Hangman\Frames\MM_BG_Image.png", (500, 600), 0, 0)
    #Inserting the base image of hangman
    insert_img(r"Hangman\Hangman\Frames\Base.jpg", (340, 330), 80, 30)

    #Rectangle dimensions when clicked will redirect to main menu window screen
    bttn1 = pygame.Rect(5, 5, 40, 40)
    pygame.draw.rect(screen, white, bttn1, 2)
    draw_text('<', None, 70, white, screen, 14, 6, (20, 32))
    # Rectangle dimensions when clicked will redirect to main menu window screen
    bttn2 = pygame.Rect(450, 550, 40, 40)
    pygame.draw.rect(screen, white, bttn2, 2)
    draw_text('>', None, 70, white, screen, 461, 552, (20, 32))

    #List of questions of data type string
    ques_list = ["130 + 275 =", "Largest Planet in Solar System", "Cube Root of 64 =", "Atomic Number of Hydrogen", "131 * 0 * 30 * 4 =", "Deepest Ocean of the World", "Common Name of H2O", "'K' element in Periodic Table", "Next Prime after 7", "Highest region of Earth", "36,34,30,28,,22", "6,12,18,,30,36", "3 + 6 * (5 + 4)/3 - 7", "8.563 + 4.8292 = ", "53,53,40,40,27,27,,"]
    # List of answers of data type string
    ans_list = ["405", "Jupiter", "4", "1", "0", "Pacific", "Water", "Potassium", "11", "Tibet", "24", "24", "14", "13.3922", "14"]
    #Storing a random ques taken from ques_list
    ques = random.choice(ques_list)
    #Executing a loop to find which question was randomly stored in ques variable
    for index in range(len(ques_list)):
        if ques == ques_list[index]:
            #Storing the answer to the question at same index inn variable ans
            ans = ans_list[index]
    #Function call to the actual game logic
    G_logic(bttn1, bttn2, True, 1, ques, ans)

#Function to create options window screen
def options():

    #Declaring these variables as global for their values to be used in the program
    global music_counter, m_chk
    running = True
    #Removing the contents of main menu window to insert new contents
    screen.fill(black)
    insert_img(r"Hangman\Hangman\Frames\MM_BG_Image.png", (500, 600), 0, 0)

    #Rectangle dimensions when clicked will redirect to main menu window screen
    bttn = pygame.Rect(5, 5, 40, 40)
    pygame.draw.rect(screen, white, bttn,2)
    draw_text('<', None, 70, white, screen, 14, 6, (20, 32))

    #Code to check whether music is ON/OFF
    #It should also change to ON/OFF when music is clicked
    draw_text('MUSIC', None, 100, white, screen, 75, 150, (80, 30))
    #Dimensions of the small box displaying ON/OFF
    dim = pygame.Rect(375, 150, 40, 30)
    pygame.draw.rect(screen, black, dim)
    pygame.draw.rect(screen, white, dim, 2)

    #Checks whether original value of m_chk is True/False to display ON/OFF
    if m_chk:
        draw_text('OFF', None, 60, black, screen, 381, 158, (27, 17))
        draw_text('ON', None, 60, white, screen, 381, 158, (27, 17))
        #When box is clicked change the value
        music_counter= 1
        #When clicked next time change to OFF
        m_chk = False
    else:
        draw_text('ON', None, 60, black, screen, 381, 158, (27, 17))
        draw_text('OFF', None, 60, white, screen, 381, 158, (27, 17))
        music_counter = 0
        m_chk = True

    #Loop to execute the options window screen logic
    while running:
        pygame.display.set_caption("OPTIONS")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            #Getting the position of the mouse on the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                #Checking if mouse is clicked on the box to redirect back to the main menu screen
                if bttn.collidepoint((mx, my)):
                    main_menu()
                #If mouse is clicked on the music box change it to ON/OFF
                if dim.collidepoint((mx, my)):
                    if music_counter == 1:
                        draw_text('ON', None,60, black, screen, 381, 158, (27, 17))
                        draw_text('OFF', None,60, white, screen, 381, 158, (27, 17))
                        music_counter = 0
                    else:
                        draw_text('OFF', None,60, black, screen, 381, 158, (27, 17))
                        draw_text('ON', None,60, white, screen, 381, 158, (27, 17))
                        music_counter = 1
        pygame.display.update()
        mainClock.tick(60)

#Function to create the front page, main menu window screen
def main_menu():
    #Variable to determine which box is pressed PLAY/SETTINGS
    click = False
    #Loop to execute the logic of main menu window screen
    while True:
        screen.fill(black)
        #Inserting images
        insert_img(r"Hangman\Hangman\Frames\MM_BG_Image.png", (500, 600), 0, 0)
        insert_img(r"Hangman\Hangman\Frames\hangman.png", (200, 200), 40, 40)
        #Inserting text on the screen
        draw_text("Let's", "comicsans", 100, black, screen, 270, 90, (140, 80))
        draw_text("Play", "comicsans", 100, black, screen, 330, 170, (140, 80))
        draw_text("HANGMAN", "comicsans", 150, black, screen, 140, 240, (270, 110))

        #Checking which rectangle is clicked for redirection
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(170, 400, 170, 50)
        button_2 = pygame.Rect(170, 480, 170, 50)
        #Redirected to the game window screen
        if (button_1.collidepoint((mx, my)) and click):
            game()
        #Redirecting to the options window screen
        if (button_2.collidepoint((mx, my)) and click):
            options()
        #Creating the boxes to be displayed
        pygame.draw.rect(screen, white, button_1)
        pygame.draw.rect(screen, black, button_1,3)
        draw_text('PLAY', None, 70, black, screen, 220, 402, (70, 50))
        pygame.draw.rect(screen, white, button_2)
        pygame.draw.rect(screen, black, button_2,3)
        draw_text('SETTINGS', None, 70, black, screen, 200, 482, (110, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #Checking if mouse cursor is clicked
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #Displaying the contents on screen
        pygame.display.update()
        #Dertermining frame rate
        mainClock.tick(60)

#Calling the first function to start the program code
main_menu()