class Animal:
    def __init__(self, name, species):
        self._name = name  # Using underscore convention for private attribute
        self._species = species

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def description(self):
        return f"A {self._name} is a {self._species}"

    @name.setter
    def name(self, value):
        self._name = value

    @species.setter
    def species(self, value):
        self._species = value

def main():
    my_animal = Animal("Python", "Snake")

    print(f"Name: {my_animal.name}")
    print(f"Species: {my_animal.species}")
    print(f"Description: {my_animal.description}")

    # Set new values
    my_animal.name = "Cat"
    my_animal.species = "Mammal"

    print(f"Updated Name: {my_animal.name}")
    print(f"Updated Species: {my_animal.species}")
    print(f"Updated Description: {my_animal.description}")

if __name__ == "__main__":
    main()