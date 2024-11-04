from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        return "У бойца нет оружия!"

# Класс Monster, представляющий монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        return f"{self.name} побежден!"

# Шаг 4: Реализуем простой механизм боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    print(monster.defeat())

# Пример использования
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч и сражается
    fighter.change_weapon(Sword())
    battle(fighter, monster)

    print()  # Пустая строка для отделения боя

    # Боец меняет оружие на лук и сражается
    fighter.change_weapon(Bow())
    battle(fighter, monster)