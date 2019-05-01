from gamelib import *

game = Game(800, 600, "backup_game")

bk = Image("trans_screen.jpg", game)
game.setBackground(bk)
bk.resizeTo(game.width, game.height)

t_s = Image("title_screen.jpg", game)
t_s.resizeTo(game.width, game.height)

hero = Image("shadow2.gif", game)
hero.resizeBy(-50)
h_x = 400
h_y = 400
hero.moveTo(h_x, h_y)


shadow = Image("shadoww.png", game)
shadow.resizeBy(-60)
shadow.setSpeed(3, 90)

f = Font(white, 45, black, "Bookman Old Style")

#Title screen
while not game.over:
    game.processInput()

    t_s.draw()
    game.drawText("BACKUP", 300, 240, f)
    game.drawText("GAME", 320, 290, f)
    
    if keys.Pressed[K_SPACE]:
        game.over = True

    game.update(60)
game.over = False

#Level 1
while not game.over:
    game.processInput()

    bk.draw()  
    hero.draw()
    shadow.move()
    shadow.visible = True

    if shadow.x < 0:
        shadow.x = 982
        shadow.y = randint(100, 550)

    if keys.Pressed[K_DOWN]:
        hero.y += 3

    if keys.Pressed[K_UP]:
        hero.y -= 3

    if keys.Pressed[K_RIGHT]:
        hero.x += 3

    if keys.Pressed[K_LEFT]:
        hero.x -= 3

    if hero.collidedWith(shadow):
        game.score += 5
        shadow.visible = False

    game.drawText("X " + str(game.score), game.width - 675, game.height - 70, f)
          
    game.update(60)
game.over = False
