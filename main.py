from game import Game

if __name__ == '__main__':
    game = Game()
    #niekończona pętla wywołująca główne funkcję
    while True:
        game.handle_events()
        game.update()
        game.draw()

