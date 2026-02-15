class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "..."

    def info(self):
        return f"{self.__class__.__name__} {self.name}"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


class Parrot(Animal):
    def make_sound(self):
        return "Чик-чирик!"


# Создаём зоопарк
zoo = [Dog("Бобик"), Cat("Мурка"), Parrot("Кеша")]

# Выводим информацию о животных
for animal in zoo:
    print(f"{animal.info()}: {animal.make_sound()}")