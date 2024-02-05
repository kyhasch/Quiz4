from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

    def movement(self):
        pass

class Snake(Animal):
    def sound(self):
        return "Hisses"

    def movement(self):
        return "slithers"

class Bird(Animal):
    def sound(self):
        return "Chirps"

    def movement(self):
        return "Flys"

def main():
    # Create instances of the derived classes
    snake = Snake("Python")
    bird = Bird("Robin")

    print(f"The {snake.name} {snake.movement()} and {snake.sound()}")
    print(f"The {bird.name} {bird.movement()} and {bird.sound()}")

if __name__ == "__main__":
    main()

