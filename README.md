from models import *

display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), WINDOW_SIZE)
#Музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()

win = font_message.render('WIN', True, (200, 100, 100) )
lose = font_message.render('LOSE', True,(200, 200, 200) )

#Игрок
player = Player('rocket.png', 250, WINDOW_SIZE[1] - SPSize[1], 15)
#Вороги
enemies = sprite.Group()
for i in range(5):
    enemies.add(Enemy("ufo.png", randint(0, WINDOW_SIZE[1] - SPSize[1]),
    randint(-260, -65), randint( 1, 3)))

clock = time.Clock()
game_over = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not game_over:
        window.blit(background, (0, 0))
        player.update_position()
        player.reset()
        player.fire()
        enemies.draw(window)
        enemies.update()

        bullets.draw(window)
        bullets.update()

        for bullet in bullets:
            for enemy in enemies:            
                if sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    enemy.kill()
                    counter.killed += 1

                    enemies.add(Enemy("ufo.png", randint(0, WINDOW_SIZE[1] - SPSize[1]),
    randint(-260, -65), randint( 1, 3)))
    
        counter.show()

        if counter.killed >= 10:
            window.blit(win, (WINDOW_SIZE[0] / 2 , WINDOW_SIZE[1] / 2))
            game_over = True
        elif counter.lost >=3 or sprite.spritecollide(player, enemies, False):
            window.blit(lose, (WINDOW_SIZE[0] / 2 , WINDOW_SIZE[1] / 2))
            game_over = True

        clock.tick(FPS)
        display.update()
