class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    def display_name(self):
        print(f"Dog's Name: {self.name}")


# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

#Single Inheritance
class Labrador(Dog):
    def sound(self):
        print("Labrador woof")
lab = Labrador(dog2.name, dog2.age)
lab.display_name()
lab.sound()

#Multilevel Inheritance
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guides the way!")
guide_dog = GuideDog("Max",2)
guide_dog.display_name()
guide_dog.guide()

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print("Golden Retriever Barks")
retriever = GoldenRetriever("Charlie",10)
retriever.display_name()
retriever.greet()
retriever.sound()