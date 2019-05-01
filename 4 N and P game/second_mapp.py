#Name Incorporated
#SQUIDACUS... DA FOE IS HERE!
#Nicole Meselsohn and Preston Muirhead
#As the player, you must collect and defeat shadows to beat Da Foe -
# - and save your village from the darkness

from gamelib import *

game = Game(800, 600, "map")

mapp = Image("mapp.png", game)
mapp.resizeBy(220)
mapp.y = -225

mapp1 = Image("mapp11.png", game)
mapp1.resizeBy(180)
mapp2 = Image("mapp22.png", game)
mapp2.resizeBy(180)

tds = Image("tdsquid.png", game) #SHIP
tds.resizeBy(-35)
tds.x = 400
tds.y = 300

mapp2.y = 402

while not game.over:
    game.processInput()

    mapp1.draw()
    mapp2.draw()

    if keys.Pressed[K_DOWN]:
        mapp1.y -= 3
        mapp2.y -=3

    if keys.Pressed[K_UP]:
        mapp1.y += 3
        mapp2.y +=3

    game.update(30)
game.quit()
