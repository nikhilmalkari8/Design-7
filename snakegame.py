from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: list):
        self.width = width
        self.height = height
        self.food = deque(food)  # Convert food list to a deque for efficient popping
        self.snake = deque([(0, 0)])  # Snake starts at the top-left corner
        self.snake_set = {(0, 0)}  # Set to track snake's body for quick collision check
        self.score = 0

    def move(self, direction: str) -> int:
        # Get current head position
        head_x, head_y = self.snake[0]

        # Compute new head position
        if direction == "U":
            head_x -= 1
        elif direction == "D":
            head_x += 1
        elif direction == "L":
            head_y -= 1
        elif direction == "R":
            head_y += 1

        new_head = (head_x, head_y)

        # Check for boundary collision
        if head_x < 0 or head_x >= self.height or head_y < 0 or head_y >= self.width:
            return -1

        # Check for self-collision (excluding the tail, which moves if not eating)
        if new_head in self.snake_set and new_head != self.snake[-1]:
            return -1

        # Check if the snake eats food
        if self.food and self.food[0] == [head_x, head_y]:
            self.food.popleft()  # Remove the eaten food
            self.score += 1
        else:
            # Move the snake by removing the tail
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        # Add the new head
        self.snake.appendleft(new_head)
        self.snake_set.add(new_head)

        return self.score
