from dataclasses import dataclass

@dataclass

class Animal:
    species: str
    type: str
    animalClass: str
    Move: str

    def display_info(self):
        print(f"Species: {self.species}")
        print(f"type: {self.type}")
        print(f"Class: {self.animalClass}")
        print(f"Movement {self.Move}")

def main():
    animal1 = Animal("Python", "Snake", "Reptile", "Slithers")
    animal2 = Animal("Cougar", "Cat", "Mammal", "walking on 4 legs")

    print("Animal 1:")
    animal1.display_info()

    print("\nAnimal 2:")
    animal2.display_info()

if __name__ == "__main__":
    main()