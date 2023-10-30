import pygame
import random

class StartGame:
    pygame.init()
    screen = pygame.display.set_mode((900, 504))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()
    pipe_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(pipe_timer, 1500)
    pipe_list_in_game = []
    bg = pygame.image.load('images/background.png')
    pipe = pygame.image.load('images/pipe.png')
    pipe = pygame.transform.scale(pipe, (100, 300))
    pipe2 = pygame.image.load('images/pipe-reversed.png')
    pipe2 = pygame.transform.scale(pipe2, (100, 300))
    bird = pygame.image.load('images/bird_upflap.png')
    bird2 = pygame.image.load('images/bird_midflap.png')
    bird3 = pygame.image.load('images/bird_downflap.png')
    game_over = pygame.image.load('images/gameover.png')
    logo = pygame.image.load('images/logo.png')
    font = pygame.font.Font('fonts/Righteous-Regular.ttf', 60)

    bird_array = [
        pygame.transform.scale(bird, (45, 45)),
        pygame.transform.scale(bird2, (45, 45)),
        pygame.transform.scale(bird3, (45, 45))
    ]

    is_jumped = False
    bird_y = 200
    jump_count = 6
    bird_el = 0
    running = True
    userSum = -1
    user_sum_arr = []

    def __init__(self):
        self.game_logic()

    def game_logic(self):
        gameplay = True
        temp_val = 0

        while self.running:
            self.screen.blit(self.logo, (10, 150))

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.bird_array[self.bird_el], (450, self.bird_y))
            bird_rect = self.bird_array[self.bird_el].get_rect(topleft=(450, self.bird_y))
            key = pygame.key.get_pressed()

            if self.bird_y >= 460:
                gameplay = False

            if gameplay:
                if self.pipe_list_in_game:
                    for el in self.pipe_list_in_game:
                        self.screen.blit(self.pipe2, el['pipe2'])
                        self.screen.blit(self.pipe, el['pipe1'])

                        el['pipe1'].x -= 10
                        el['pipe2'].x -= 10

                        if bird_rect.colliderect(el['pipe1']) or bird_rect.colliderect(el['pipe2']):
                            gameplay = False

                for i in range(len(self.user_sum_arr)):
                    self.screen.blit(self.user_sum_arr[i], (440 + i * 20, 50))

                if not self.is_jumped:
                    if key[pygame.K_SPACE]:
                        self.is_jumped = True
                    self.bird_y += (self.jump_count * abs(self.jump_count)) * 0.2

                else:
                    if self.jump_count > 0:
                        self.bird_y -= (self.jump_count * abs(self.jump_count)) * 0.6
                        self.jump_count -= 1
                    else:
                        self.jump_count = 6
                        if not key[pygame.K_SPACE]:
                            self.is_jumped = False

            else:
                self.screen.blit(self.game_over, (130, 150))

                if temp_val == 0 and self.userSum > 0 and gameplay:
                    temp_val = self.userSum

                text_result = self.font.render(f"You Result Is {temp_val}", False, (244, 165, 73))
                self.screen.blit(text_result, (240, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == self.pipe_timer:
                    second_pipe_height = random.randint(-200, 0)

                    self.pipe_list_in_game.append({
                        'pipe1': self.pipe.get_rect(topleft=(910, second_pipe_height + 420)),
                        'pipe2': self.pipe2.get_rect(topleft=(910, second_pipe_height))
                    })

                    if self.bird_el == 2:
                        self.bird_el = 0
                    else:
                        self.bird_el += 1

                    self.userSum += 1
                    self.user_sum_arr.clear()

                    for el2 in list(str(self.userSum)):
                        num = pygame.image.load(f"images/{el2}.png")
                        self.user_sum_arr.append(num)


            pygame.display.update()

            self.clock.tick(30)