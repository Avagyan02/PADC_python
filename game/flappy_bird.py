import random
import pygame

class GameProperties:
    # game properties images, fonts, timer, etc
    def __init__(self):
        try:
            pygame.init()
            self.screen = pygame.display.set_mode((900, 504))
            pygame.display.set_caption('My game')
            self.clock = pygame.time.Clock()
            self.pipe_timer = pygame.USEREVENT + 1
            pygame.time.set_timer(self.pipe_timer, 1500)
            self.pipe_list_in_game = []
            self.bg = pygame.image.load('images/other/background.png')
            self.pipe = pygame.image.load('images/other/pipe.png')
            self.pipe2 = pygame.image.load('images/other/pipe-reversed.png')
            self.bird = pygame.image.load('images/bird/bird_upflap.png')
            self.bird2 = pygame.image.load('images/bird/bird_midflap.png')
            self.bird3 = pygame.image.load('images/bird/bird_downflap.png')
            self.game_over = pygame.image.load('images/other/gameover.png')
            self.logo = pygame.image.load('images/other/logo.png')
            self.font = pygame.font.Font('fonts/Righteous-Regular.ttf', 60)
            self.pipe = pygame.transform.scale(self.pipe, (100, 300))
            self.pipe2 = pygame.transform.scale(self.pipe2, (100, 300))

            self.bird_array = [
                pygame.transform.scale(self.bird, (45, 45)),
                pygame.transform.scale(self.bird2, (45, 45)),
                pygame.transform.scale(self.bird3, (45, 45))
            ]

            self.is_jumped = False
            self.running = True
            self.bird_y = 200
            self.jump_count = 6
            self.bird_el = 0
            self.user_sum = -1
            self.user_sum_arr = []
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print(f'Something went wrong: {e}')


class StartGame:
    def __init__(self):
        self.game_properties = GameProperties()
        self.game_logic()

    def game_logic(self):
        # base logic function
        try:
            gameplay = True
            temp_val = 0

            while self.game_properties.running:
                bird_rect = (
                    self.game_properties.bird_array[self.game_properties.bird_el].get_rect(
                        topleft=(450, self.game_properties.bird_y)
                    )
                )
                self.base_elements_render()
                key = pygame.key.get_pressed()

                if self.game_properties.bird_y >= 460:
                    gameplay = False

                if gameplay:
                    if self.game_properties.pipe_list_in_game:
                        for el in self.game_properties.pipe_list_in_game:
                            self.game_properties.screen.blit(
                                self.game_properties.pipe2, el['pipe2']
                            )
                            self.game_properties.screen.blit(
                                self.game_properties.pipe, el['pipe1']
                            )

                            el['pipe1'].x -= 10
                            el['pipe2'].x -= 10

                            if (bird_rect.colliderect(el['pipe1'])
                                    or bird_rect.colliderect(el['pipe2'])):
                                gameplay = False

                    for i in range(len(self.game_properties.user_sum_arr)):
                        self.game_properties.screen.blit(
                            self.game_properties.user_sum_arr[i], (440 + i * 20, 50)
                        )

                    if not self.game_properties.is_jumped:
                        if key[pygame.K_SPACE]:
                            self.game_properties.is_jumped = True
                        self.game_properties.bird_y += (
                            self.game_properties.jump_count * abs(self.game_properties.jump_count)
                        ) * 0.2
                    else:
                        if self.game_properties.jump_count > 0:
                            self.game_properties.bird_y -= (
                                self.game_properties.jump_count
                                    * abs(self.game_properties.jump_count)) * 0.6
                            self.game_properties.jump_count -= 1
                        else:
                            self.game_properties.jump_count = 6
                            if not key[pygame.K_SPACE]:
                                self.game_properties.is_jumped = False

                else:
                    self.game_properties.screen.blit(
                        self.game_properties.game_over, (130, 150)
                    )
                    if temp_val == 0 and self.game_properties.user_sum > 0 and gameplay:
                        temp_val = self.game_properties.user_sum

                    text_result = self.game_properties.font.render(
                        f"You'r Result Is {temp_val}", False, (244, 165, 73)
                    )
                    self.game_properties.screen.blit(text_result, (240, 300))

                self.event_handler()
                pygame.display.update()
                self.game_properties.clock.tick(30)
        except Exception:
            print('Something went wrong')

    def event_handler(self):
        # even handler for jump etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_properties.running = False
                pygame.quit()

            if event.type == self.game_properties.pipe_timer:
                second_pipe_height = random.randint(-200, 0)

                self.game_properties.pipe_list_in_game.append({
                    'pipe1': self.game_properties.pipe.get_rect(
                        topleft=(910, second_pipe_height + 420)
                    ),
                    'pipe2': self.game_properties.pipe2.get_rect(
                        topleft=(910, second_pipe_height)
                    )
                })

                if self.game_properties.bird_el == 2:
                    self.game_properties.bird_el = 0
                else:
                    self.game_properties.bird_el += 1

                self.game_properties.user_sum += 1
                self.game_properties.user_sum_arr.clear()

                for el2 in list(str(self.game_properties.user_sum)):
                    num = pygame.image.load(
                        f"images/numbers/{el2}.png"
                    )
                    self.game_properties.user_sum_arr.append(num)


    def base_elements_render(self):
        # base elements show method
        self.game_properties.screen.blit(self.game_properties.logo, (10, 150))
        self.game_properties.screen.blit(self.game_properties.bg, (0, 0))
        self.game_properties.screen.blit(
            self.game_properties.bird_array[self.game_properties.bird_el],
            (450, self.game_properties.bird_y)
        )
