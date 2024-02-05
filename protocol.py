from typing import Protocol, abstractmethod

class AnimalProtocol(Protocol):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def sound(self) -> str:
        pass

    @abstractmethod
    def movement(self) -> str:
        pass

class Animal:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name

class Snake(Animal, AnimalProtocol):
    def sound(self) -> str:
        return "Hisses"

    def movement(self) -> str:
        return "slithers"

class Bird(Animal, AnimalProtocol):
    def sound(self) -> str:
        return "Chirps"

    def movement(self) -> str:
        return "Flys"

def main():
    # Create instances of the derived classes
    snake: AnimalProtocol = Snake("Python")
    bird: AnimalProtocol = Bird("Robin")

    print(f"The {snake.name} {snake.movement()} and {snake.sound()}")
    print(f"The {bird.name} {bird.movement()} and {bird.sound()}")

if __name__ == "__main__":
    main()