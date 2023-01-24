import pygame, sys
from pygame import mixer
pygame.init()
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
clicksound = mixer.Sound("button_click.wav")
clicksound.set_volume(0.08)

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_pos_y = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#9E1414'
        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#531414'

        # the text
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw_button(self):  # draw the button function
        # elavation logic
        self.top_rect.y = self.original_pos_y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=8)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=8)
        screen.blit(self.text_surf, self.text_rect)
        self.clicked()

    def clicked(self):  # check if the mouse hover in the rectangle and the user clicked the butto
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D44646'
            if pygame.mouse.get_pressed()[0]:  # the rght clicked mouse is pressed self.pressed = true
                self.dynamic_elevation = 0
                self.pressed = True # if the user release the mouse and self.pressed == true print clicked and self.pressed = false
            if self.pressed == True:
                clicksound.play()
                self.dynamic_elevation = self.elevation
                print('works')

        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#9E1414'

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PING - PONG MASTER')
font = pygame.font.Font('munro-small.ttf', 30)
run = True
# BUTTONS
button1 = Button('START', 200, 40, (290, 250), 6)
button2 = Button('Settings', 200, 40, (290, 300), 6)
button3 = Button('Help', 200, 40, (290,350), 6)
button4 = Button('Exit',200,40,(290,400),6)
background = pygame.image.load('Background/background.png')
background_music = pygame.mixer.Sound("mainmenumusic.wav")
background_music.set_volume(0.5)
print("im back")


if __name__ == "__main__":  # this line of code only activates if this is a main file but not as sub-modules #
    background_music.play(-1)
    def title_text():
        title_font = pygame.font.SysFont('munro-small.ttf', 70, bold=pygame.font.Font.bold)
        text = title_font.render('PING PONG', True, '#FFA07A')
        texT = title_font.render('MASTER', True, '#FFA07A')
        screen.blit(texT,(270,150))
        screen.blit(text, (235, 100))


# ============ Trigger when button pressed ==================== #
    def start_button():
        global Button
        import gameplaysingleplayer
        gameplaysingleplayer
        del sys.modules["gameplaysingleplayer"]

    def gameSettings():
        global Button
        import game_settings
        game_settings
        del sys.modules["game_settings"]

    def gameHelp():
        global Button
        import Help
        Help
        del sys.modules["Help"]

    while run:
        pos = pygame.mouse.get_pos()
        # if button1.draw_button().collide
        for event in pygame.event.get():
            if event.type == pygame.QUIT or button4.pressed == True:
                pygame.quit()
                sys.exit()

        # ============ The button pressed to tirgger ==================== #

        if button1.pressed == True:
            setattr(button1, "pressed", False)
            background_music.set_volume(0)
            start_button()
            print('play')
        else:
            background_music.set_volume(0.5)

        if button2.pressed == True:
            setattr(button2, "pressed", False)
            gameSettings()
            print('settings')

        if button3.pressed == True:
            setattr(button3, "pressed", False)
            gameHelp()
            print('settings')




        screen.blit(background, (0, 0))
        title_text()
        button1.draw_button()
        button2.draw_button()
        button3.draw_button()
        button4.draw_button()
        pygame.display.update()