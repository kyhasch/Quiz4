class Animal:
    def __init__(self, name, species):
        self._name = name  # Using underscore convention for private attribute
        self._species = species

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_species(self):
        return self._species

    def set_species(self, value):
        self._species = value

    def description(self):
        return f"A {self._name} is a {self._species}"

def main():
    my_animal = Animal("Python", "Snake")

    print(f"Name: {my_animal.get_name()}")
    print(f"Species: {my_animal.get_species()}")
    print(f"Description: {my_animal.description()}")

    # Set new values
    my_animal.set_name("Cat")
    my_animal.set_species("Mammal")

    print(f"Updated Name: {my_animal.get_name()}")
    print(f"Updated Species: {my_animal.get_species()}")
    print(f"Updated Description: {my_animal.description()}")

if __name__ == "__main__":
    main()