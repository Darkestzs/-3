class Weapon:
    def __init__(self, damage=10, modifier=1.5):
        self.damage = damage
        self._modifier = modifier
    def get_damage(self):
        return self.damage
    def set_damage(self, value):
        self.damage = value
    def get_modifier(self):
        return self._modifier
    def set_modifier(self, value):
        self._modifier = value
    def __apply_modifier(self):
        return self.damage * self._modifier
    def get_final_damage(self):
        return self.__apply_modifier()
weapon = Weapon(20, 1.3)
print(f"Базовый урон: {weapon.get_damage()}")
print(f"Финальный урон: {weapon.get_final_damage()}")
