from Game import Game
from TetrominoFactory import TetrominoFactory
import pygame

def tetris_loop():
	game=Game()
	print(game.board)
	game.mainLoop()







if __name__ == '__main__':
	tetris_loop()