from attack import Attack
from random import Random
class Character:
    def __init__(self, name, attack_power, attacks, defeat, is_enemy, health=100, ): 
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.attacks = attacks
        self.attack = ''
        self.defeat_ver = defeat
        self.is_enemy = is_enemy

    def attack(self, enemy, attack):
        enemy.health -= self.attack_power
        print(f'{enemy.name} took {attack} damage from your.')

    def receive_damage(self, enemy):
        self.health -= enemy.attack_power

    def choose_attack_methods(self):
        if self.is_enemy == True:
            self.attack = Random.choice(self.attacks)
        else:
            print(self.attacks)
            user_input = input('Which attack would you like to use?')
        return user_input

    def display_defeat (self):
        pass

    def say_something(self, message):
        print(f"{self.name}: {message}")

    def heal():
        pass

