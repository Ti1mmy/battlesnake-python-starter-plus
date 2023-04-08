from data.board import Board
from data.snake import Snake

import typing

class Battlesnake:
    def __init__(self, game_data: dict) -> None:
        self.board = Board(game_data)
        self.our_snake = self.board.get_our_snake()

    def get_best_move(self) -> str:
        # Basic implementation (you should improve this)
        moves = ["up", "down", "left", "right"]
        for move in moves:
            if self.__is_move_safe(self.our_snake, move):
                return move
        return "up"
    
    def __is_move_safe(self, snake: Snake, move: str) -> bool:
        # Basic implementation (you should improve this)
        snake_copy = snake.copy()
        snake_copy.move(move, self.board.food)
        head = snake_copy.tiles[0]
        
        # Check boundaries
        if head[0] not in range(0, self.board.width) or head[1] not in range(0, self.board.height):
            return False
        return True
