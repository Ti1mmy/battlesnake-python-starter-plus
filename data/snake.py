import typing
import numpy as np

class Snake:
    def __init__(self, snake_data: typing.Dict, our_snake: bool = False):
        self.health = snake_data['health']
        self.id = snake_data['id']
        self.is_our_snake = our_snake
        
        # The head is always the first index in the body
        self.tiles = np.array([(posn['x'], posn['y']) for posn in snake_data['body']])


    def copy(self) -> 'Snake':
        snake = Snake({'health': self.health, 'id': self.id, 'body': [{'x': x, 'y': y} for x, y in self.tiles]})
        snake.is_our_snake = self.is_our_snake
        return snake


    # when we move the snake we just delete the tail and add a new head in the direction we are going
    # return value is a tuple of (did we grow?, new food list)
    def move(self, direction: str, food: np.ndarray) -> typing.Tuple[bool, np.ndarray]:
        self.health -= 1
        
        new_head = (-1, -1)
        match direction:
            case 'up':
                new_head = (self.tiles[0][0], self.tiles[0][1] + 1)
            case 'down':
                new_head = (self.tiles[0][0], self.tiles[0][1] - 1)
            case 'left':
                new_head = (self.tiles[0][0] - 1, self.tiles[0][1])
            case 'right':
                new_head = (self.tiles[0][0] + 1, self.tiles[0][1])
        
        grown = False
        # Eating food        
        for food_dot in food:
            if new_head[0] == food_dot[0] and new_head[1] == food_dot[1]:
                self.health = 100
                grown = True
                # remove food from the board
                food = np.delete(food, np.where((food == food_dot).all(axis=1)), axis=0)
        
        if grown:
            # grow the snake
            self.tiles = np.roll(self.tiles, 1, axis=0)
            self.tiles[0] = new_head
            self.tiles = np.insert(self.tiles, -1, self.tiles[-1].copy(), axis=0)
        else: 
            # move the snake
            self.tiles = np.roll(self.tiles, 1, axis=0)
            self.tiles[0] = new_head
        
        return (grown, food)
