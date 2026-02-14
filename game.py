import game
game.init()
screen = game.display.set_mode((400,500))
done = False
while not done:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
    game.display.flip()
