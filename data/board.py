import numpy as np
from data.snake import Snake

class Board:
    def __init__(self, *args):
        if len(args) == 0:
            self.instantiated = False
            self.width = 0
            self.height = 0
            self.food = np.array([])
            self.hazards = np.array([])
            self.snakes = np.array([])
            self.turn = 0

        else:
            game_data = args[0]
            self.width = game_data['board']['width']
            self.height = game_data['board']['height']
            
            self.food = np.array([(posn['x'], posn['y']) for posn in game_data['board']['food']])
            
            # Not sure if we have to use this
            self.hazards = np.array([(posn['x'], posn['y']) for posn in game_data['board']['hazards']])
            
            self.turn = game_data['turn']
            
            # read in the snakes
            self.snakes = []
            
            for snake in game_data['board']['snakes']:
                if snake['id'] == game_data['you']['id']:
                    self.snakes.append(Snake(snake, True))
                else:
                    self.snakes.append(Snake(snake))

            self.snakes = np.array(self.snakes)
            self.instantiated = True


    def copy(self):
        if not self.instantiated:
            raise Exception("Board not instantiated!")
        
        # Fill values with the same data
        board = Board()
        
        board.width = self.width
        board.height = self.height
        board.food = self.food.copy()
        board.hazards = self.hazards.copy()
        board.snakes = self.snakes.copy()
        board.instantiated = True
        return board
    
    def get_our_snake(self) -> Snake:
        if not self.instantiated:
            raise Exception("Board not instantiated!")
        return [snake for snake in self.snakes if snake.is_our_snake][0]
    
    def get_other_snakes(self, snake_id: str) -> np.ndarray:
        if not self.instantiated:
            raise Exception("Board not instantiated!")
        
        other_snakes = []
        for snake in self.snakes:
            if snake.id != snake_id:
                other_snakes.append(snake)
        return np.array(other_snakes)
    
    
    # Preferred method of moving the snake
    def move_snake(self, snake_id: str, direction: str) -> None:
        if not self.instantiated:
            raise Exception("Board not instantiated!")
        
        for snake in self.snakes:
            if snake.id == snake_id:
                self.food = snake.move(direction, self.food)[1]
                return
